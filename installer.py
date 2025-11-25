# installer.py
import os
import requests
import subprocess
import winreg
import time
from apps_config import APPS
from persistence import MemoryBank

class InstallerEngine:
    def __init__(self, log_callback=None, progress_callback=None):
        self.download_dir = os.path.join(os.getcwd(), "downloads")
        self.db = MemoryBank()
        self.log_callback = log_callback
        self.progress_callback = progress_callback # (app_id, percent, speed_str)
        
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def log(self, message):
        if self.log_callback:
            self.log_callback(message)
        print(f"[LOG] {message}")

    def update_progress(self, app_id, percent, speed=""):
        if self.progress_callback:
            self.progress_callback(app_id, percent, speed)

    def get_installed_apps_from_registry(self):
        installed_names = set()
        uninstall_paths = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        ]
        for root, path in uninstall_paths:
            try:
                with winreg.OpenKey(root, path) as key:
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            with winreg.OpenKey(key, subkey_name) as subkey:
                                try:
                                    display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                    if display_name:
                                        installed_names.add(display_name.lower())
                                except FileNotFoundError:
                                    pass
                        except Exception:
                            continue
            except Exception:
                continue
        return installed_names

    def get_all_system_apps(self):
        """Sistemde yüklü TÜM uygulamaları döndürür (Registry taraması)."""
        installed_list = []
        uninstall_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ]
        
        for p in uninstall_paths:
            for root in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
                try:
                    key = winreg.OpenKey(root, p)
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        try:
                            sub_key_name = winreg.EnumKey(key, i)
                            sub_key = winreg.OpenKey(key, sub_key_name)
                            try:
                                display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                                try:
                                    version = winreg.QueryValueEx(sub_key, "DisplayVersion")[0]
                                except:
                                    version = "Bilinmiyor"
                                    
                                if display_name:
                                    installed_list.append({"name": display_name, "version": version})
                            except FileNotFoundError:
                                pass
                            finally:
                                winreg.CloseKey(sub_key)
                        except Exception:
                            pass
                    winreg.CloseKey(key)
                except Exception:
                    pass
                    
        # Tekrarlananları temizle ve isme göre sırala
        unique_apps = {app['name']: app for app in installed_list}.values()
        return sorted(unique_apps, key=lambda x: x['name'])

    def check_installed_apps(self):
        self.log("Sistem taranıyor (Deep Scan)...")
        registry_apps = self.get_installed_apps_from_registry()
        
        for app_id, data in APPS.items():
            is_installed = False
            if "check_paths" in data and data["check_paths"]:
                for path in data["check_paths"]:
                    if os.path.exists(path):
                        is_installed = True
                        break
            
            if not is_installed and "keywords" in data:
                for keyword in data["keywords"]:
                    keyword_lower = keyword.lower()
                    for reg_app in registry_apps:
                        if keyword_lower in reg_app:
                            is_installed = True
                            break
                    if is_installed:
                        break

            if is_installed:
                self.log(f"Algılandı: {data['name']}")
                self.db.update_app_status(app_id, data['name'], "installed")
        self.log("Tarama tamamlandı.")

    def download_file(self, app_id, url, filename):
        filepath = os.path.join(self.download_dir, filename)
        try:
            self.log(f"İndiriliyor: {filename}...")
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            block_size = 8192
            downloaded_size = 0
            start_time = time.time()
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=block_size):
                    downloaded_size += len(chunk)
                    f.write(chunk)
                    
                    # İlerleme Hesaplama
                    if total_size > 0:
                        percent = (downloaded_size / total_size)
                        
                        # Hız Hesaplama
                        elapsed_time = time.time() - start_time
                        if elapsed_time > 0:
                            speed = (downloaded_size / 1024 / 1024) / elapsed_time # MB/s
                            speed_str = f"{speed:.1f} MB/s"
                        else:
                            speed_str = "..."
                            
                        self.update_progress(app_id, percent, speed_str)
            
            self.update_progress(app_id, 1.0, "Tamamlandı")
            self.log(f"İndirme Tamamlandı: {filename}")
            return filepath
        except Exception as e:
            self.log(f"HATA (İndirme): {filename} - {str(e)}")
            self.update_progress(app_id, 0, "Hata")
            return None

    def install_app_process(self, app_id, override_url=None):
        """Tek bir uygulamayı indirip kurar (Sıralı işlem için)."""
        app_info = APPS.get(app_id)
        if not app_info:
            return False

        # Eğer override_url varsa (sürüm seçimi vb.), onu kullan, yoksa config'dekini
        url = override_url if override_url else app_info["url"]
        silent_args = app_info.get("silent_args", [])
        
        try:
            # 1. İndir (Eğer override_url varsa ismi özelleştir ki karışmasın)
            filename = f"{app_id}_installer.exe"
            installer_path = self.download_file(app_id, url, filename)
            
            if not installer_path:
                self.log(f"HATA: İndirme başarısız -> {app_info['name']}")
                return False

            # 2. Kur
            self.log(f"Kuruluyor: {app_info['name']} (Yönetici izni isteniyor)...")
            self.update_progress(app_id, 1.0, "Kuruluyor...")
            
            args_str = " ".join(silent_args)
            ps_command = [
                "powershell",
                "-Command",
                f"Start-Process -FilePath '{installer_path}' -ArgumentList '{args_str}' -Verb RunAs -Wait"
            ]
            
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            result = subprocess.run(ps_command, check=True, startupinfo=startupinfo)
            
            if result.returncode == 0:
                self.log(f"Kurulum Başarılı: {app_info['name']}")
                self.db.update_app_status(app_id, app_info['name'], "installed")
                self.update_progress(app_id, 1.0, "Yüklendi")
                # Temizlik
                try:
                    os.remove(installer_path)
                except:
                    pass
                return True
            else:
                self.log(f"HATA (Kurulum): {app_info['name']} - Kod: {result.returncode}")
                self.update_progress(app_id, 0, "Hata")
                return False

        except Exception as e:
            self.log(f"HATA (İşlem): {app_info['name']} - {str(e)}")
            self.update_progress(app_id, 0, "Hata")
            return False

    def uninstall_app_process(self, app_id):
        app_info = APPS.get(app_id)
        if not app_info:
            return
        self.log(f"Kaldırma işlemi başlatılıyor: {app_info['name']}...")
        try:
            subprocess.Popen("appwiz.cpl", shell=True)
            self.log(f"Lütfen açılan pencereden {app_info['name']} uygulamasını kaldırın.")
            self.db.update_app_status(app_id, app_info['name'], "not_installed")
        except Exception as e:
            self.log(f"HATA (Kaldırma): {str(e)}")

    def process_queue(self, app_ids):
        """Seçilen uygulamaları SIRAYLA indirir ve kurar."""
        self.log(f"İşlem Başlıyor: {len(app_ids)} uygulama seçildi.")

        for app_id in app_ids:
            # install_app_process artık indirmeyi de içinde yapıyor
            self.install_app_process(app_id)
        
        self.log("Tüm işlemler tamamlandı.")
