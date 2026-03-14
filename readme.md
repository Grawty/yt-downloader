# [ youtube downloader ]
Basit bir **Python CLI YouTube Downloader**.  
Bu proje, yt-dlp kütüphanesini öğrenmek için oluşturuldu.


## Özellikler
- `.mp4` formatında video indirme
- `.mp3` formatında ses indirme
- Videolar için kalite seçme (144–1080p)
- Playlist (çalma listesi) indirme
- Hatalı videoları atlama (ignoreerrors)

## Gereksinimler
- Python 3.10+
- [FFmpeg](https://ffmpeg.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Kurulum
1. Python ve FFmpeg bilgisayarınızda yüklü olmalı.  
   - FFmpeg’i yüklediyseniz, kurulu olduğu klasörü PATH’e eklemeyi unutmayın veya program içindeki `FFMPEG` ayarını güncelleyin.
2. yt-dlp’yi yükleyin:
```bash
pip install -U yt-dlp