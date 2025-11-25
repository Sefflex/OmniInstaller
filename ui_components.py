# ui_components.py
import customtkinter as ctk
from PIL import Image
import os
import requests
from io import BytesIO
import threading
import queue
from localization import Locale

# Global resim kuyruğu
IMAGE_QUEUE = queue.Queue()

def start_image_dispatcher(root_widget):
    """Kuyruktaki resim yükleme işlerini ana thread'de işler."""
    def _check_queue():
        try:
            while True:
                callback, image = IMAGE_QUEUE.get_nowait()
                try:
                    callback(image)
                except Exception as e:
                    print(f"Error in image callback: {e}")
        except queue.Empty:
            pass
        root_widget.after(100, _check_queue)
    
    _check_queue()

import concurrent.futures
from urllib.parse import urlparse, quote
from PIL import Image, ImageDraw, ImageFont
import random
import re

# Global ThreadPool (20 Worker)
ICON_EXECUTOR = concurrent.futures.ThreadPoolExecutor(max_workers=20)

class SmartIconLoader:
    """
    RAM-Only Akıllı İkon Yükleyici.
    Öncelik: Walkx CDN (GitHub) -> Google Favicon API -> Harfli Placeholder
    Disk I/O YOK.
    """
    _cache = {}
    
    @classmethod
    def load(cls, app_data, callback):
        """
        app_data: Uygulama verisi sözlüğü (name, icon_url, url, website vb. içerir)
        callback: (PIL.Image) -> None
        """
        # Cache Key: icon_url > name
        cache_key = app_data.get("icon_url") or app_data.get("name")
        
        if not cache_key:
            return

        if cache_key in cls._cache:
            callback(cls._cache[cache_key])
            return

        ICON_EXECUTOR.submit(cls._fetch_task, app_data, cache_key, callback)

    @classmethod
    def _fetch_task(cls, app_data, cache_key, callback):
        try:
            pil_image = None
            
            # 1. Adım: Walkx Dashboard Icons (GitHub CDN) - En Yüksek Başarı Oranı
            app_name = app_data.get("name")
            if app_name:
                pil_image = cls._fetch_from_walkx(app_name)

            # 2. Adım: Config'deki icon_url (Varsa ve Walkx'ta bulunamadıysa)
            # Kullanıcı "generic domains return wrong icons" dediği için bunu 2. sıraya koyuyoruz.
            # Ancak Walkx'ta yoksa, config'deki özel URL (varsa) iyidir.
            if not pil_image and app_data.get("icon_url"):
                pil_image = cls._download_image(app_data["icon_url"])

            # 3. Adım: Google Favicon API (Domain Fallback)
            if not pil_image:
                target_url = app_data.get("website") or app_data.get("url")
                if target_url:
                    domain = urlparse(target_url).netloc
                    if domain:
                        google_api_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
                        pil_image = cls._download_image(google_api_url)

            # 4. Adım: Harfli Placeholder (Son Çare)
            if not pil_image:
                pil_image = cls._generate_placeholder(app_name)

            # 5. Adım: İşle (Resize & Cache)
            if pil_image:
                pil_image = pil_image.resize((48, 48), Image.Resampling.LANCZOS)
                cls._cache[cache_key] = pil_image
                IMAGE_QUEUE.put((callback, pil_image))

        except Exception as e:
            print(f"SmartIconLoader Error: {e}")

    @classmethod
    def _slugify(cls, text):
        """
        App Name -> Slug
        Example: "Visual Studio Code" -> "visual-studio-code"
        Example: "Node.js" -> "node-js" (veya "nodejs", Walkx genelde tire sever ama nokta silinir)
        Kural: Lowercase, space->hyphen, remove special chars.
        """
        if not text: return ""
        text = text.lower()
        text = text.replace(" ", "-")
        # Sadece a-z, 0-9 ve - kalsın
        text = re.sub(r'[^a-z0-9-]', '', text)
        return text

    @classmethod
    def _fetch_from_walkx(cls, app_name):
        """Walkxcode Dashboard Icons CDN'inden ikon çeker."""
        try:
            slug = cls._slugify(app_name)
            if not slug: return None
            
            # Walkx CDN URL
            url = f"https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/{slug}.png"
            
            return cls._download_image(url)
        except:
            pass
        return None

    @classmethod
    def _download_image(cls, url):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                img_data = BytesIO(response.content)
                return Image.open(img_data)
        except:
            pass
        return None

    @classmethod
    def _generate_placeholder(cls, text):
        """Rastgele renkli bir kutu üzerine ilk harfi çizer."""
        try:
            # Rastgele pastel renkler
            colors = [
                (26, 188, 156), (46, 204, 113), (52, 152, 219), (155, 89, 182),
                (52, 73, 94), (22, 160, 133), (39, 174, 96), (41, 128, 185),
                (142, 68, 173), (44, 62, 80), (241, 196, 15), (230, 126, 34),
                (231, 76, 60), (243, 156, 18), (211, 84, 0), (192, 57, 43)
            ]
            bg_color = random.choice(colors)
            
            img = Image.new('RGB', (128, 128), color=bg_color)
            draw = ImageDraw.Draw(img)
            
            # İlk harfi al
            char = text[0].upper() if text else "?"
            
            # Font yüklemeyi dene, yoksa varsayılanı kullan
            try:
                # Windows'ta Segoe UI veya Arial bold deneyelim
                font = ImageFont.truetype("arialbd.ttf", 64)
            except:
                font = ImageFont.load_default()
                
            # Yazıyı ortala (Basit hesaplama)
            # ImageFont.getbbox yeni pillow sürümlerinde var, eskilerde getsize
            # Basitçe ortaya çizelim
            draw.text((64, 64), char, font=font, fill="white", anchor="mm")
            
            return img
        except Exception as e:
            print(f"Placeholder Error: {e}")
            return Image.new('RGB', (48, 48), color=(50, 50, 50))

class AppCard(ctk.CTkFrame):
    def __init__(self, master, app_id, app_data, status, on_select_change, on_action_click, on_uninstall_click):
        super().__init__(master, corner_radius=15, border_width=2, border_color="#2B2B2B", fg_color=("gray95", "#212121"))
        self.app_id = app_id
        self.app_data = app_data
        self.status = status
        self.on_select_change = on_select_change
        self.on_action_click = on_action_click # Bu artık "Detayları Aç" fonksiyonu
        self.on_uninstall_click = on_uninstall_click
        
        # Hover Efektleri için renkler
        self.default_color = ("gray95", "#212121")
        self.hover_color = ("gray85", "#2A2A2A")
        
        self.setup_ui()
        self.load_icon()
        
        # Event Binding (Tüm karta tıklama özelliği)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_card_click)
        
        # Alt widgetlara da bind etmemiz lazım ki tıklama çalışsın
        for widget in self.winfo_children():
            if not isinstance(widget, (ctk.CTkButton, ctk.CTkCheckBox)):
                widget.bind("<Button-1>", self._on_card_click)
                widget.bind("<Enter>", self._on_enter)
                widget.bind("<Leave>", self._on_leave)

    def setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # 0. İkon
        self.icon_image = None
        self.icon_label = ctk.CTkLabel(self, text="📦", font=("Arial", 32), width=48, height=48, fg_color="#333", corner_radius=10)
        self.icon_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        # 1. Başlık ve Kategori
        self.lbl_name = ctk.CTkLabel(self, text=self.app_data['name'], font=("Roboto", 16, "bold"))
        self.lbl_name.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
        
        self.lbl_cat = ctk.CTkLabel(self, text=self.app_data['category'], font=("Roboto", 12), text_color="gray")
        self.lbl_cat.grid(row=1, column=1, padx=(0, 10), pady=(0, 5), sticky="w")

        # 2. Durum Rozeti
        self.update_badge()

        # 3. Açıklama
        desc = self.app_data.get('description', '')
        # Çok uzun açıklamaları kısalt
        if len(desc) > 60: desc = desc[:57] + "..."
        
        self.lbl_desc = ctk.CTkLabel(self, text=desc, wraplength=220, justify="left", text_color="#A0A0A0")
        self.lbl_desc.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nw")

        # 4. Alt Kontroller
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        
        # Checkbox (Toplu işlem için)
        self.var_select = ctk.BooleanVar()
        self.chk_select = ctk.CTkCheckBox(self.bottom_frame, text="", variable=self.var_select, command=self._on_check, width=24, height=24)
        self.chk_select.pack(side="left")

        # Action Buttons Container
        self.action_frame = ctk.CTkFrame(self.bottom_frame, fg_color="transparent")
        self.action_frame.pack(side="right")

        # Hızlı Yükle Butonu (Detay sayfasına gitmeden yüklemek isteyenler için)
        # Ancak kullanıcı "Tıklayınca detay açılsın" dediği için, buraya "Detay" butonu yerine
        # direkt "Yükle" butonu koyuyoruz ama kartın kendisine tıklayınca detay açılıyor.
        self.btn_action = ctk.CTkButton(self.action_frame, text="Yükle", command=self._on_quick_install, width=80, height=28)
        self.btn_action.pack(side="right")
        
        self.btn_uninstall = ctk.CTkButton(self.action_frame, text="Sil", command=self._on_uninstall, width=60, height=28, fg_color="#D32F2F", hover_color="#B71C1C")
        
        # Progress Bar (Gizli Başlar)
        self.progress_frame = ctk.CTkFrame(self.bottom_frame, fg_color="transparent")
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame, width=120, height=10)
        self.progress_bar.pack(pady=(0, 2))
        self.lbl_speed = ctk.CTkLabel(self.progress_frame, text="0.0 MB/s", font=("Roboto", 10), text_color="gray")
        self.lbl_speed.pack()
        
        self.update_buttons()

    def _on_enter(self, event):
        self.configure(fg_color=self.hover_color)

    def _on_leave(self, event):
        self.configure(fg_color=self.default_color)

    def _on_card_click(self, event):
        # Karta tıklanınca detay sayfasını aç
        if self.on_action_click:
            self.on_action_click(self.app_id)

    def _on_quick_install(self):
        if hasattr(self, 'on_quick_install'):
            self.on_quick_install()
        elif self.on_action_click:
            # Fallback olarak detay sayfasını aç
            self.on_action_click(self.app_id)

    def load_icon(self):
        # SmartIconLoader artık tüm app_data'yı alıyor (Fallback için)
        SmartIconLoader.load(self.app_data, self._update_icon_ui)

    def _update_icon_ui(self, pil_image):
        # Burası ImageDispatcher tarafından ANA THREAD'de çağrılır.
        try:
            self.icon_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(48, 48))
            self.icon_label.configure(image=self.icon_image, text="")
        except Exception as e:
            print(f"Error setting icon for {self.app_id}: {e}")

    def update_badge(self):
        status_color = "#4CAF50" if self.status == "installed" else "#757575"
        status_text = Locale.get("status_installed") if self.status == "installed" else Locale.get("status_not_installed")
        
        if hasattr(self, 'badge'):
            self.badge.configure(text=status_text, fg_color=status_color)
        else:
            self.badge = ctk.CTkLabel(self, text=status_text, fg_color=status_color, corner_radius=8, text_color="white", padx=8, pady=2)
            self.badge.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def update_buttons(self):
        if self.status == "installed":
            self.btn_action.configure(text=Locale.get("btn_reinstall"), fg_color="#2d2d2d")
            self.btn_uninstall.pack(side="right", padx=(0, 5))
        else:
            self.btn_action.configure(text=Locale.get("btn_install"), fg_color="#1f6aa5")
            self.btn_uninstall.pack_forget()

    def set_progress(self, percent, speed_str):
        """İlerleme durumunu günceller."""
        if percent < 1.0:
            # Yükleme moduna geç
            self.action_frame.pack_forget()
            self.progress_frame.pack(side="right")
            self.progress_bar.set(percent)
            self.lbl_speed.configure(text=speed_str)
        else:
            # Normal moda dön
            self.progress_frame.pack_forget()
            self.action_frame.pack(side="right")
            self.update_buttons()

    def _on_check(self):
        if self.on_select_change:
            self.on_select_change(self.app_id, self.var_select.get())

    def _on_uninstall(self):
        if self.on_uninstall_click:
            self.on_uninstall_click(self.app_id)

    def update_status(self, new_status):
        self.status = new_status
        self.update_badge()
        self.update_buttons()

from urllib.parse import urlparse

class AppDetailsPage(ctk.CTkFrame):
    def __init__(self, master, app_id, app_data, on_back, on_install):
        super().__init__(master, fg_color="transparent")
        self.app_id = app_id
        self.app_data = app_data
        self.on_back = on_back
        self.on_install = on_install
        
        # Üst Bar (Geri Butonu)
        self.top_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.top_bar.pack(fill="x", pady=(0, 20))
        
        btn_back = ctk.CTkButton(self.top_bar, text="← Geri", width=80, command=self.on_back, fg_color="transparent", border_width=1, text_color=("gray10", "gray90"))
        btn_back.pack(side="left")
        
        # İçerik
        self.content = ctk.CTkFrame(self, corner_radius=15)
        self.content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Sol Taraf: İkon ve İsim
        self.left_panel = ctk.CTkFrame(self.content, fg_color="transparent")
        self.left_panel.pack(side="left", fill="y", padx=40, pady=40)
        
        self.icon_label = ctk.CTkLabel(self.left_panel, text="📦", font=("Arial", 64), width=128, height=128)
        self.icon_label.pack(pady=(0, 20))
        
        if self.app_data:
            SmartIconLoader.load(self.app_data, self._set_icon)
            
        ctk.CTkLabel(self.left_panel, text=self.app_data["name"], font=("Roboto", 24, "bold")).pack()
        ctk.CTkLabel(self.left_panel, text=self.app_data["category"], font=("Roboto", 14), text_color="gray").pack(pady=5)
        
        # Sağ Taraf: Detaylar ve Aksiyonlar
        self.right_panel = ctk.CTkFrame(self.content, fg_color="transparent")
        self.right_panel.pack(side="left", fill="both", expand=True, padx=40, pady=40)
        
        # Açıklama
        ctk.CTkLabel(self.right_panel, text="Hakkında", font=("Roboto", 18, "bold"), anchor="w").pack(fill="x")
        ctk.CTkLabel(self.right_panel, text=self.app_data.get("description", "Açıklama yok."), wraplength=400, justify="left", anchor="w").pack(fill="x", pady=(5, 20))
        
        # --- Bilgi Kartları (Kaynak, Boyut, Web) ---
        self.info_frame = ctk.CTkFrame(self.right_panel, fg_color=("gray90", "#2B2B2B"), corner_radius=10)
        self.info_frame.pack(fill="x", pady=10)
        
        # Kaynak
        domain = urlparse(self.app_data["url"]).netloc
        self._add_info_row(self.info_frame, "Kaynak:", domain)
        
        # Boyut (Asenkron yüklenecek)
        self.lbl_size_val = self._add_info_row(self.info_frame, "Boyut:", "Hesaplanıyor...")
        self._fetch_size()

        # Web Sitesi
        website = self.app_data.get("website")
        if website:
             self._add_info_row(self.info_frame, "Web Sitesi:", website, is_link=True)

        # Sürüm Seçimi
        ctk.CTkLabel(self.right_panel, text="Sürüm Seçin", font=("Roboto", 18, "bold"), anchor="w").pack(fill="x", pady=(20, 5))
        
        self.versions = self.app_data.get("versions", {"Latest": self.app_data["url"]})
        self.ver_var = ctk.StringVar(value=list(self.versions.keys())[0])
        
        self.opt_version = ctk.CTkOptionMenu(self.right_panel, values=list(self.versions.keys()), variable=self.ver_var)
        self.opt_version.pack(anchor="w")
        
        # Yükle Butonu
        self.btn_install = ctk.CTkButton(self.right_panel, text="Yükle", font=("Roboto", 16, "bold"), height=40, width=200, command=self._on_install_click)
        self.btn_install.pack(anchor="w", pady=40)

    def _add_info_row(self, parent, label, value, is_link=False):
        row = ctk.CTkFrame(parent, fg_color="transparent", height=30)
        row.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(row, text=label, font=("Roboto", 12, "bold"), width=80, anchor="w").pack(side="left")
        
        if is_link:
            lbl_val = ctk.CTkButton(row, text=value, fg_color="transparent", text_color="#1f6aa5", hover=False, anchor="w", command=lambda: webbrowser.open(value))
            lbl_val.pack(side="left")
        else:
            lbl_val = ctk.CTkLabel(row, text=value, font=("Roboto", 12), anchor="w")
            lbl_val.pack(side="left")
            
        return lbl_val

    def _fetch_size(self):
        def _get():
            try:
                url = self.app_data["url"]
                response = requests.head(url, allow_redirects=True, timeout=5)
                size_bytes = int(response.headers.get('content-length', 0))
                if size_bytes > 0:
                    size_mb = size_bytes / (1024 * 1024)
                    self.after(0, lambda: self.lbl_size_val.configure(text=f"{size_mb:.1f} MB"))
                else:
                    self.after(0, lambda: self.lbl_size_val.configure(text="Bilinmiyor"))
            except:
                self.after(0, lambda: self.lbl_size_val.configure(text="Bilinmiyor"))
        
        threading.Thread(target=_get, daemon=True).start()

    def _set_icon(self, pil_image):
        img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(128, 128))
        self.icon_label.configure(image=img, text="")

    def _on_install_click(self):
        selected_ver = self.ver_var.get()
        url = self.versions[selected_ver]
        self.on_install(self.app_id, url)

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_nav_click):
        super().__init__(master, width=200, corner_radius=0)
        self.on_nav_click = on_nav_click
        
        self.lbl_title = ctk.CTkLabel(self, text="OmniInstaller", font=("Roboto", 20, "bold"))
        self.lbl_title.pack(pady=30, padx=20)

        self.add_btn("dashboard", Locale.get("dashboard"))
        self.add_btn("library", Locale.get("library"))
        self.add_btn("logs", Locale.get("logs"))
        self.add_btn("settings", Locale.get("settings"))
        
        ctk.CTkLabel(self, text="").pack(expand=True)
        
        self.lbl_version = ctk.CTkLabel(self, text="v0.5 | Sefflex", text_color="gray")
        self.lbl_version.pack(pady=20)

    def add_btn(self, key, text):
        btn = ctk.CTkButton(self, text=text, fg_color="transparent", anchor="w", height=40,
                            command=lambda k=key: self.on_nav_click(k))
        btn.pack(fill="x", padx=10, pady=5)
