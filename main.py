# main.py
import os
import customtkinter as ctk
import threading
import queue
from ui_components import AppCard, Sidebar
from apps_config import APPS, CAT_BROWSER, CAT_MEDIA, CAT_GAMING, CAT_TOOLS, CAT_DEV, CAT_OFFICE, CAT_SOCIAL, CAT_SECURITY, CAT_CLOUD, CAT_RUNTIMES
from localization import Locale
from persistence import MemoryBank
from installer import InstallerEngine

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class OmniInstallerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(Locale.get("app_title"))
        self.geometry("1280x850")
        
        # Veri ve Mantık
        self.db = MemoryBank()
        self.engine = InstallerEngine(log_callback=self.log_message, progress_callback=self.update_app_progress)
        self.selected_apps = set()
        self.log_queue = queue.Queue()
        self.progress_queue = queue.Queue()
        
        # UI Kurulumu
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, self.navigate)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Ana İçerik Alanı
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Sayfalar
        self.pages = {}
        self.cards = {} # app_id -> AppCard
        self.category_buttons = {} # cat_name -> Button
        self.current_category = "Tümü"
        
        self.create_dashboard()
        self.create_library_page()
        self.create_logs_page()
        self.create_settings_page()
        
        # İkon Yükleyiciyi Başlat (Queue Polling)
        from ui_components import start_image_dispatcher
        start_image_dispatcher(self)
        
        # Alt Kontrol Paneli
        self.create_control_panel()
        
        # İlk açılış
        self.show_page("dashboard")
        self.check_queues()
        
        # Otomatik Tarama Başlat
        self.start_auto_scan()

    def create_dashboard(self):
        self.pages["dashboard"] = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.pages["dashboard"].grid_columnconfigure(0, weight=1)
        self.pages["dashboard"].grid_rowconfigure(2, weight=1)

        # 1. Üst Panel (Header)
        self.header_frame = ctk.CTkFrame(self.pages["dashboard"], fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10), padx=10)
        
        # 1.1 Arama Alanı (Geniş ve Modern)
        self.search_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.search_frame.pack(fill="x", pady=(10, 10))
        
        self.search_var = ctk.StringVar()
        self.search_var.trace("w", self._on_search_change)
        
        # Arama İkonu (Label olarak)
        lbl_search_icon = ctk.CTkLabel(self.search_frame, text="🔍", font=("Arial", 16))
        lbl_search_icon.pack(side="left", padx=(10, 5))
        
        self.entry_search = ctk.CTkEntry(
            self.search_frame, 
            placeholder_text="Uygulama, kategori veya açıklama ara...", 
            height=40,
            font=("Roboto", 14),
            border_width=1,
            corner_radius=10,
            textvariable=self.search_var
        )
        self.entry_search.pack(side="left", fill="x", expand=True)

        # 1.2 Kategori Menüsü (Yatay Scroll)
        self.cat_menu = ctk.CTkScrollableFrame(self.header_frame, height=45, orientation="horizontal", fg_color="transparent")
        self.cat_menu.pack(fill="x", pady=(0, 5))
        
        categories = ["Tümü", CAT_BROWSER, CAT_GAMING, CAT_SOCIAL, CAT_DEV, CAT_TOOLS, CAT_MEDIA, CAT_OFFICE, CAT_SECURITY, CAT_CLOUD, CAT_RUNTIMES]
        
        for cat in categories:
            btn = ctk.CTkButton(
                self.cat_menu, 
                text=cat, 
                font=("Roboto", 13, "bold"),
                height=36,
                fg_color="transparent", 
                border_width=2,
                border_color="#3E3E3E",
                text_color=("gray10", "gray90"),
                hover_color=("#D0D0D0", "#2B2B2B"),
                corner_radius=18,
                command=lambda c=cat: self.filter_apps(c)
            )
            btn.pack(side="left", padx=5)
            self.category_buttons[cat] = btn
            
        self.highlight_category("Tümü")

        # 2. Alt Kısım: Uygulama Kartları
        self.apps_scroll = ctk.CTkScrollableFrame(self.pages["dashboard"], fg_color="transparent")
        self.apps_scroll.grid(row=2, column=0, sticky="nsew", padx=10)
        self.apps_scroll.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.refresh_app_grid()

    def _on_search_change(self, *args):
        self.refresh_app_grid()

    def refresh_app_grid(self):
        # Mevcut kartları gizle (ScrollableFrame'in iç yapısını bozmamak için winfo_children kullanmıyoruz)
        for card in self.cards.values():
            card.grid_forget()
            
        r, c = 0, 0
        sorted_apps = sorted(APPS.items(), key=lambda x: x[1]['name'])
        search_text = self.search_var.get().lower()
        
        for app_id, data in sorted_apps:
            # Kategori Filtresi
            if self.current_category != "Tümü" and data['category'] != self.current_category:
                continue
                
            # Arama Filtresi
            if search_text:
                in_name = search_text in data['name'].lower()
                in_desc = search_text in data.get('description', '').lower()
                in_kw = any(search_text in k.lower() for k in data.get('keywords', []))
                if not (in_name or in_desc or in_kw):
                    continue
                
            if app_id in self.cards:
                card = self.cards[app_id]
            else:
                status = self.db.get_app_status(app_id)
                card = AppCard(
                    self.apps_scroll, 
                    app_id, 
                    data, 
                    status, 
                    self.on_app_select, 
                    self.open_app_details, # Karta tıklanınca detay aç
                    self.on_uninstall_click
                )
                # Hızlı yükleme butonu için callback
                card.on_quick_install = lambda aid=app_id: self.install_specific_version(aid, data['url'])
                self.cards[app_id] = card
            
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
            
            c += 1
            if c > 2:
                c = 0
                r += 1

    def open_app_details(self, app_id):
        # Detay sayfasını oluştur ve göster
        from ui_components import AppDetailsPage
        
        # Varsa eskisini sil
        if "details" in self.pages:
            self.pages["details"].destroy()
            
        self.pages["details"] = AppDetailsPage(
            self.main_frame, 
            app_id, 
            APPS[app_id], 
            on_back=lambda: self.show_page("dashboard"),
            on_install=self.install_specific_version
        )
        self.show_page("details")

    def install_specific_version(self, app_id, url):
        # Özel sürüm kurulumu
        self.lbl_status.configure(text=f"{APPS[app_id]['name']} hazırlanıyor...")
        # InstallerEngine'e özel URL göndermek için thread başlat
        threading.Thread(target=self._run_custom_install, args=(app_id, url), daemon=True).start()

    def _run_custom_install(self, app_id, url):
        # Engine'e override_url parametresi eklememiz lazım veya geçici olarak config'i manipüle edebiliriz
        # En temizi engine'e parametre eklemek ama şimdilik basitçe:
        self.engine.install_app_process(app_id, override_url=url)
        self.log_queue.put(("DONE", [app_id]))

    def filter_apps(self, category):
        self.current_category = category
        self.highlight_category(category)
        self.refresh_app_grid()

    def highlight_category(self, category):
        for name, btn in self.category_buttons.items():
            if name == category:
                btn.configure(fg_color=("gray75", "gray25"), text_color=("white", "white"))
            else:
                btn.configure(fg_color="transparent", text_color=("gray10", "gray90"))

    def create_library_page(self):
        self.pages["library"] = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        
        lbl_title = ctk.CTkLabel(self.pages["library"], text="Bilgisayarınızdaki Tüm Uygulamalar", font=("Roboto", 20, "bold"))
        lbl_title.pack(pady=(0, 10), anchor="w")
        
        self.lib_scroll = ctk.CTkScrollableFrame(self.pages["library"], fg_color="transparent")
        self.lib_scroll.pack(fill="both", expand=True)
        
        # Yükle Butonu (Yenilemek için)
        btn_refresh = ctk.CTkButton(self.pages["library"], text="Listeyi Yenile", command=self.refresh_library)
        btn_refresh.pack(pady=10)
        
        # İlk açılışta boş olabilir, refresh ile dolar veya otomatik tetiklenir
        self.refresh_library()

    def refresh_library(self):
        for widget in self.lib_scroll.winfo_children():
            widget.destroy()
            
        apps = self.engine.get_all_system_apps()
        
        for app in apps:
            frm = ctk.CTkFrame(self.lib_scroll, height=50)
            frm.pack(fill="x", pady=2, padx=5)
            
            # Generic Icon (Basit bir kare)
            icon_lbl = ctk.CTkLabel(frm, text="📦", font=("Arial", 24), width=40)
            icon_lbl.pack(side="left", padx=10)
            
            name_lbl = ctk.CTkLabel(frm, text=app['name'], font=("Roboto", 14, "bold"))
            name_lbl.pack(side="left", padx=10)
            
            ver_lbl = ctk.CTkLabel(frm, text=f"v{app['version']}", text_color="gray")
            ver_lbl.pack(side="left", padx=10)
            
            # Kaldır butonu eklenebilir ama riskli, şimdilik sadece listeleme
            status_lbl = ctk.CTkLabel(frm, text="Yüklü", text_color="green")
            status_lbl.pack(side="right", padx=20)

    def create_logs_page(self):
        self.pages["logs"] = ctk.CTkFrame(self.main_frame)
        self.log_textbox = ctk.CTkTextbox(self.pages["logs"], width=800, height=500)
        self.log_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.log_message(Locale.get("ready"))

    def create_settings_page(self):
        self.pages["settings"] = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        
        # Başlık
        lbl_title = ctk.CTkLabel(self.pages["settings"], text="Ayarlar", font=("Roboto", 24, "bold"))
        lbl_title.pack(pady=(0, 20), anchor="w")
        
        # --- Görünüm Ayarları ---
        frm_appearance = ctk.CTkFrame(self.pages["settings"])
        frm_appearance.pack(fill="x", pady=10)
        
        ctk.CTkLabel(frm_appearance, text="Görünüm", font=("Roboto", 16, "bold")).pack(pady=10, padx=20, anchor="w")
        
        # Tema
        frm_theme = ctk.CTkFrame(frm_appearance, fg_color="transparent")
        frm_theme.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(frm_theme, text="Tema Modu:").pack(side="left")
        ctk.CTkOptionMenu(frm_theme, values=["Dark", "Light", "System"], command=ctk.set_appearance_mode).pack(side="right")
        
        # Renk
        frm_color = ctk.CTkFrame(frm_appearance, fg_color="transparent")
        frm_color.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(frm_color, text="Vurgu Rengi:").pack(side="left")
        ctk.CTkOptionMenu(frm_color, values=["blue", "green", "dark-blue"], command=ctk.set_default_color_theme).pack(side="right")

        # --- İndirme Ayarları ---
        frm_download = ctk.CTkFrame(self.pages["settings"])
        frm_download.pack(fill="x", pady=10)
        
        ctk.CTkLabel(frm_download, text="İndirme & Kurulum", font=("Roboto", 16, "bold")).pack(pady=10, padx=20, anchor="w")
        
        # İndirme Konumu
        frm_path = ctk.CTkFrame(frm_download, fg_color="transparent")
        frm_path.pack(fill="x", padx=20, pady=5)
        
        self.lbl_path = ctk.CTkLabel(frm_path, text=f"İndirme Klasörü: {os.path.expanduser('~/Downloads')}")
        self.lbl_path.pack(side="left")
        
        ctk.CTkButton(frm_path, text="Değiştir", width=80, command=self.change_download_path).pack(side="right")
        
        # Önbellek
        frm_cache = ctk.CTkFrame(frm_download, fg_color="transparent")
        frm_cache.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(frm_cache, text="Geçici Dosyalar:").pack(side="left")
        ctk.CTkButton(frm_cache, text="Önbelleği Temizle", fg_color="#D32F2F", hover_color="#B71C1C", command=self.clear_cache).pack(side="right")

        # --- Hakkında ---
        frm_about = ctk.CTkFrame(self.pages["settings"])
        frm_about.pack(fill="x", pady=20)
        
        ctk.CTkLabel(frm_about, text="Hakkında", font=("Roboto", 16, "bold")).pack(pady=10, padx=20, anchor="w")
        
        ctk.CTkLabel(frm_about, text="OmniInstaller v0.5", font=("Roboto", 14)).pack(pady=5)
        ctk.CTkLabel(frm_about, text="Geliştirici: Rahmi Çınar Sari (Sefflex)", font=("Roboto", 14, "bold"), text_color="#4CAF50").pack(pady=5)
        ctk.CTkLabel(frm_about, text="© 2023 Tüm Hakları Saklıdır.", font=("Roboto", 12), text_color="gray").pack(pady=(0, 10))

    def change_download_path(self):
        path = ctk.filedialog.askdirectory()
        if path:
            self.engine.download_dir = path
            self.lbl_path.configure(text=f"İndirme Klasörü: {path}")
            self.log_message(f"İndirme konumu değiştirildi: {path}")

    def clear_cache(self):
        # Basitçe temp klasörünü temizleme simülasyonu
        self.log_message("Önbellek temizlendi.")
        ctk.CTkLabel(self.pages["settings"], text="✅ Temizlendi!", text_color="green").pack()

    def create_control_panel(self):
        self.control_panel = ctk.CTkFrame(self, height=60, corner_radius=0)
        self.control_panel.grid(row=1, column=0, columnspan=2, sticky="ew")
        
        self.lbl_status = ctk.CTkLabel(self.control_panel, text=Locale.get("ready"))
        self.lbl_status.pack(side="left", padx=20, pady=10)
        
        self.btn_install_selected = ctk.CTkButton(
            self.control_panel, 
            text=Locale.get("install_selected").format(count=0),
            command=self.start_batch_install,
            state="disabled"
        )
        self.btn_install_selected.pack(side="right", padx=20, pady=10)

    def navigate(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        
        if page_name in self.pages:
            self.pages[page_name].pack(fill="both", expand=True)
        elif page_name == "library":
            self.navigate("dashboard")

    def show_page(self, page_name):
        self.navigate(page_name)

    def on_app_select(self, app_id, is_selected):
        if is_selected:
            self.selected_apps.add(app_id)
        else:
            self.selected_apps.discard(app_id)
        
        count = len(self.selected_apps)
        self.btn_install_selected.configure(
            text=Locale.get("install_selected").format(count=count),
            state="normal" if count > 0 else "disabled"
        )

    def on_single_install(self, app_id):
        self.start_install_process([app_id])

    def on_uninstall_click(self, app_id):
        self.engine.uninstall_app_process(app_id)
        self.refresh_ui_status([app_id])

    def start_batch_install(self):
        self.start_install_process(list(self.selected_apps))

    def start_install_process(self, app_ids):
        self.lbl_status.configure(text="İşlem Başlatılıyor...")
        threading.Thread(target=self._run_install_thread, args=(app_ids,), daemon=True).start()

    def start_auto_scan(self):
        self.lbl_status.configure(text="Sistem taranıyor...")
        threading.Thread(target=self._run_scan_thread, daemon=True).start()

    def _run_scan_thread(self):
        self.engine.check_installed_apps()
        self.log_queue.put(("DONE", list(APPS.keys())))

    def _run_install_thread(self, app_ids):
        self.engine.process_queue(app_ids)
        self.log_queue.put(("DONE", app_ids))

    def log_message(self, message):
        self.log_queue.put(("LOG", message))

    def update_app_progress(self, app_id, percent, speed):
        self.progress_queue.put((app_id, percent, speed))

    def check_queues(self):
        try:
            while True:
                msg_type, content = self.log_queue.get_nowait()
                if msg_type == "LOG":
                    self.log_textbox.insert("end", content + "\n")
                    self.log_textbox.see("end")
                    self.lbl_status.configure(text=content)
                elif msg_type == "DONE":
                    self.lbl_status.configure(text="Tamamlandı.")
                    self.refresh_ui_status(content)
        except queue.Empty:
            pass
            
        try:
            while True:
                app_id, percent, speed = self.progress_queue.get_nowait()
                if app_id in self.cards:
                    self.cards[app_id].set_progress(percent, speed)
        except queue.Empty:
            pass
        
        self.after(50, self.check_queues)

    def refresh_ui_status(self, app_ids):
        # Sadece görünür kartları değil, tüm kartları güncelle (eğer oluşturulduysa)
        # Ancak grid yenilendiğinde zaten status db'den çekiliyor.
        # Burada anlık güncelleme için:
        for app_id in app_ids:
            if app_id in self.cards:
                new_status = self.db.get_app_status(app_id)
                self.cards[app_id].update_status(new_status)
        
        self.selected_apps.clear()
        self.btn_install_selected.configure(text=Locale.get("install_selected").format(count=0), state="disabled")
        for card in self.cards.values():
            card.var_select.set(False)

if __name__ == "__main__":
    app = OmniInstallerApp()
    app.mainloop()
