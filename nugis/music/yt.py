from django.conf import settings
import youtube_dl
from .models import Track
from .exeptions import VideoUnavailable


OPTIONS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'outtmpl': settings.BASE_DIR + '/media/music' + '/%(id)s.%(ext)s',
}


def extract_data_video(url):
    try:
        with youtube_dl.YoutubeDL(OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'id': info['id'],
                'url': info['webpage_url'],
                'title': info['title'],
                'thumbnail': info['thumbnail']
                }
    except Exception as e:
        raise VideoUnavailable()
