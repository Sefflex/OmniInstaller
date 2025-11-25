# localization.py

LANGUAGES = {
    "TR": {
        "app_title": "OmniInstaller - Yazılım Yöneticisi",
        "dashboard": "İndirici",
        "library": "Kütüphanem",
        "settings": "Ayarlar",
        "logs": "Kayıtlar",
        "install_selected": "Seçilenleri Yükle ({count})",
        "status_installed": "Yüklü",
        "status_not_installed": "Yüklü Değil",
        "status_update": "Güncelleme Var",
        "btn_install": "Yükle",
        "btn_update": "Güncelle",
        "btn_reinstall": "Onar",
        "msg_installing": "Yükleniyor: {app}",
        "msg_success": "{app} başarıyla yüklendi.",
        "msg_error": "{app} yüklenirken hata oluştu!",
        "settings_lang": "Dil / Language",
        "settings_theme": "Tema",
        "theme_dark": "Koyu",
        "theme_light": "Açık",
        "welcome": "OmniInstaller'a Hoşgeldiniz",
        "ready": "Hazır"
    },
    "EN": {
        "app_title": "OmniInstaller - Software Manager",
        "dashboard": "Dashboard",
        "library": "My Library",
        "settings": "Settings",
        "logs": "Logs",
        "install_selected": "Install Selected ({count})",
        "status_installed": "Installed",
        "status_not_installed": "Not Installed",
        "status_update": "Update Available",
        "btn_install": "Install",
        "btn_update": "Update",
        "btn_reinstall": "Re-install",
        "msg_installing": "Installing: {app}",
        "msg_success": "{app} installed successfully.",
        "msg_error": "Error installing {app}!",
        "settings_lang": "Language / Dil",
        "settings_theme": "Theme",
        "theme_dark": "Dark",
        "theme_light": "Light",
        "welcome": "Welcome to OmniInstaller",
        "ready": "Ready"
    }
}

class Locale:
    _current_lang = "TR"

    @classmethod
    def set_lang(cls, lang_code):
        if lang_code in LANGUAGES:
            cls._current_lang = lang_code

    @classmethod
    def get(cls, key):
        return LANGUAGES[cls._current_lang].get(key, key)
