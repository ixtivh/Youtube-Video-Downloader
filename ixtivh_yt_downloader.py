# Bu programın tüm hakları saklıdır. (C) 2025 ixtivh. Logo ve kaynak kodu koruma altındadır.
# All rights reserved. (C) 2025 ixtivh. The logo and source code are protected.
def resource_path(relative_path):
    import sys, os
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

LOGO_PATH = resource_path("output-onlinepngtools (1).png")
LOGO_SIZE = (80, 80)

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import shutil
import traceback
import requests
import uuid
import sys



# Çoklu dil desteği sözlüğü
LANGUAGES = {
    'tr': {
        'title': "IXTIVH",
        'youtube_link': "YouTube Linki:",
        'download_type': "İndirme Türü:",
        'mp4': "MP4 (Video)",
        'mp3': "MP3 (Ses)",
        'download_folder': "İndirme Klasörü:",
        'browse': "Gözat",
        'fetch_res': "Çözünürlükleri Getir",
        'choose_res': "Çözünürlük:",
        'download': "İndir",
        'status_ready': "  ",
        'copyright_notice': "Tüm hakları saklıdır.",
        'footer_text': "Tüm hakları saklıdır. Copyright © 2025 ixtivh | YouTube Downloader",
        'language_select': "Dil Seçimi:",
        'select_folder': "Lütfen indirme klasörü seçin!",
        'warning': "Uyarı",
        'please_select_folder': "Lütfen önce indirme klasörü seçin!",
        'mp3_downloading': "MP3 indiriliyor... Bu işlem bir kaç dakika sürebilir lütfen bekleyin.",
        'downloading': "İndiriliyor... Bu işlem bir kaç dakika sürebilir lütfen bekleyin({})",
        'download_complete': "İndirme tamamlandı!",
        'success': "Başarılı",
        'download_folder_msg': "İndirme tamamlandı!\nKlasör: {}",
        'error': "Hata",
        'please_enter_url': "Lütfen bir YouTube linki girin.",
        'audio_downloading': "Ses indiriliyor...",
        'mp3_success': "MP3 başarıyla indirildi.",
        'download_error': "İndirme hatası: {}",
        'please_select_res': "Lütfen bir çözünürlük seçin.",
        'video_downloading': "Video indiriliyor... Bu işlem bir kaç dakika sürebilir lütfen bekleyin.",
        'video_success': "Video başarıyla indirildi.",
        'video_success': "Video başarılı bir şekilde indirildi!!",
        'ffmpeg_required': "FFmpeg Gerekli",
        'ffmpeg_not_found': "FFmpeg bulunamadı. FFmpeg, video işleme için gereklidir. \n\nOtomatik olarak kurulsun mu?",
        'restart_needed': "Yeniden Başlatma Gerekli",
        'ffmpeg_installed': "FFmpeg başarıyla kuruldu! \n\nDeğişikliklerin etkili olması için bilgisayarınızı yeniden başlatmanız gerekmektedir.",
        'ffmpeg_failed': "FFmpeg kurulumu başarısız oldu! \n\nLütfen FFmpeg'i manuel olarak kurun.",
        'ffmpeg_cannot_run': "FFmpeg olmadan program çalışamaz!",
    # Added missing Turkish translations for new keys
    'no_resolution_in_mp3': "MP3 modunda çözünürlük seçimi yok.",
    'fetching_resolutions': "Çözünürlükler getiriliyor...",
    'resolutions_found': "{} çözünürlük bulundu.",
    'no_resolutions_found': "Çözünürlük bulunamadı veya geçersiz link.",
    'error_with_detail': "Hata: {}",
    'cancel': "İptal",
    'download_cancelled': "İndirme iptal edildi!",
    'folder_error': "Klasör Hatası",
    'folder_create_failed': "Klasör oluşturulamadı:\n{}\n{}",
    },
    'en': {
        'title': "IXTIVH",
        'youtube_link': "YouTube Link:",
        'download_type': "Download Type:",
        'mp4': "MP4 (Video)",
        'mp3': "MP3 (Audio)",
        'download_folder': "Download Folder:",
        'browse': "Browse",
        'fetch_res': "Fetch Resolutions",
        'choose_res': "Resolution:",
        'download': "Download",
        'status_ready': "",
        'copyright_notice': "All rights reserved.",
        'footer_text': "All rights reserved. Copyright © 2025 ixtivh | YouTube Downloader",
        'language_select': "Language:",
        'select_folder': "Please select a download folder!",
        'warning': "Warning",
        'please_select_folder': "Please select a download folder first!",
        'mp3_downloading': "Downloading MP3... This may take a few minutes, please wait.",
        'downloading': "Downloading... ({})",
        'download_complete': "Download complete!",
        'success': "Success",
        'download_folder_msg': "Download complete!\nFolder: {}",
        'error': "Error",
        'please_enter_url': "Please enter a YouTube link.",
        'audio_downloading': "Downloading audio... This may take a few minutes, please wait.",
        'mp3_success': "MP3 downloaded successfully.",
        'download_error': "Download error: {}",
        'please_select_res': "Please select a resolution.",
        'video_downloading': "Downloading video... This may take a few minutes, please wait.",
        'video_success': "Video downloaded successfully.",
        'video_success': "Video downloaded successfully.",
        'ffmpeg_required': "FFmpeg Required",
        'ffmpeg_not_found': "FFmpeg not found. FFmpeg is required for video processing. \n\nInstall automatically?",
        'restart_needed': "Restart Required",
        'ffmpeg_installed': "FFmpeg installed successfully! \n\nYou must restart your computer for changes to take effect.",
        'ffmpeg_failed': "FFmpeg installation failed! \n\nPlease install FFmpeg manually.",
        'ffmpeg_cannot_run': "The program cannot run without FFmpeg!",
    # Added missing English translations for Turkish messages
    'no_resolution_in_mp3': "No resolution selection in MP3 mode.",
    'fetching_resolutions': "Fetching resolutions...",
    'resolutions_found': "{} resolutions found.",
    'no_resolutions_found': "No resolutions found or invalid link.",
    'error_with_detail': "Error: {}",
    'cancel': "Cancel",
    'download_cancelled': "Download cancelled!",
    'folder_error': "Folder Error",
    'folder_create_failed': "Could not create folder:\n{}\n{}",
    }

}

current_lang = 'tr'  # Varsayılan dil

def _(key):
    return LANGUAGES[current_lang][key]

import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from PIL import Image, ImageTk
import threading
import subprocess
import json

def resource_path(relative_path):
    # PyInstaller ile EXE'de çalışırken logo dosyalarını bulmak için
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

import os
import sys

# Komut penceresiz çalıştırmak için Windows sabiti
if os.name == 'nt':
    CREATE_NO_WINDOW = 0x08000000
else:
    CREATE_NO_WINDOW = 0

# PyInstaller ile paketlenmişse kaynak dosyalarını bulmak için
import sys, os
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



# Hata loglama fonksiyonu
def log_error(msg):
    with open(os.path.join(BASE_DIR, 'yt_downloader_error.log'), 'a', encoding='utf-8') as f:
        f.write(msg + '\n')

# İnternet bağlantısı kontrolü
def check_internet():
    import socket
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except Exception:
        return False

# Bağımlılık ve dosya bütünlüğü kontrol fonksiyonları
def is_program_available(cmd):
    # Önce program klasöründe var mı bak
    exe_path = os.path.join(BASE_DIR, cmd)
    if os.path.isfile(exe_path):
        return True
    # Yoksa PATH'te var mı bak
    return shutil.which(cmd) is not None

def is_yt_dlp_available():
    try:
        import yt_dlp
        return True
    except ImportError:
        # .exe kontrolü
        return is_program_available('yt-dlp.exe') or is_program_available('yt-dlp')

def try_auto_install_yt_dlp():
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        return True
    except Exception as e:
        log_error(f"yt-dlp otomatik yükleme hatası: {e}\n{traceback.format_exc()}")
        return False

def is_ffmpeg_available():
    return is_program_available('ffmpeg.exe') or is_program_available('ffmpeg')

def check_required_files():
    missing = []
    # Burada başka zorunlu dosyalar varsa ekle
    return missing

# Komut satırından veya modül olarak yt-dlp ile çözünürlükleri al

def get_formats(url):
    # 1. Dosya bütünlüğü kontrolü
    missing_files = check_required_files()
    if missing_files:
        messagebox.showerror("Eksik Dosya", f"Eksik dosyalar: {', '.join(missing_files)}\nLütfen program klasörüne ekleyin.")
        log_error(f"Eksik dosya: {', '.join(missing_files)}")
        return []
    # 2. İnternet kontrolü
    if not check_internet():
        messagebox.showerror("İnternet Yok", "Çözünürlükleri almak için internet bağlantısı gereklidir!")
        log_error("İnternet bağlantısı yok.")
        return []
    # 3. yt-dlp kontrolü
    if not is_yt_dlp_available():
        if messagebox.askyesno("yt-dlp Eksik", "yt-dlp bulunamadı! Otomatik yüklemeyi denemek ister misiniz?"):
            ok = try_auto_install_yt_dlp()
            if ok and is_yt_dlp_available():
                messagebox.showinfo("yt-dlp Yüklendi", "yt-dlp başarıyla yüklendi. Lütfen tekrar deneyin.")
                return []
            else:
                messagebox.showerror("yt-dlp Hatası", "yt-dlp otomatik yüklenemedi!\nElle yükleyin veya internet bağlantınızı kontrol edin.")
                log_error("yt-dlp otomatik yüklenemedi.")
                return []
        else:
            messagebox.showerror("yt-dlp Eksik", "yt-dlp bulunamadı! Programın bulunduğu klasörde yt-dlp modülü veya yt-dlp.exe olmalı.")
            log_error("yt-dlp bulunamadı.")
            return []
    # 4. ffmpeg kontrolü (çözünürlük için değil ama genel kontrol için)
    if not is_ffmpeg_available():
        messagebox.showwarning("FFmpeg Eksik", "FFmpeg bulunamadı! Video/MP3 indirmek için gerekli olabilir.")
        log_error("FFmpeg bulunamadı.")
    try:
        # Önce Python modülü olarak dene
        try:
            import yt_dlp
            ydl_opts = {'quiet': True, 'skip_download': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            log_error("yt-dlp python modülü ile başarıyla getirildi.")
        except ImportError:
            # Komut satırı olarak dene
            # Program klasöründe yt-dlp.exe var mı bak
            ytdlp_path = os.path.join(BASE_DIR, 'yt-dlp.exe')
            if not os.path.isfile(ytdlp_path):
                ytdlp_path = 'yt-dlp'  # PATH'te aranacak
            result = subprocess.run(
                [ytdlp_path, '-j', url],
                capture_output=True, text=True, check=True,
                creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            info = json.loads(result.stdout)
            formats = info.get('formats', [])
            log_error("yt-dlp komut satırı ile başarıyla getirildi.")
        resolutions = []
        for f in formats:
            # Sadece video-only (acodec none) mp4 formatlar listelensin
            if (
                f.get('ext') == 'mp4'
                and f.get('height') and 360 <= f['height'] <= 1080
                and f.get('acodec', 'none') == 'none'  # sadece video
            ):
                label = f"{f['height']}p- {f['format_id']}"
                resolutions.append(label)
        # Yüksekten düşüğe sırala
        resolutions = sorted(set(resolutions), key=lambda x: int(x.split('p')[0]), reverse=True)
        if not resolutions:
            messagebox.showerror("Çözünürlük Yok", "Videodan çözünürlük alınamadı. Video özel/kısıtlı olabilir veya YouTube API değişmiş olabilir.")
            log_error(f"Çözünürlük bulunamadı: {url}")
        return resolutions
    except Exception as e:
        err_msg = f"YT-DLP format hatası: {e}\n{traceback.format_exc()}"
        log_error(err_msg)
        messagebox.showerror("yt-dlp Hatası", f"Çözünürlükler alınamadı!\nHata: {e}\nDetaylı bilgi için yt_downloader_error.log dosyasına bakınız.\n\nOlası nedenler:\n- İnternet yok\n- yt-dlp eksik\n- Video özel/kısıtlı\n- Güvenlik yazılımı engelliyor")
        return []

def download_video(url, format_id, status_label, download_btn, mode, download_dir):
    try:
        if not download_dir:
            status_label.config(text=_('select_folder'))
            messagebox.showwarning(_('warning'), _('please_select_folder'))
            download_btn.config(state=tk.NORMAL)
            return
        # Bağımlılık kontrolü
        if not is_yt_dlp_available():
            messagebox.showerror("yt-dlp Missing", "yt-dlp not found! There must be a yt-dlp module or yt-dlp.exe in the program folder.\nSolution: If you have an internet connection, restart the program or install it manually.") if current_lang == 'en' else messagebox.showerror("yt-dlp Eksik", "yt-dlp bulunamadı! Programın bulunduğu klasörde yt-dlp modülü veya yt-dlp.exe olmalı.\nÇözüm: İnternet bağlantınız varsa programı tekrar başlatın veya elle yükleyin.")
            download_btn.config(state=tk.NORMAL)
            return
        if not is_ffmpeg_available():
            messagebox.showerror("FFmpeg Missing", "FFmpeg not found! Please add ffmpeg.exe to the program folder or use an internet connection for automatic installation.") if current_lang == 'en' else messagebox.showerror("FFmpeg Eksik", "FFmpeg bulunamadı! ffmpeg.exe dosyasını program klasörüne ekleyin veya internet bağlantısı ile otomatik kurulum yapın.")
            download_btn.config(state=tk.NORMAL)
            return
        # Program klasöründe yt-dlp.exe var mı bak
        ytdlp_path = os.path.join(BASE_DIR, 'yt-dlp.exe')
        if not os.path.isfile(ytdlp_path):
            ytdlp_path = 'yt-dlp'  # PATH'te aranacak
        if mode == 'mp3':
            status_label.config(text="MP3 indiriliyor...")
            cmd = [
                ytdlp_path,
                '-f', 'bestaudio',
                '--extract-audio',
                '--audio-format', 'mp3',
                '-P', download_dir,
                url
            ]
        else:
            status_label.config(text=f"İndiriliyor... ({format_id})")
            cmd = [
                ytdlp_path,
                '-f', format_id,
                '-P', download_dir,
                url
            ]
        subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0)
        status_label.config(text=_('download_complete'))
        messagebox.showinfo(_('success'), _('download_folder_msg').format(download_dir))
    except Exception as e:
        status_label.config(text=f"{_('error')}: {e}")
        messagebox.showerror(_('error'), str(e))
    finally:
        download_btn.config(state=tk.NORMAL)

def start_download(url_entry, res_combo, status_label, download_btn, mode_var, download_dir_var):
    url = url_entry.get().strip()
    selected = res_combo.get()
    download_dir = download_dir_var.get()
    if not url:
        messagebox.showwarning("Uyarı", "Lütfen bir YouTube linki girin.")
        return
    if mode_var.get() == 'mp3':
        # MP3 indirme
        status_label.config(text="Ses indiriliyor...")
        download_btn.config(state='disabled')
        def worker():
            try:
                cmd = [
                    'yt-dlp', '-f', 'bestaudio',
                    '-x', '--audio-format', 'mp3',
                    '-o', os.path.join(download_dir, '%(title)s.%(ext)s'), url
                ]
                subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0)
                status_label.config(text="MP3 başarıyla indirildi.")
            except Exception as e:
                status_label.config(text=f"İndirme hatası: {e}")
            finally:
                download_btn.config(state='normal')
        threading.Thread(target=worker, daemon=True).start()
        return
    if not selected:
        messagebox.showwarning("Uyarı", "Lütfen bir çözünürlük seçin.")
        return
    # Format ID'yi ayıkla
    format_id = selected.split('-')[-1].strip()
    status_label.config(text="Video indiriliyor...")
    download_btn.config(state='disabled')
    def worker():
        try:
            # Eğer sadece video (acodec none) ise, en iyi sesle otomatik birleştir
            # Seçilen video-only formatı ve en iyi sesi indirip birleştir (muxing), çıktı mp4 olsun
            cmd = [
                'yt-dlp',
                '-f', f'{format_id}+bestaudio',
                '--audio-format', 'aac',  # Ses formatını AAC olarak belirt
                '-o', os.path.join(download_dir, '%(title)s.%(ext)s'),
                '--merge-output-format', 'mp4',
                '--postprocessor-args', '-acodec aac',  # FFmpeg'e AAC codec'ini kullan talimatı ver
                url
            ]
            subprocess.run(cmd, check=True, creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0)
            status_label.config(text="Video ve ses başarıyla indirildi ve birleştirildi (yt-dlp ile mp4 olarak kaydedildi).")
        except Exception as e:
            status_label.config(text=f"İndirme hatası: {e}")
        finally:
            download_btn.config(state='normal')
    threading.Thread(target=worker, daemon=True).start()

def fetch_resolutions(url_entry, res_combo, status_label, mode_var):
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Uyarı", "Lütfen önce bir YouTube linki girin.")
        return
    if mode_var.get() == 'mp3':
        res_combo['values'] = []
        res_combo.set('')
        status_label.config(text=_('no_resolution_in_mp3'))
        return
    status_label.config(text=_('fetching_resolutions'))
    def worker():
        try:
            resolutions = get_formats(url)
            if resolutions:
                res_combo['values'] = resolutions
                res_combo.set(resolutions[0])
                status_label.config(text=_('resolutions_found').format(len(resolutions)))
            else:
                res_combo['values'] = []
                res_combo.set('')
                status_label.config(text=_('no_resolutions_found'))
        except Exception as e:
            res_combo['values'] = []
            res_combo.set('')
            status_label.config(text=_('error_with_detail').format(e))
    threading.Thread(target=worker, daemon=True).start()

def on_mode_change(res_combo, status_label, mode_var):
    if mode_var.get() == 'mp3':
        res_combo['values'] = []
        res_combo.set('')
        status_label.config(text=_('no_resolution_in_mp3'))
        res_combo.config(state='disabled')
    else:
        res_combo.config(state='readonly')
        status_label.config(text="")

def check_and_setup_ffmpeg():
    from ffmpeg_check_and_auto_setup import is_ffmpeg_installed, download_and_setup_ffmpeg
    
    if not is_ffmpeg_installed():
        root = tk.Tk()
        root.withdraw()  # Ana pencereyi gizle
        
        result = messagebox.askyesno(
            "FFmpeg Gerekli",
            "FFmpeg bulunamadı. FFmpeg, video işleme için gereklidir. \n\n" \
            "Otomatik olarak kurulsun mu?"
        )
        
        if result:
            success = download_and_setup_ffmpeg()
            if success:
                messagebox.showwarning(
                    "Yeniden Başlatma Gerekli",
                    "FFmpeg başarıyla kuruldu! \n\n" \
                    "Değişikliklerin etkili olması için bilgisayarınızı yeniden başlatmanız gerekmektedir."
                )
            else:
                messagebox.showerror(
                    "Hata",
                    "FFmpeg kurulumu başarısız oldu! \n\n" \
                    "Lütfen FFmpeg'i manuel olarak kurun."
                )
                sys.exit(1)
        else:
            messagebox.showwarning(
                "FFmpeg Gerekli",
                "FFmpeg olmadan program çalışamaz!"
            )
            sys.exit(1)
        
        root.destroy()

def main():
    global current_lang
    # FFmpeg kontrolü ve kurulumu
    check_and_setup_ffmpeg()
    
    # YouTube teması renkleri
    YT_RED = "#FF0000"
    YT_BG = "#000000"  # Tam siyah
    YT_ENTRY_BG = "#000000"  # Tam siyah
    YT_FG = YT_RED  # Tüm yazılar kırmızı
    bg_color = YT_BG
    YT_BTN_BG = YT_RED
    YT_BTN_FG = YT_FG
    YT_HIGHLIGHT = YT_RED
    YT_LABEL_COLOR = YT_FG
    YT_STATUS_FG = YT_RED
    entry_bg = YT_ENTRY_BG
    entry_fg = YT_FG
    button_bg = YT_BG
    button_fg = YT_RED
    highlight_color = YT_RED
    label_color = YT_LABEL_COLOR
    status_fg = YT_RED

    def update_texts():
        root.title(_("title"))
        url_label.config(text=_("youtube_link"))
        mode_label.config(text=_("download_type"))
        mp4_radio.config(text=_("mp4"))
        mp3_radio.config(text=_("mp3"))
        download_dir_label.config(text=_("download_folder"))
        browse_btn.config(text=_("browse"))
        res_label.config(text=_("choose_res"))
        fetch_btn.config(text=_("fetch_res"))
        download_btn.config(text=_("download"))
        status_label.config(text=_("status_ready"))
        # Update footer and language label if they exist
        try:
            footer.config(text=_("footer_text"))
        except Exception:
            pass
        try:
            lang_label.config(text=_("language_select"))
        except Exception:
            pass


    # Ana pencereyi oluştur
    root = tk.Tk()
    root.title(_("title"))

    # Sol üstte büyük logo (ixtivh yazısı yerine)
    try:
        logo_img = Image.open(LOGO_PATH).resize(LOGO_SIZE, Image.LANCZOS)
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(root, image=logo, bg=bg_color)
        logo_label.image = logo
        logo_label.pack(pady=(16, 0))
    except Exception:
        logo_label = tk.Label(root, text="ixtivh", font=("Arial", 24, "bold"), fg=label_color, bg=bg_color)
        logo_label.pack(pady=(16, 0))
    # Sağ üst köşeye küçük YouTube logosu (en önde ve paddingli)
    try:
        yt_logo_img = Image.open(resource_path('Youtube_logo.png'))
        w, h = yt_logo_img.size
        new_h = 32
        new_w = int(w * (new_h / h))
        yt_logo_img = yt_logo_img.resize((new_w, new_h), Image.LANCZOS)
        yt_logo = ImageTk.PhotoImage(yt_logo_img)
        yt_logo_label = tk.Label(root, image=yt_logo, bg=bg_color, bd=0, highlightthickness=0)
        yt_logo_label.image = yt_logo
        yt_logo_label.place(relx=1.0, y=20, x=-16, anchor='ne')
        yt_logo_label.lift()
    except Exception:
        pass

    lang_var = tk.StringVar(value='Türkçe' if current_lang == 'tr' else 'English')
    def set_lang_entry(val):
        lang_entry.config(state='normal')
        lang_entry.delete(0, tk.END)
        lang_entry.insert(0, val)
        lang_entry.config(state='disabled')
        global current_lang
        current_lang = 'tr' if val == 'Türkçe' else 'en'
        update_texts()
    lang_frame = tk.Frame(root, bg=bg_color)
    lang_frame.place(relx=0.0, rely=0.0, x=10, y=10, anchor='nw')
    lang_label = tk.Label(lang_frame, text=_('language_select'), bg=bg_color, fg=highlight_color, font=("Segoe UI", 11, "bold"))
    lang_label.pack(side='left', padx=(0, 4))

    lang_entry = tk.Entry(lang_frame, width=8, font=("Segoe UI", 10, "bold"),
                         bg='#000000', fg='#FF0000', relief=tk.FLAT, justify='center',
                         highlightthickness=2, highlightbackground=highlight_color, highlightcolor=highlight_color,
                         insertbackground='#FF0000', disabledbackground='#000000', disabledforeground='#FF0000')
    lang_entry.pack(side='left')
    lang_entry.insert(0, lang_var.get())
    lang_entry.config(state='disabled')
    def show_lang_menu(event):
        menu = tk.Menu(lang_frame, tearoff=0, bg='#000000', fg='#FF0000', activebackground=highlight_color, activeforeground='#000000', borderwidth=0)
        menu.add_command(label='Türkçe', command=lambda: set_lang_entry('Türkçe'))
        menu.add_command(label='English', command=lambda: set_lang_entry('English'))
        menu.tk_popup(event.x_root, event.y_root)
    lang_entry.bind('<Button-1>', show_lang_menu)
    def on_lang_change(event=None):
        val = lang_entry.get()
        set_lang_entry(val)

    try:
        # root.iconphoto(True, ImageTk.PhotoImage(Image.open(resource_path('temiz_yazili_beyaz.png')).resize((64, 64), Image.LANCZOS)))
        pass
    except Exception:
        pass
    root.geometry("540x480")
    root.resizable(False, False)
    root.configure(bg=bg_color)

    url_label = tk.Label(root, text=_("youtube_link"), bg=bg_color, fg=label_color)
    url_label.pack(pady=(10, 0))
    url_entry = tk.Entry(root, width=55, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg, relief=tk.FLAT, highlightthickness=1, highlightbackground='#FFFFFF')
    url_entry.pack(pady=5)

    mode_var = tk.StringVar(value='mp4')
    mode_frame = tk.Frame(root, bg=bg_color)
    mode_frame.pack(pady=(0, 5))
    mode_label = tk.Label(mode_frame, text=_("download_type"), bg=bg_color, fg=label_color)
    mode_label.pack(side='left')
    mp4_radio = tk.Radiobutton(mode_frame, text=_("mp4"), variable=mode_var, value='mp4', bg=bg_color, fg=label_color, selectcolor=button_bg, activebackground=bg_color)
    mp4_radio.pack(side='left', padx=5)
    mp3_radio = tk.Radiobutton(mode_frame, text=_("mp3"), variable=mode_var, value='mp3', bg=bg_color, fg=label_color, selectcolor=button_bg, activebackground=bg_color)
    mp3_radio.pack(side='left', padx=5)

    # İndirme klasörü seçimi
    download_dir_frame = tk.Frame(root, bg=bg_color)
    download_dir_frame.pack(pady=5, fill='x', padx=10)
    download_dir_label = tk.Label(download_dir_frame, text=_("download_folder"), bg=bg_color, fg=label_color)
    download_dir_label.pack(side='left')
    # Varsayılan indirme klasörü: Kullanıcının Downloads/ixtivh_youtube_videovemuzikler klasörü
    import getpass
    import platform
    if platform.system() == "Windows":
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    default_download_dir = os.path.join(downloads_folder, 'ixtivh_youtube_videovemuzikler')
    download_dir_var = tk.StringVar(value=default_download_dir)
    download_dir_entry = tk.Entry(
        download_dir_frame,
        textvariable=download_dir_var,
        width=45,
        bg=entry_bg,
        fg=entry_fg,
        insertbackground=entry_fg,
        relief=tk.FLAT,
        highlightthickness=1,
        highlightbackground='#FFFFFF',
        readonlybackground=entry_bg,
        state='readonly'
    )
    download_dir_entry.pack(side='left', padx=5)
    def browse_dir():
        dir_path = filedialog.askdirectory()
        if dir_path:
            download_dir_var.set(dir_path)
    browse_btn = tk.Button(
        download_dir_frame,
        text=_("browse"),
        command=browse_dir,
        bg=button_bg,
        fg=button_fg,
        activebackground=highlight_color,
        activeforeground=button_fg,
        relief=tk.GROOVE,  # Make border visible
        bd=3,              # Thicker border
        highlightthickness=2,
        highlightbackground=highlight_color,
        highlightcolor=highlight_color,
        padx=10
    )
    browse_btn.pack(side='left', padx=5)

    # Çözünürlük seçimi frame
    res_frame = tk.Frame(root, bg=bg_color)
    res_frame.pack(pady=10, fill='x', padx=10)
    res_label = tk.Label(res_frame, text=_("choose_res"), bg=bg_color, fg=label_color)
    res_label.pack(side='left')
    style = ttk.Style()
    style.theme_use('clam')
    style.configure(
        'Custom.TCombobox',
        fieldbackground=YT_BG,
        background=YT_BG,
        foreground=YT_RED,
        selectbackground=YT_BG,
        selectforeground=YT_RED,
        arrowcolor='#FFFFFF',  # Ok ve kenarlıklar beyaz
        bordercolor='#FFFFFF',
        lightcolor='#FFFFFF',
        darkcolor='#FFFFFF'
    )
    style.map(
        'Custom.TCombobox',
        fieldbackground=[('readonly', YT_BG)],
        selectbackground=[('readonly', YT_BG)],
        background=[('readonly', YT_BG)],
        foreground=[('readonly', YT_RED)]
    )
    # Açılır menü (dropdown) için Listbox ve Popdown stilleri
    style.configure('TCombobox',
        selectbackground=YT_BG,
        selectforeground=YT_RED,
        fieldbackground=YT_BG,
        background=YT_BG,
        foreground=YT_RED
    )
    style.configure('TCombobox PopdownFrame', background=YT_BG)
    style.configure('TCombobox Listbox', background=YT_BG, foreground=YT_RED, selectbackground=YT_BG, selectforeground=YT_RED)

    res_combo = ttk.Combobox(
        res_frame,
        state="readonly",
        width=40,
        style='Custom.TCombobox'
    )
    res_combo.pack(side='left', padx=5)
    fetch_btn = tk.Button(
        res_frame,
        text=_("fetch_res"),
        bg=YT_BG,
        fg=YT_RED,
        activebackground=YT_BG,
        activeforeground=YT_RED,
        relief=tk.GROOVE,
        padx=10,
        highlightthickness=3,
        highlightbackground='#FFFFFF',
        highlightcolor='#FFFFFF',
        bd=3
    )
    fetch_btn.pack(side='left', padx=5)

    # İlerleme başlığı
    # Dalga animasyonlu loading bar ve iptal butonu
    progress_cancel_frame = tk.Frame(root, bg=bg_color)
    progress_cancel_frame.pack(pady=(16, 8))
    wave_canvas = tk.Canvas(progress_cancel_frame, width=270, height=16, bg=YT_ENTRY_BG, highlightthickness=2, highlightbackground=YT_RED)
    wave_canvas.pack(side='left', padx=(0, 16))
    # Küçük iptal butonu
    cancel_btn = tk.Button(progress_cancel_frame, text=_('cancel'), bg=YT_BG, fg=YT_RED, activebackground=YT_BG, activeforeground=YT_RED, relief=tk.GROOVE, font=("Arial", 10, "bold"), width=8, height=1, highlightthickness=2, highlightbackground='#FFFFFF', highlightcolor='#FFFFFF', bd=2)
    cancel_btn.pack(side='left', padx=(0, 0))
    cancel_btn.config(state='disabled')

    # Dalga animasyonu fonksiyonu
    wave_anim = {'running': False}
    def animate_wave():
        import math
        if not wave_anim['running']:
            wave_canvas.delete('all')
            return
        wave_canvas.delete('all')
        width = 270
        height = 16
        t = animate_wave.t
        freq = 2 * math.pi / 60
        amp = 6
        phase_speed = 0.18
        points = []
        for x in range(width):
            y = int(height/2 + amp * math.sin(freq*x + t))
            points.append((x, y))
        for i in range(len(points)-1):
            wave_canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=YT_RED, width=5, smooth=True)
        animate_wave.t += phase_speed
        wave_canvas.after(16, animate_wave)
    animate_wave.t = 0
    def start_wave():
        wave_anim['running'] = True
        animate_wave()
    def stop_wave():
        wave_anim['running'] = False
        wave_canvas.delete('all')

    # --- İndirme başlatıldığında kullanılacak metin ---
    download_in_progress_text = "İndirme işlemi başlatıldı, bu işlem birkaç dakika sürebilir..." if current_lang == 'tr' else "Download started, this may take a few minutes..."


    # İndir butonu (daha geniş)
    download_btn = tk.Button(root, text=_("download"), bg=YT_BG, fg=YT_RED, activebackground=YT_BG, activeforeground=YT_RED, relief=tk.GROOVE, font=("Arial", 13, "bold"), width=13, height=1, bd=2, cursor='hand2', highlightthickness=2, highlightbackground='#FFFFFF', highlightcolor='#FFFFFF')
    download_btn.pack(pady=8)

    status_label = tk.Label(root, text="", bg=bg_color, fg=status_fg)
    status_label.pack(pady=(0, 10))

    update_texts()

    # Modern alt bilgi (sp_downloader tarzı, marka vurgulu)
    footer = tk.Label(root, text=_('footer_text'), font=("Segoe UI", 9), bg=bg_color, fg="#FFFFFF")
    footer.pack(side='bottom', pady=(0, 2))


    # İptal işlevi için kontrol
    download_cancel_flag = {'cancel': False}

    def cancel_download():
        download_cancel_flag['cancel'] = True
        cancel_btn.config(state='disabled')
        status_label.config(text="İndirme iptal edildi!", fg="#b71c1c")
        progress_var.set(0)

    cancel_btn.config(command=cancel_download)

    def update_progress(percent):
        # Dalga animasyonlu loading bar olduğu için bu fonksiyon artık kullanılmıyor.
        pass

        root.update_idletasks()

    def download_with_progress(*args, **kwargs):
        # Dalga animasyonu başlat
        status_label.config(text=download_in_progress_text, fg=YT_RED)
        start_wave()
        # --- İndirme işlemini başlat ---
        import time
        url = url_entry.get().strip()
        selected = res_combo.get()
        download_dir = download_dir_var.get()
        # Klasörü oluştur (varsa hata vermez)
        try:
            os.makedirs(download_dir, exist_ok=True)
        except Exception as e:
            messagebox.showerror(_('folder_error'), _('folder_create_failed').format(download_dir, e))
            return
        mode = mode_var.get()
        if not url:
            messagebox.showwarning("Uyarı", "Lütfen bir YouTube linki girin.")
            return
        if mode == 'mp3':
            status_label.config(text="Ses indiriliyor...")
            download_btn.config(state='disabled')
            cancel_btn.config(state='normal')
            def worker():
                try:
                    cmd = [
                        'yt-dlp', '-f', 'bestaudio',
                        '-x', '--audio-format', 'mp3',
                        '-o', os.path.join(download_dir, '%(title)s.%(ext)s'), url
                    ]
                    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0)
                    for line in process.stdout:
                        if download_cancel_flag['cancel']:
                            process.terminate()
                            status_label.config(text="İndirme iptal edildi!", fg="#b71c1c")
                            stop_wave()
                            break
                        if "%" in line:
                            import re
                            match = re.search(r"(\d{1,3}\.\d)%", line)
                            if match:
                                percent = float(match.group(1))
                                update_progress(percent)
                    process.wait()
                    if process.returncode == 0 and not download_cancel_flag['cancel']:
                        status_label.config(text="MP3 başarıyla indirildi.")
                        update_progress(100)
                        stop_wave()
                except Exception as e:
                    status_label.config(text=f"İndirme hatası: {e}")
                    stop_wave()
                finally:
                    download_btn.config(state='normal')
                    cancel_btn.config(state='disabled')
                    download_cancel_flag['cancel'] = False
                    update_progress(0)
                    stop_wave()
            threading.Thread(target=worker, daemon=True).start()
            return
        if not selected:
            messagebox.showwarning("Uyarı", "Lütfen bir çözünürlük seçin.")
            return
        format_id = selected.split('-')[-1].strip()
        status_label.config(text=_('video_downloading'))
        download_btn.config(state='disabled')
        cancel_btn.config(state='normal')
        def worker():
            try:
                cmd = [
                    'yt-dlp',
                    '-f', f'{format_id}+bestaudio',
                    '--audio-format', 'aac',
                    '-o', os.path.join(download_dir, '%(title)s.%(ext)s'),
                    '--merge-output-format', 'mp4',
                    '--postprocessor-args', '-acodec aac',
                    url
                ]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, creationflags=CREATE_NO_WINDOW if os.name == 'nt' else 0)
                for line in process.stdout:
                    if download_cancel_flag['cancel']:
                        process.terminate()
                        status_label.config(text="İndirme iptal edildi!", fg="#b71c1c")
                        break
                    if "%" in line:
                        import re
                        match = re.search(r"(\d{1,3}\.\d)%", line)
                        if match:
                            percent = float(match.group(1))
                            update_progress(percent)
                process.wait()
                if process.returncode == 0 and not download_cancel_flag['cancel']:
                    status_label.config(text=_('video_success'))
                    update_progress(100)
                    stop_wave()
            except Exception as e:
                status_label.config(text=f"İndirme hatası: {e}")
                stop_wave()
            finally:
                download_btn.config(state='normal')
                cancel_btn.config(state='disabled')
                download_cancel_flag['cancel'] = False
                update_progress(0)
                stop_wave()
        threading.Thread(target=worker, daemon=True).start()

    fetch_btn.config(command=lambda: fetch_resolutions(url_entry, res_combo, status_label, mode_var))
    download_btn.config(command=download_with_progress)
    mode_var.trace_add('write', lambda *args: on_mode_change(res_combo, status_label, mode_var))

    root.mainloop()

if __name__ == "__main__":
    # Program başında bütünlük ve erişim kontrolleri
    missing_files = check_required_files()
    if missing_files:
        messagebox.showerror("Eksik Dosya", f"Eksik dosyalar: {', '.join(missing_files)}\nLütfen program klasörüne ekleyin.")
        log_error(f"Eksik dosya: {', '.join(missing_files)}")
    elif not check_internet():
        messagebox.showerror("İnternet Yok", "Programın tam çalışabilmesi için internet bağlantısı gereklidir!")
        log_error("İnternet bağlantısı yok (başlangıç).")
    elif not is_yt_dlp_available():
        if messagebox.askyesno("yt-dlp Eksik", "yt-dlp bulunamadı! Otomatik yüklemeyi denemek ister misiniz?"):
            ok = try_auto_install_yt_dlp()
            if ok and is_yt_dlp_available():
                messagebox.showinfo("yt-dlp Yüklendi", "yt-dlp başarıyla yüklendi. Lütfen tekrar deneyin.")
            else:
                messagebox.showerror("yt-dlp Hatası", "yt-dlp otomatik yüklenemedi!\nElle yükleyin veya internet bağlantınızı kontrol edin.")
                log_error("yt-dlp otomatik yüklenemedi (başlangıç).")
        else:
            messagebox.showerror("yt-dlp Eksik", "yt-dlp bulunamadı! Programın bulunduğu klasörde yt-dlp modülü veya yt-dlp.exe olmalı.")
            log_error("yt-dlp bulunamadı (başlangıç).")
    else:
        main()
