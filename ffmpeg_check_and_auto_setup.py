import os
import shutil
import subprocess
import sys
import zipfile
import urllib.request
import platform
import winreg

def is_ffmpeg_installed():
    """Komut satırında ffmpeg erişilebilir mi kontrol eder."""
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False

def download_and_setup_ffmpeg(target_dir="ffmpeg_bin"):
    ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    zip_path = os.path.join(target_dir, "ffmpeg.zip")
    ffmpeg_extracted_dir = os.path.join(target_dir, "ffmpeg_extracted")
    ffmpeg_bin_dir = None
    os.makedirs(target_dir, exist_ok=True)
    print("FFmpeg indiriliyor...")
    urllib.request.urlretrieve(ffmpeg_url, zip_path)
    print("FFmpeg zip açılıyor...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(ffmpeg_extracted_dir)
    # Bin klasörünü bul
    for root, dirs, files in os.walk(ffmpeg_extracted_dir):
        if 'ffmpeg.exe' in files:
            ffmpeg_bin_dir = root
            break
    if not ffmpeg_bin_dir:
        print("ffmpeg.exe bulunamadı!")
        return False
    shutil.copy(os.path.join(ffmpeg_bin_dir, 'ffmpeg.exe'), target_dir)
    print(f"ffmpeg.exe {target_dir} klasörüne kopyalandı.")
    # PATH'e ekle (hem mevcut oturum hem kalıcı)
    abs_target_dir = os.path.abspath(target_dir)
    os.environ["PATH"] = abs_target_dir + os.pathsep + os.environ["PATH"]
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_READ | winreg.KEY_SET_VALUE) as key:
            try:
                current_path, _ = winreg.QueryValueEx(key, 'PATH')
            except FileNotFoundError:
                current_path = ''
            if abs_target_dir not in current_path:
                new_path = abs_target_dir + os.pathsep + current_path
                winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)
                print(f"{abs_target_dir} başarıyla PATH ortam değişkenine eklendi. Oturumu kapatıp açınca etkinleşir.")
            else:
                print(f"{abs_target_dir} zaten PATH ortam değişkeninde var.")
    except Exception as e:
        print(f"PATH ortam değişkenine eklenemedi: {e}")
    print("Artık ffmpeg.exe otomatik olarak kullanılabilir.")
    return True

def main():
    if is_ffmpeg_installed():
        print("FFmpeg zaten kurulu ve PATH'te erişilebilir.")
        sys.exit(0)
    print("FFmpeg bulunamadı, otomatik kurulum başlatılıyor...")
    success = download_and_setup_ffmpeg()
    if success:
        print("FFmpeg başarıyla kuruldu ve PATH'e eklendi. Oturumu kapatıp açın.")
    else:
        print("FFmpeg kurulumu başarısız oldu!")

if __name__ == "__main__":
    main()
