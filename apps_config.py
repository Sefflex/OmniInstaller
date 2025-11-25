# apps_config.py
import os

# Kategori Tanımları
CAT_BROWSER = "Tarayıcılar"
CAT_SOCIAL = "Sosyal & İletişim"
CAT_GAMING = "Oyun & Başlatıcılar"
CAT_DEV = "Yazılım Geliştirme"
CAT_TOOLS = "Araçlar & Sistem"
CAT_MEDIA = "Medya & Tasarım"
CAT_OFFICE = "Ofis & Üretkenlik"
CAT_SECURITY = "Güvenlik & Ağ"
CAT_CLOUD = "Bulut & Depolama"
CAT_RUNTIMES = "Kütüphaneler"

# Uygulama Kataloğu
APPS = {
    # --- 1. WEB TARAYICILARI ---
    "chrome": {
        "name": "Google Chrome",
        "category": CAT_BROWSER,
        "url": "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B59616949-9C64-2826-6815-499317592415%7D%26lang%3Dtr%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe",
        "silent_args": ["/silent", "/install"],
        "description": "Standart web tarayıcısı.",
        "keywords": ["Google Chrome"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/888/888859.png",
        "check_paths": [r"C:\Program Files\Google\Chrome\Application\chrome.exe"]
    },
    "firefox": {
        "name": "Mozilla Firefox",
        "category": CAT_BROWSER,
        "url": "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=tr",
        "silent_args": ["-ms"],
        "description": "Gizlilik odaklı tarayıcı.",
        "keywords": ["Mozilla Firefox"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968827.png",
        "check_paths": [r"C:\Program Files\Mozilla Firefox\firefox.exe"]
    },
    "brave": {
        "name": "Brave Browser",
        "category": CAT_BROWSER,
        "url": "https://referrals.brave.com/latest/BraveBrowserSetup.exe",
        "silent_args": ["--silent", "--install"],
        "description": "Reklam engelleyici gömülü tarayıcı.",
        "keywords": ["Brave"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968658.png",
        "check_paths": [r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"]
    },
    "opera_gx": {
        "name": "Opera GX",
        "category": CAT_BROWSER,
        "url": "https://net.geo.opera.com/opera_gx/stable/windows?utm_tryagain=yes&utm_source=opera_com&utm_medium=ose&utm_campaign=(none)&http_referrer=https%3A%2F%2Fwww.opera.com%2Ftr%2Fgx&utm_site=opera_com&utm_lastpage=opera.com",
        "silent_args": ["/silent", "/launchopera=0"],
        "description": "Oyuncular için özel tarayıcı.",
        "keywords": ["Opera GX"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968930.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Programs\Opera GX\launcher.exe")]
    },
    "edge": {
        "name": "Microsoft Edge",
        "category": CAT_BROWSER,
        "url": "https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?ProductreleaseID=Edge&platform=X64&version=Edge&source=EdgeStablePage&Channel=Stable&language=tr",
        "silent_args": ["/quiet", "/norestart"],
        "description": "Microsoft'un modern tarayıcısı.",
        "keywords": ["Microsoft Edge"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968812.png",
        "check_paths": [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
    },
    "vivaldi": {
        "name": "Vivaldi",
        "category": CAT_BROWSER,
        "url": "https://downloads.vivaldi.com/stable/Vivaldi.6.5.3206.53.x64.exe",
        "silent_args": ["--vivaldi-silent", "--do-not-launch-chrome"],
        "description": "Özelleştirilebilir tarayıcı.",
        "keywords": ["Vivaldi"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2504/2504955.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Vivaldi\Application\vivaldi.exe")]
    },
    "tor": {
        "name": "Tor Browser",
        "category": CAT_BROWSER,
        "url": "https://www.torproject.org/dist/torbrowser/13.0.9/torbrowser-install-win64-13.0.9_ALL.exe",
        "silent_args": ["/S"],
        "description": "Anonim internet tarayıcısı.",
        "keywords": ["Tor Browser"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Tor-logo-2011-flat.svg/1024px-Tor-logo-2011-flat.svg.png",
        "check_paths": [os.path.expandvars(r"%USERPROFILE%\Desktop\Tor Browser\Browser\firefox.exe")]
    },

    # --- 2. İLETİŞİM & SOSYAL ---
    "discord": {
        "name": "Discord",
        "category": CAT_SOCIAL,
        "url": "https://discord.com/api/download?platform=win",
        "silent_args": ["--squirrel-install", "--squirrel-firstrun"],
        "description": "Topluluklar ve oyuncular için sohbet.",
        "keywords": ["Discord"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111370.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Discord\Update.exe")]
    },
    "whatsapp": {
        "name": "WhatsApp",
        "category": CAT_SOCIAL,
        "url": "https://web.whatsapp.com/desktop/windows/release/x64/WhatsAppSetup.exe",
        "silent_args": ["/silent"],
        "description": "Popüler mesajlaşma uygulaması.",
        "keywords": ["WhatsApp"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/733/733585.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\WhatsApp\WhatsApp.exe")]
    },
    "telegram": {
        "name": "Telegram",
        "category": CAT_SOCIAL,
        "url": "https://telegram.org/dl/desktop/win64",
        "silent_args": ["/VERYSILENT", "/NORESTART"],
        "description": "Hızlı ve güvenli mesajlaşma.",
        "keywords": ["Telegram Desktop"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111646.png",
        "check_paths": [os.path.expandvars(r"%APPDATA%\Telegram Desktop\Telegram.exe")]
    },
    "zoom": {
        "name": "Zoom",
        "category": CAT_SOCIAL,
        "url": "https://zoom.us/client/latest/ZoomInstaller.exe",
        "silent_args": ["/silent"],
        "description": "Video konferans ve toplantı.",
        "keywords": ["Zoom"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/4406/4406234.png",
        "check_paths": [os.path.expandvars(r"%APPDATA%\Zoom\bin\Zoom.exe")]
    },
    "teams": {
        "name": "Microsoft Teams",
        "category": CAT_SOCIAL,
        "url": "https://statics.teams.cdn.office.net/production-windows-x64/1.6.00.33567/Teams_windows_x64.exe",
        "silent_args": ["/s"],
        "description": "İş için iletişim platformu.",
        "keywords": ["Microsoft Teams"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/906/906349.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Teams\current\Teams.exe")]
    },
    "slack": {
        "name": "Slack",
        "category": CAT_SOCIAL,
        "url": "https://downloads.slack-edge.com/releases/windows/4.36.136/prod/x64/SlackSetup.exe",
        "silent_args": ["--silent"],
        "description": "İş ve yazılım ekipleri için sohbet.",
        "keywords": ["Slack"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111615.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\slack\slack.exe")]
    },
    "skype": {
        "name": "Skype",
        "category": CAT_SOCIAL,
        "url": "https://go.skype.com/windows.desktop.download",
        "silent_args": ["/VERYSILENT", "/NORESTART"],
        "description": "Görüntülü görüşme klasiği.",
        "keywords": ["Skype"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111609.png",
        "check_paths": [r"C:\Program Files (x86)\Microsoft\Skype for Desktop\Skype.exe"]
    },
    "signal": {
        "name": "Signal",
        "category": CAT_SOCIAL,
        "url": "https://updates.signal.org/desktop/signal-desktop-win-6.42.0.exe",
        "silent_args": ["/S"],
        "description": "Gizlilik odaklı mesajlaşma.",
        "keywords": ["Signal"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Signal-Logo.svg/1200px-Signal-Logo.svg.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Programs\Signal\Signal.exe")]
    },

    # --- 3. OYUN & BAŞLATICILAR ---
    "steam": {
        "name": "Steam",
        "category": CAT_GAMING,
        "url": "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe",
        "silent_args": ["/S"],
        "description": "Dünyanın en büyük oyun platformu.",
        "keywords": ["Steam"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/220/220223.png",
        "check_paths": [r"C:\Program Files (x86)\Steam\steam.exe"]
    },
    "epic": {
        "name": "Epic Games",
        "category": CAT_GAMING,
        "url": "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi",
        "silent_args": ["/quiet", "/norestart"],
        "description": "Epic Games mağazası.",
        "keywords": ["Epic Games Launcher"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/588/588346.png",
        "check_paths": [r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"]
    },
    "battlenet": {
        "name": "Battle.net",
        "category": CAT_GAMING,
        "url": "https://www.battle.net/download/getInstallerForGame?os=win&locale=enUS&version=LIVE&gameProgram=BATTLENET_APP",
        "silent_args": ["--lang=enUS"],
        "description": "Blizzard oyunları başlatıcısı.",
        "keywords": ["Battle.net"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Battle.net_Icon.svg/1200px-Battle.net_Icon.svg.png",
        "check_paths": [r"C:\Program Files (x86)\Battle.net\Battle.net.exe"]
    },
    "eaapp": {
        "name": "EA App",
        "category": CAT_GAMING,
        "url": "https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe",
        "silent_args": ["/quiet"],
        "description": "EA oyunları için yeni başlatıcı.",
        "keywords": ["EA App"],
        "icon_url": "https://media.game.es/COVERV2/3D_L/544/544172.png",
        "check_paths": [r"C:\Program Files\Electronic Arts\EA Desktop\EA Desktop\EADesktop.exe"]
    },
    "ubisoft": {
        "name": "Ubisoft Connect",
        "category": CAT_GAMING,
        "url": "https://ubi.li/4vxt9",
        "silent_args": ["/S"],
        "description": "Ubisoft oyunları başlatıcısı.",
        "keywords": ["Ubisoft Connect"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5969/5969040.png",
        "check_paths": [r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\UbisoftConnect.exe"]
    },
    "gog": {
        "name": "GOG Galaxy",
        "category": CAT_GAMING,
        "url": "https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe",
        "silent_args": ["/SILENT"],
        "description": "DRM'siz oyun platformu.",
        "keywords": ["GOG Galaxy"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968822.png",
        "check_paths": [r"C:\Program Files (x86)\GOG Galaxy\GalaxyClient.exe"]
    },
    "riot": {
        "name": "Riot Client",
        "category": CAT_GAMING,
        "url": "https://riotgamespatcher-cos.ranker.com/RiotClientInstalls/RiotClientInstaller.exe", # Resmi Link Değil, Riot Installers dinamik
        "silent_args": [], # Riot sessiz kurulumu zor
        "description": "LoL ve Valorant istemcisi.",
        "keywords": ["Riot Client"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5969/5969240.png", # Generic Game
        "check_paths": [r"C:\Riot Games\Riot Client\RiotClientServices.exe"]
    },
    "roblox": {
        "name": "Roblox",
        "category": CAT_GAMING,
        "url": "https://setup.rbxcdn.com/RobloxPlayerInstaller.exe",
        "silent_args": [],
        "description": "Oyun oluşturma platformu.",
        "keywords": ["Roblox"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968902.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Roblox\Versions\RobloxPlayerLauncher.exe")]
    },
    "minecraft": {
        "name": "Minecraft Launcher",
        "category": CAT_GAMING,
        "url": "https://launcher.mojang.com/download/MinecraftInstaller.msi",
        "silent_args": ["/quiet"],
        "description": "Minecraft başlatıcısı.",
        "keywords": ["Minecraft Launcher"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968853.png",
        "check_paths": [r"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe"]
    },
    "razer": {
        "name": "Razer Synapse 3",
        "category": CAT_GAMING,
        "url": "https://rzr.to/synapse-3-pc-download",
        "silent_args": ["/S"],
        "description": "Razer ekipman kontrolü.",
        "keywords": ["Razer Synapse"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/en/thumb/4/40/Razer_Snake_Logo.svg/1200px-Razer_Snake_Logo.svg.png", # Wikipedia bazen 403 verir, alternatif:
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5969/5969240.png", # Generic Game (Razer logosu zor bulunuyor)
        "check_paths": [r"C:\Program Files (x86)\Razer\Synapse3\WPF\Razer Synapse 3.exe"]
    },
    "cpuz": {
        "name": "CPU-Z",
        "category": CAT_TOOLS,
        "url": "https://download.cpuid.com/cpu-z/cpu-z_2.08-en.exe",
        "silent_args": ["/SILENT"],
        "description": "Donanım bilgisi.",
        "keywords": ["CPU-Z"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/906/906324.png", # Chip icon
        "check_paths": [r"C:\Program Files\CPUID\CPU-Z\cpuz.exe"]
    },
    "wireshark": {
        "name": "Wireshark",
        "category": CAT_SECURITY,
        "url": "https://2.na.dl.wireshark.org/win64/Wireshark-win64-4.2.0.exe",
        "silent_args": ["/S"],
        "description": "Ağ analizi.",
        "keywords": ["Wireshark"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2082/2082852.png", # Network icon
        "check_paths": [r"C:\Program Files\Wireshark\Wireshark.exe"]
    },
    "vlc": {
        "name": "VLC Media Player",
        "category": CAT_MEDIA,
        "url": "https://get.videolan.org/vlc/last/win64/vlc-3.0.20-win64.exe", # 'last' dizini
        "silent_args": ["/S"],
        "description": "Her şeyi oynatan oynatıcı.",
        "keywords": ["VLC media player"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/9509/9509923.png",
        "check_paths": [r"C:\Program Files\VideoLAN\VLC\vlc.exe"]
    },
    "audacity": {
        "name": "Audacity",
        "category": CAT_MEDIA,
        "url": "https://github.com/audacity/audacity/releases/latest/download/audacity-win-x64.exe", # Github latest redirect
        "silent_args": ["/VERYSILENT"],
        "description": "Ses düzenleyici.",
        "keywords": ["Audacity"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968846.png",
        "check_paths": [r"C:\Program Files\Audacity\Audacity.exe"]
    },

    # --- 4. YAZILIM GELİŞTİRME ---
    "vscode": {
        "name": "VS Code",
        "category": CAT_DEV,
        "url": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user",
        "silent_args": ["/VERYSILENT", "/MERGETASKS=!runcode"],
        "description": "En popüler kod editörü.",
        "keywords": ["Microsoft Visual Studio Code", "VS Code"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/906/906324.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe")]
    },
    "python": {
        "name": "Python",
        "category": CAT_DEV,
        "website": "https://www.python.org/",
        "versions": {
            "3.12.1 (Latest)": "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe",
            "3.11.7": "https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe",
            "3.10.11": "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
        },
        "url": "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe", # Varsayılan
        "silent_args": ["/quiet", "InstallAllUsers=1", "PrependPath=1"],
        "description": "Python programlama dili.",
        "keywords": ["Python 3.12", "Python 3.11", "Python 3.10"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968350.png",
        "check_paths": [r"C:\Python312\python.exe"]
    },
    "nodejs": {
        "name": "Node.js",
        "category": CAT_DEV,
        "website": "https://nodejs.org/",
        "versions": {
            "20.10.0 (LTS)": "https://nodejs.org/dist/v20.10.0/node-v20.10.0-x64.msi",
            "21.5.0 (Current)": "https://nodejs.org/dist/v21.5.0/node-v21.5.0-x64.msi",
            "18.19.0": "https://nodejs.org/dist/v18.19.0/node-v18.19.0-x64.msi"
        },
        "url": "https://nodejs.org/dist/v20.10.0/node-v20.10.0-x64.msi",
        "silent_args": ["/quiet"],
        "description": "JavaScript çalışma zamanı.",
        "keywords": ["Node.js"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/919/919825.png",
        "check_paths": [r"C:\Program Files\nodejs\node.exe"]
    },
    "git": {
        "name": "Git",
        "category": CAT_DEV,
        "url": "https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe",
        "silent_args": ["/VERYSILENT", "/NORESTART"],
        "description": "Versiyon kontrol sistemi.",
        "keywords": ["Git"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/11518/11518876.png",
        "check_paths": [r"C:\Program Files\Git\bin\git.exe"]
    },
    "docker": {
        "name": "Docker Desktop",
        "category": CAT_DEV,
        "url": "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe",
        "silent_args": ["install", "--quiet"],
        "description": "Konteyner platformu.",
        "keywords": ["Docker Desktop"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/919/919853.png",
        "check_paths": [r"C:\Program Files\Docker\Docker\Docker Desktop.exe"]
    },
    "notepadpp": {
        "name": "Notepad++",
        "category": CAT_DEV,
        "url": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6/npp.8.6.Installer.x64.exe",
        "silent_args": ["/S"],
        "description": "Hafif metin editörü.",
        "keywords": ["Notepad++"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/6124/6124995.png",
        "check_paths": [r"C:\Program Files\Notepad++\notepad++.exe"]
    },
    "pycharm": {
        "name": "PyCharm Community",
        "category": CAT_DEV,
        "url": "https://download.jetbrains.com/python/pycharm-community-2023.3.2.exe",
        "silent_args": ["/S"],
        "description": "Python IDE.",
        "keywords": ["PyCharm Community"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png",
        "check_paths": [r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.2\bin\pycharm64.exe"]
    },
    "intellij": {
        "name": "IntelliJ IDEA",
        "category": CAT_DEV,
        "url": "https://download.jetbrains.com/idea/ideaIC-2023.3.2.exe",
        "silent_args": ["/S"],
        "description": "Java IDE.",
        "keywords": ["IntelliJ IDEA Community"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IntelliJ_IDEA_Icon.svg/1024px-IntelliJ_IDEA_Icon.svg.png",
        "check_paths": [r"C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2023.3.2\bin\idea64.exe"]
    },
    "sublime": {
        "name": "Sublime Text 4",
        "category": CAT_DEV,
        "url": "https://download.sublimetext.com/sublime_text_build_4169_x64_setup.exe",
        "silent_args": ["/VERYSILENT"],
        "description": "Hızlı kod editörü.",
        "keywords": ["Sublime Text"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Sublime_Text_Logo.svg/1200px-Sublime_Text_Logo.svg.png",
        "check_paths": [r"C:\Program Files\Sublime Text\sublime_text.exe"]
    },
    "postman": {
        "name": "Postman",
        "category": CAT_DEV,
        "url": "https://dl.pstmn.io/download/latest/win64",
        "silent_args": ["/silent"],
        "description": "API test aracı.",
        "keywords": ["Postman"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968866.png", # Generic API
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Postman\Postman.exe")]
    },
    "filezilla": {
        "name": "FileZilla",
        "category": CAT_DEV,
        "url": "https://download.filezilla-project.org/client/FileZilla_3.66.4_win64_setup.exe",
        "silent_args": ["/S"],
        "description": "FTP İstemcisi.",
        "keywords": ["FileZilla"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968875.png",
        "check_paths": [r"C:\Program Files\FileZilla FTP Client\filezilla.exe"]
    },
    "anaconda": {
        "name": "Anaconda",
        "category": CAT_DEV,
        "url": "https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Windows-x86_64.exe",
        "silent_args": ["/S", r"/D=%UserProfile%\Anaconda3"],
        "description": "Veri bilimi platformu.",
        "keywords": ["Anaconda3"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png",
        "check_paths": [os.path.expandvars(r"%USERPROFILE%\Anaconda3\python.exe")]
    },

    # --- 5. ARAÇLAR & SİSTEM ---
    "winrar": {
        "name": "WinRAR",
        "category": CAT_TOOLS,
        "url": "https://www.rarlab.com/rar/winrar-x64-624.exe",
        "silent_args": ["/S"],
        "description": "Klasik arşiv yöneticisi.",
        "keywords": ["WinRAR"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968943.png",
        "check_paths": [r"C:\Program Files\WinRAR\WinRAR.exe"]
    },
    "7zip": {
        "name": "7-Zip",
        "category": CAT_TOOLS,
        "url": "https://www.7-zip.org/a/7z2301-x64.exe",
        "silent_args": ["/S"],
        "description": "Açık kaynak arşivleyici.",
        "keywords": ["7-Zip"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/7/76/7-Zip_32-pixel_icon.png",
        "check_paths": [r"C:\Program Files\7-Zip\7zFM.exe"]
    },
    "powertoys": {
        "name": "PowerToys",
        "category": CAT_TOOLS,
        "url": "https://github.com/microsoft/PowerToys/releases/download/v0.76.2/PowerToysUserSetup-0.76.2-x64.exe",
        "silent_args": ["/install", "/quiet", "/norestart"],
        "description": "Windows geliştirme araçları.",
        "keywords": ["PowerToys"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/888/888870.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\PowerToys\PowerToys.exe")]
    },
    "rufus": {
        "name": "Rufus",
        "category": CAT_TOOLS,
        "url": "https://github.com/pbatard/rufus/releases/download/v4.3/rufus-4.3.exe",
        "silent_args": [],
        "description": "Format USB'si hazırlama.",
        "keywords": ["Rufus"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2306/2306085.png",
        "check_paths": []
    },

    "anydesk": {
        "name": "AnyDesk",
        "category": CAT_TOOLS,
        "url": "https://download.anydesk.com/AnyDesk.exe",
        "silent_args": ["--install", "C:\\Program Files (x86)\\AnyDesk", "--silent"],
        "description": "Uzak masaüstü.",
        "keywords": ["AnyDesk"],
        "icon_url": "https://cdn.icon-icons.com/icons2/2699/PNG/512/anydesk_logo_icon_170295.png",
        "check_paths": [r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"]
    },
    "teamviewer": {
        "name": "TeamViewer",
        "category": CAT_TOOLS,
        "url": "https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe",
        "silent_args": ["/S"],
        "description": "Uzak destek.",
        "keywords": ["TeamViewer"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968936.png",
        "check_paths": [r"C:\Program Files\TeamViewer\TeamViewer.exe"]
    },
    "revouninstaller": {
        "name": "Revo Uninstaller",
        "category": CAT_TOOLS,
        "url": "https://www.revouninstaller.com/download-freeware-version.php", # Redirect olabilir
        "silent_args": ["/VERYSILENT"],
        "description": "Kalıntısız silme aracı.",
        "keywords": ["Revo Uninstaller"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968850.png", # Generic trash
        "check_paths": [r"C:\Program Files\VS Revo Group\Revo Uninstaller\RevoUnin.exe"]
    },
    "everything": {
        "name": "Everything",
        "category": CAT_TOOLS,
        "url": "https://www.voidtools.com/Everything-1.4.1.1024.x64-Setup.exe",
        "silent_args": ["/S"],
        "description": "Hızlı dosya arama.",
        "keywords": ["Everything"],
        "icon_url": "https://www.voidtools.com/Everything.png",
        "check_paths": [r"C:\Program Files\Everything\Everything.exe"]
    },
    "bleachbit": {
        "name": "BleachBit",
        "category": CAT_TOOLS,
        "url": "https://download.bleachbit.org/BleachBit-4.6.0-setup.exe",
        "silent_args": ["/S"],
        "description": "Sistem temizleyici.",
        "keywords": ["BleachBit"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/BleachBit_icon.svg/1024px-BleachBit_icon.svg.png",
        "check_paths": [r"C:\Program Files (x86)\BleachBit\bleachbit.exe"]
    },
    "putty": {
        "name": "PuTTY",
        "category": CAT_TOOLS,
        "url": "https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.80-installer.msi",
        "silent_args": ["/quiet"],
        "description": "SSH istemcisi.",
        "keywords": ["PuTTY"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/PuTTY_icon.svg/1200px-PuTTY_icon.svg.png",
        "check_paths": [r"C:\Program Files\PuTTY\putty.exe"]
    },
    "winscp": {
        "name": "WinSCP",
        "category": CAT_TOOLS,
        "url": "https://winscp.net/download/WinSCP-6.1.2-Setup.exe",
        "silent_args": ["/VERYSILENT"],
        "description": "SFTP/FTP istemcisi.",
        "keywords": ["WinSCP"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/WinSCP_Logo.svg/1024px-WinSCP_Logo.svg.png",
        "check_paths": [r"C:\Program Files (x86)\WinSCP\WinSCP.exe"]
    },

    # --- 6. MEDYA & TASARIM ---

    "obs": {
        "name": "OBS Studio",
        "category": CAT_MEDIA,
        "url": "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-30.0.2-Full-Installer-x64.exe",
        "silent_args": ["/S"],
        "description": "Yayın ve kayıt aracı.",
        "keywords": ["OBS Studio"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/8152/8152542.png",
        "check_paths": [r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"]
    },
    "gimp": {
        "name": "GIMP",
        "category": CAT_MEDIA,
        "url": "https://download.gimp.org/gimp/v2.10/windows/gimp-2.10.36-setup.exe",
        "silent_args": ["/VERYSILENT", "/NORESTART"],
        "description": "Ücretsiz resim düzenleyici.",
        "keywords": ["GIMP"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/The_GIMP_icon_-_gnome.svg/1024px-The_GIMP_icon_-_gnome.svg.png",
        "check_paths": [r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe"]
    },
    "blender": {
        "name": "Blender",
        "category": CAT_MEDIA,
        "url": "https://download.blender.org/release/Blender4.0/blender-4.0.2-windows-x64.msi",
        "silent_args": ["/quiet"],
        "description": "3D Modelleme.",
        "keywords": ["Blender"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Blender_logo_no_text.svg/1024px-Blender_logo_no_text.svg.png",
        "check_paths": [r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe"]
    },

    "handbrake": {
        "name": "HandBrake",
        "category": CAT_MEDIA,
        "url": "https://github.com/HandBrake/HandBrake/releases/download/1.7.2/HandBrake-1.7.2-x86_64-Win_GUI.exe",
        "silent_args": ["/S"],
        "description": "Video dönüştürücü.",
        "keywords": ["HandBrake"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/HandBrake_Icon.png/120px-HandBrake_Icon.png",
        "check_paths": [r"C:\Program Files\HandBrake\HandBrake.exe"]
    },
    "paintnet": {
        "name": "Paint.NET",
        "category": CAT_MEDIA,
        "url": "https://github.com/paintdotnet/release/releases/download/v5.0.11/paint.net.5.0.11.install.x64.zip", # ZIP sorunu
        "silent_args": [],
        "description": "Resim düzenleme (ZIP).",
        "keywords": ["Paint.NET"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Paint.net_Icon.png/120px-Paint.net_Icon.png",
        "check_paths": [r"C:\Program Files\paint.net\paintdotnet.exe"]
    },
    "krita": {
        "name": "Krita",
        "category": CAT_MEDIA,
        "url": "https://download.kde.org/stable/krita/5.2.2/krita-x64-5.2.2-setup.exe",
        "silent_args": ["/S"],
        "description": "Dijital çizim.",
        "keywords": ["Krita"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Krita-icon-2021.svg/1024px-Krita-icon-2021.svg.png",
        "check_paths": [r"C:\Program Files\Krita (x64)\bin\krita.exe"]
    },
    "inkscape": {
        "name": "Inkscape",
        "category": CAT_MEDIA,
        "url": "https://media.inkscape.org/dl/resources/file/inkscape-1.3.2_2023-11-25_091e20e-x64.msi",
        "silent_args": ["/quiet"],
        "description": "Vektörel çizim.",
        "keywords": ["Inkscape"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Inkscape_Logo.svg/1024px-Inkscape_Logo.svg.png",
        "check_paths": [r"C:\Program Files\Inkscape\bin\inkscape.exe"]
    },
    "sharex": {
        "name": "ShareX",
        "category": CAT_MEDIA,
        "url": "https://github.com/ShareX/ShareX/releases/download/v15.0.0/ShareX-15.0.0-setup.exe",
        "silent_args": ["/VERYSILENT", "/NORESTART"],
        "description": "Ekran görüntüsü aracı.",
        "keywords": ["ShareX"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/ShareX_Logo.svg/1024px-ShareX_Logo.svg.png",
        "check_paths": [r"C:\Program Files\ShareX\ShareX.exe"]
    },
    "lightshot": {
        "name": "Lightshot",
        "category": CAT_MEDIA,
        "url": "https://app.prntscr.com/build/setup-lightshot.exe",
        "silent_args": ["/VERYSILENT"],
        "description": "Hızlı ekran görüntüsü.",
        "keywords": ["Lightshot"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Lightshot_icon.svg/1024px-Lightshot_icon.svg.png",
        "check_paths": [r"C:\Program Files (x86)\Skillbrains\lightshot\Lightshot.exe"]
    },
    "spotify": {
        "name": "Spotify",
        "category": CAT_MEDIA,
        "url": "https://download.scdn.co/SpotifySetup.exe",
        "silent_args": ["/S"],
        "description": "Müzik dinleme.",
        "keywords": ["Spotify"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111624.png",
        "check_paths": [os.path.expandvars(r"%APPDATA%\Spotify\Spotify.exe")]
    },

    # --- 7. OFİS & ÜRETKENLİK ---
    "libreoffice": {
        "name": "LibreOffice",
        "category": CAT_OFFICE,
        "url": "https://download.documentfoundation.org/libreoffice/stable/7.6.4/win-x86_64/LibreOffice_7.6.4_Win_x86-64.msi",
        "silent_args": ["/quiet", "/norestart"],
        "description": "Ücretsiz ofis paketi.",
        "keywords": ["LibreOffice"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/732/732220.png",
        "check_paths": [r"C:\Program Files\LibreOffice\program\soffice.exe"]
    },
    "acrobat": {
        "name": "Adobe Reader",
        "category": CAT_OFFICE,
        "url": "https://ardownload2.adobe.com/pub/adobe/reader/win/AcrobatDC/2300820421/AcroRdrDC2300820421_en_US.exe",
        "silent_args": ["/sAll", "/rs", "/msi", "EULA_ACCEPT=YES"],
        "description": "PDF görüntüleyici.",
        "keywords": ["Adobe Acrobat Reader"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/4202/4202070.png",
        "check_paths": [r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"]
    },
    "notion": {
        "name": "Notion",
        "category": CAT_OFFICE,
        "url": "https://desktop-release.notion-static.com/Notion%20Setup%202.0.49.exe",
        "silent_args": ["/S"],
        "description": "Not ve planlama.",
        "keywords": ["Notion"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Programs\Notion\Notion.exe")]
    },
    "evernote": {
        "name": "Evernote",
        "category": CAT_OFFICE,
        "url": "https://cdn1.evernote.com/win6/public/Evernote-10.68.2-win-ddl-ga-4175-setup.exe",
        "silent_args": ["/S"],
        "description": "Not alma uygulaması.",
        "keywords": ["Evernote"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111394.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Programs\Evernote\Evernote.exe")]
    },
    "obsidian": {
        "name": "Obsidian",
        "category": CAT_OFFICE,
        "url": "https://github.com/obsidianmd/obsidian-releases/releases/download/v1.4.16/Obsidian.1.4.16.exe",
        "silent_args": ["/S"],
        "description": "Kişisel bilgi tabanı.",
        "keywords": ["Obsidian"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/1/10/2023_Obsidian_logo.png",
        "check_paths": [os.path.expandvars(r"%LOCALAPPDATA%\Obsidian\Obsidian.exe")]
    },
    "thunderbird": {
        "name": "Thunderbird",
        "category": CAT_OFFICE,
        "url": "https://download.mozilla.org/?product=thunderbird-115.6.0-SSL&os=win64&lang=tr",
        "silent_args": ["-ms"],
        "description": "Mail istemcisi.",
        "keywords": ["Mozilla Thunderbird"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/732/732228.png",
        "check_paths": [r"C:\Program Files\Mozilla Thunderbird\thunderbird.exe"]
    },

    # --- 8. GÜVENLİK & AĞ ---
    "malwarebytes": {
        "name": "Malwarebytes",
        "category": CAT_SECURITY,
        "url": "https://downloads.malwarebytes.com/file/mb4_offline",
        "silent_args": ["/VERYSILENT"],
        "description": "Virüs tarama.",
        "keywords": ["Malwarebytes"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/906/906336.png",
        "check_paths": [r"C:\Program Files\Malwarebytes\Anti-Malware\mbam.exe"]
    },
    "bitwarden": {
        "name": "Bitwarden",
        "category": CAT_SECURITY,
        "url": "https://github.com/bitwarden/clients/releases/download/desktop-v2023.12.0/Bitwarden-Installer-2023.12.0.exe",
        "silent_args": ["/S"],
        "description": "Şifre yöneticisi.",
        "keywords": ["Bitwarden"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Bitwarden_logo_vertical.svg/1024px-Bitwarden_logo_vertical.svg.png",
        "check_paths": [r"C:\Program Files\Bitwarden\Bitwarden.exe"]
    },


    # --- 9. BULUT & DEPOLAMA ---
    "googledrive": {
        "name": "Google Drive",
        "category": CAT_CLOUD,
        "url": "https://dl.google.com/drive-file-stream/GoogleDriveSetup.exe",
        "silent_args": ["--silent", "--desktop_shortcut"],
        "description": "Google bulut.",
        "keywords": ["Google Drive"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968523.png",
        "check_paths": [r"C:\Program Files\Google\Drive File Stream\launch_bat.exe"]
    },
    "dropbox": {
        "name": "Dropbox",
        "category": CAT_CLOUD,
        "url": "https://www.dropbox.com/download?plat=win&full=1",
        "silent_args": ["/S"],
        "description": "Bulut depolama.",
        "keywords": ["Dropbox"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/2111/2111363.png",
        "check_paths": [r"C:\Program Files (x86)\Dropbox\Client\Dropbox.exe"]
    },
    "qbittorrent": {
        "name": "qBittorrent",
        "category": CAT_CLOUD,
        "url": "https://downloads.sourceforge.net/project/qbittorrent/qbittorrent-win32/qbittorrent-4.6.2/qbittorrent_4.6.2_x64_setup.exe",
        "silent_args": ["/S"],
        "description": "Torrent istemcisi.",
        "keywords": ["qBittorrent"],
        "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/New_qBittorrent_Logo.svg/1200px-New_qBittorrent_Logo.svg.png",
        "check_paths": [r"C:\Program Files\qBittorrent\qbittorrent.exe"]
    },

    # --- 10. KÜTÜPHANELER (RUNTIMES) ---
    "java_jdk": {
        "name": "Java JDK 21",
        "category": CAT_RUNTIMES,
        "url": "https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.exe",
        "silent_args": ["/s"],
        "description": "Java Geliştirme Kiti.",
        "keywords": ["Java(TM) SE Development Kit"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/226/226777.png",
        "check_paths": [r"C:\Program Files\Java\jdk-21\bin\java.exe"]
    },
    "vc_redist": {
        "name": "Visual C++ AIO",
        "category": CAT_RUNTIMES,
        "url": "https://aka.ms/vs/17/release/vc_redist.x64.exe",
        "silent_args": ["/install", "/quiet", "/norestart"],
        "description": "C++ kütüphaneleri.",
        "keywords": ["Microsoft Visual C++"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968812.png",
        "check_paths": []
    },
    "directx": {
        "name": "DirectX Runtime",
        "category": CAT_RUNTIMES,
        "url": "https://download.microsoft.com/download/1/7/1/1718CCC4-6315-4D8E-9543-8E28A4E18C4C/dxwebsetup.exe",
        "silent_args": ["/Q"],
        "description": "Oyunlar için DirectX.",
        "keywords": ["DirectX"],
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968812.png",
        "check_paths": []
    }
}
