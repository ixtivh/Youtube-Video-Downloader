# ixtivh YouTube Video Downloader

Bu program, verilen bir YouTube linkinden videoyu veya sesi en yüksek çözünürlükte indirmenizi sağlar. Grafik arayüz (GUI) ile kolay kullanım sunar.

---

## Kurulum ve Kullanım (Windows için)

### 1. Python Kurulumu
- [Python 3.8 veya üzeri](https://www.python.org/downloads/) yüklü olmalıdır.
- Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın.

### 2. Gerekli Kütüphaneleri Yükleyin
Aşağıdaki komutu çalıştırın:
```bash
pip install -r requirements.txt
```

### 3. FFmpeg Kurulumu
Program, video/ses işlemleri için FFmpeg'e ihtiyaç duyar. Eğer bilgisayarınızda FFmpeg yoksa, program otomatik olarak kurulum önerecektir.
- Otomatik kurulum için ekrana gelen yönergeleri takip edin.
- Manuel kurulum için: [FFmpeg İndir](https://www.gyan.dev/ffmpeg/builds/)

### 4. Programı Başlatma
Ana grafik arayüzü başlatmak için:
```bash
python ixtivh_yt_downloader.py
```

### 5. EXE Dosyası Oluşturmak (İsteğe Bağlı)
PyInstaller ile tek tıkla çalıştırılabilir exe oluşturabilirsiniz:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "temiz_yazili_beyaz.png;." ixtivh_yt_downloader.py
```
- EXE dosyanız `dist` klasöründe oluşur.
- FFmpeg binary'sini (`ffmpeg.exe`) aynı klasöre koymayı unutmayın veya otomatik kurulumdan sonra oluşan `ffmpeg_bin` klasörünü ekleyin.

---

## Sık Karşılaşılan Sorunlar

- **Çözünürlük bulunamadı:**
    - Video bazı kısıtlamalara sahip olabilir veya YouTube API değişmiş olabilir.
    - Kütüphanelerin güncel olduğundan emin olun: `pip install --upgrade pytube yt-dlp moviepy`
    - Farklı bir video ile tekrar deneyin.

- **FFmpeg bulunamadı:**
    - Otomatik kurulum başarısız olursa, FFmpeg'i manuel indirip `ffmpeg_bin` klasörüne `ffmpeg.exe` olarak ekleyin.

- **Başka bilgisayarda çalışmıyor:**
    - Tüm adımları eksiksiz uyguladığınızdan emin olun (Python, bağımlılıklar, FFmpeg).

---

## Ek Bilgiler
- Program çoklu dil desteklidir (Türkçe/İngilizce).
- Arayüzde "Çözünürlükleri Getir" ile mevcut çözünürlükleri görebilirsiniz.
- Herhangi bir hata veya öneri için: [ixtivh](mailto:ixtivh@example.com)

---

### Not:
- Programı başka bir bilgisayara taşırken: `ixtivh_yt_downloader.py`, `ffmpeg_check_and_auto_setup.py`, `requirements.txt`, `temiz_yazili_beyaz.png` ve `ffmpeg_bin` klasörünü birlikte taşıyın.
- İlk çalıştırmadan önce yukarıdaki adımları uygulayın.
