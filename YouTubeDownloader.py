from pytube import YouTube
import re


class YoutubeDownloader:
    def __init__(self):
        self.download()

    def download(self):
        url = input("Ingrese la URL del video: ")
        while (url):
            yt = YouTube(url)
            filename = yt.title + ".mp3"
            try:
                yt.streams.filter(progressive=False, abr='160kbps').first().download(filename=filename)
            except OSError:
                title = re.sub(r"[^a-zA-Z0-9 ]", "", yt.title)
                filename = title + ".mp3"
                yt.streams.filter(progressive=False, abr='160kbps').first().download(filename=filename)
            except AttributeError:
                yt.streams.filter(progressive=False, abr='128kbps').first().download(filename=filename)
            print("Descarga realizada con exito! \n")
            url = input("Ingrese la URL del video: ")

YoutubeDownloader()