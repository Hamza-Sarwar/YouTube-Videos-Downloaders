import youtube_dl


def main():
    ydl_opts = {
        'ignoreerrors': True,
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/channel/CHANNEL ID']) # find in view source


if __name__ == '__main__':
    main()
