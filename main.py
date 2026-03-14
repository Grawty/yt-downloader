"""..."""
import yt_dlp
FFMPEG = r"C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin"
# FFmpeg PATH’e ekliyse -> FFMPEG = 'ffmpeg'
#               değilse -> FFMPEG = r"C:\...\ffmpeg\bin" dosyası nerede ise orayı yazmalısınız.

print("[ welcome to youtube downloader ]")
print(" ")
print("1 [ mp4 download ]")
print("2 [ mp3 download ]")
print("3 [ playlist download ]")
print(" ")
sec = input("section: ")

if sec == "1":
    try:
        videolink = input("[ youtube link ]: ")
        kalite = int(input("[ quality select ]: "))

        if videolink.startswith("https://youtube.com/playlist"):
            print("\n[ wrong selection ]")
        elif kalite > 1080 or kalite < 144:
            print("\n[ unsupported quality ]")
        else:
            ydl_opts = {
            # Buradaki ffmpeg konumu yüklü olduğu klasör seçilmeli
            'ffmpeg_location': FFMPEG,
            'format': f'bestvideo[ext=mp4][height<={kalite}]+bestaudio[ext=m4a]/best',
            'merge_output_format': 'mp4',
            'outtmpl': 'mp4/%(title)s.%(ext)s'
                # https://github.com/yt-dlp/yt-dlp/blob/e68afb28277b4bee39726dbcbb06801edde9f659/README.md#output-template
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([videolink])

    except yt_dlp.utils.DownloadError:
        print("\n[ invalid or unsupported video link ]")
    except ValueError:
        print("\n[ quality must be a number ]")

elif sec == "2":
    try:
        muziklink = input("[ youtube link ]: ")
        ydl_opts = {
        # Buradaki ffmpeg konumu yüklü olduğu klasör seçilmeli
        'ffmpeg_location': FFMPEG,
        'format': 'bestaudio/best',
        'outtmpl': 'mp3/%(title)s.%(ext)s',
            # https://github.com/yt-dlp/yt-dlp/blob/e68afb28277b4bee39726dbcbb06801edde9f659/README.md#output-template

        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(muziklink)
    except yt_dlp.utils.DownloadError:
        print("\n[ invalid or unsupported video link ]")

elif sec == "3":
    try:
        listlink = input("[ youtube link ]: ")
        kalite = int(input("[ quality select ]: "))

        if kalite > 1080 or kalite < 144:
            print("\n[ unsupported quality ]")
        else:
            ydl_opts = {
            # Buradaki ffmpeg konumu yüklü olduğu klasör seçilmeli
            'ffmpeg_location': FFMPEG,
            'format': f'bestvideo[ext=mp4][height<={kalite}]+bestaudio[ext=m4a]/best',
            'merge_output_format': 'mp4',
            'ignoreerrors': True,
            'outtmpl': '%(playlist)s/%(title)s.%(ext)s'
                # https://github.com/yt-dlp/yt-dlp/blob/e68afb28277b4bee39726dbcbb06801edde9f659/README.md#output-template
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([listlink])

    except yt_dlp.utils.DownloadError:
        print("\n[ invalid or unsupported video link ]")
    except ValueError:
        print("\n[ quality must be a number ]")
    except yt_dlp.utils.EntryNotInPlaylist:
        print("[ null ]")

else:
    print("[ X ]")
