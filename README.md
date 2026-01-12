# 🚀 OmniInstaller

**Windows için Akıllı Uygulama Yöneticisi ve Toplu Kurulum Aracı**

OmniInstaller, Windows PC'niz için tüm popüler uygulamaları tek bir yerden keşfetmenizi, yüklemenizi ve yönetmenizi sağlayan modern bir masaüstü uygulamasıdır. 100+ uygulama desteği, otomatik ikon bulucu, detaylı uygulama bilgileri ve kullanıcı dostu arayüzü ile kurulum sürecini çocuk oyuncağına çevirir.

---

## ✨ Özellikler

### 🎯 Temel Özellikler
- **100+ Popüler Uygulama:** Google Chrome, Discord, Spotify, VS Code, Steam, OBS Studio ve daha fazlası
- **Akıllı İkon Sistemi:** Walkx Dashboard Icons CDN + Google Favicon API ile otomatik yüksek kaliteli ikonlar
- **Kategorize Gezinti:** Browser, Gaming, Developer Tools, Media, Office, Security, Cloud, Runtimes
- **Güçlü Arama:** İsim, açıklama ve anahtar kelimelerle anlık filtreleme
- **Toplu Kurulum:** Birden fazla uygulamayı tek seferde seçip yükleyin

### 🔍 Gelişmiş Özellikler
- **Detaylı Uygulama Sayfaları:**
  - Kaynak bilgisi (hangi siteden indirildiği)
  - Dosya boyutu (dinamik hesaplama)
  - Resmi web sitesi linki
  - Sürüm seçimi (bazı uygulamalar için)
- **Otomatik Algılama:** Sistem taraması ile yüklü uygulamaları otomatik tespit
- **Kütüphane Görünümü:** PC'nizdeki tüm yüklü uygulamaları listeler
- **RAM-Only İkonlar:** Disk kirletmeden hafızada işleme
- **Modern Tasarım:** Dark/Light tema, glassmorphism efektler, hover animasyonları

### 🎨 Kullanıcı Arayüzü
- **Tıklanabilir Kartlar:** Detay sayfasına gitme
- **Hover Efektleri:** Canlı ve interaktif deneyim
- **Arama Çubuğu:** Alt alta kategorilerle modern layout
- **İlerleme Göstergeleri:** Anlık indirme hızı ve yüzde
- **Çoklu Dil Desteği:** Türkçe ve İngilizce

---

## 📸 Ekran Görüntüleri


![1764060609598](https://github.com/user-attachments/assets/42e10017-d7d2-4e25-9a07-c81aa488c75c) ![1764060609047](https://github.com/user-attachments/assets/009fc4cc-2df9-46a9-895c-8a1827f7cba8) ![1764060608421](https://github.com/user-attachments/assets/c8620aa5-6e6d-4f43-9c0d-6dcb8a803720) ![1764060608134](https://github.com/user-attachments/assets/0414b37b-b9c7-4e9b-a964-ba14c97f9f2f)

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3.10+**
- **CustomTkinter** - Modern UI framework
- **Pillow (PIL)** - Görüntü işleme
- **Requests** - HTTP istekleri
- **Threading & Queue** - Asenkron işlemler
- **WinReg** - Windows Registry erişimi
- **SQLite** - Yerel veritabanı

---

## 📦 Kurulum

### Gereksinimler
- Windows 10 veya üzeri
- Python 3.10+ (kaynak koddan çalıştırmak için)

### Yöntem 1: EXE Dosyasını Çalıştırma (Önerilen)
1. [Releases](https://github.com/yourusername/OmniInstaller/releases) sayfasından en son `OmniInstaller.exe` dosyasını indirin
2. İndirdiğiniz dosyayı çalıştırın
3. İşte bu kadar! 🎉

### Yöntem 2: Kaynak Koddan Çalıştırma
```bash
# Repoyu klonlayın
git clone https://github.com/sefflex/OmniInstaller.git
cd OmniInstaller

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python main.py
```

---

## 🚀 Kullanım

1. **Uygulamayı Başlatın:** `OmniInstaller.exe` veya `python main.py`
2. **Uygulama Keşfedin:** Kategorilerden birini seçin veya arama yapın
3. **Detayları İnceleyin:** Bir uygulamaya tıklayarak kaynak, boyut ve sürüm bilgilerini görün
4. **Kurulum Yapın:**
   - **Tek Uygulama:** Karta tıklayıp "Yükle" butonuna basın
   - **Toplu Kurulum:** Birden fazla uygulamayı seçip alt bardan "Seçilenleri Yükle"
5. **Yüklü Uygulamaları Görün:** "Kütüphanem" sekmesinden tüm yüklü programlarınızı listeleyin

---

## 🏗️ Proje Yapısı

```
OmniInstaller/
│
├── main.py                 # Ana uygulama döngüsü
├── ui_components.py        # UI bileşenleri (AppCard, Sidebar, DetailPage, SmartIconLoader)
├── installer.py            # Kurulum motoru (indirme, kurulum, algılama)
├── apps_config.py          # 100+ uygulama tanımları
├── localization.py         # Türkçe/İngilizce çeviriler
├── persistence.py          # SQLite veritabanı yönetimi
├── requirements.txt        # Python bağımlılıkları
└── README.md               # Bu dosya
```

---

## 🎯 Teknik Özellikler

### Akıllı İkon Yükleyici (SmartIconLoader)
- **ThreadPool (20 Worker):** Paralel indirme
- **Walkx CDN Entegrasyonu:** Yüksek kaliteli dashboard ikonları
- **Google Favicon Fallback:** CDN'de yoksa otomatik fallback
- **Harfli Placeholder:** Son çare olarak renkli kutu + baş harf
- **RAM-Only:** Zero disk I/O, BytesIO kullanımı

### Modern UI/UX
- **Tıklanabilir Kartlar:** Event binding ile etkileşimli
- **Hover Efektleri:** `_on_enter`, `_on_leave` metodları
- **Dinamik Filtreleme:** Kategori + arama birleşimi
- **Responsive Grid:** 3 sütun otomatik yerleşim

### Kurulum Motoru
- **Sessiz Kurulum:** `/S`, `/SILENT` gibi parametreler
- **UAC İstemi:** PowerShell ile yönetici izni
- **İlerleme Tracking:** Byte-by-byte indirme + hız hesaplama
- **Otomatik Algılama:** Registry tarama + dosya yolu kontrolü

---

## 🔧 EXE Oluşturma

PyInstaller kullanarak standalone .exe dosyası oluşturabilirsiniz:

```bash
# PyInstaller'ı yükleyin
pip install pyinstaller

# EXE oluşturun
pyinstaller --onefile --windowed --name OmniInstaller --icon=icon.ico main.py
```

---

## 🤝 Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

---

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 Geliştirici

**Rahmi Çınar Sari (Sefflex)**

- GitHub: [@seffelx](https://github.com/sefflex)
- Discord: w.xy

---

## 🙏 Teşekkürler

- [Walkxcode Dashboard Icons](https://github.com/walkxcode/dashboard-icons) - Yüksek kaliteli ikonlar
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI framework
- Tüm açık kaynak katkıcılarına ❤️

---

## ⚠️ Sorumluluk Reddi

Bu araç, yasal olarak dağıtılan yazılımların kurulumunu kolaylaştırmak için tasarlanmıştır. Tüm yazılım lisanslarına uymak kullanıcının sorumluluğundadır.

---

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!**




