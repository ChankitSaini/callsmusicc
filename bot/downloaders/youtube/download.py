from os.path import join
from youtube_dl import YoutubeDL

ytdl = YoutubeDL(
    {
        "format": "bestaudio/best",
        "geo-bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "downloads/%(id)s",
        "quiet": True,
    },
)


def download(url: str):
    return join("downloads", url.split("=")[-1]), ytdl.extract_info(url)
