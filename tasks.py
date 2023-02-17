from celery import Celery
import youtube_dl
import logging
import os
logging.getLogger().setLevel(logging.INFO)
celery_app = Celery('tasks', broker='redis://localhost:6379/')

SAVE_PATH ='E:/Downloads'
@celery_app.task
def main(channel_id):
    logging.info('This is an info message')
    ydl_opts = {
        'ignoreerrors': True,
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'outtmpl': SAVE_PATH + f'/{channel_id}' + '/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        logging.info("hi")
        ydl.download([f'https://www.youtube.com/channel/{channel_id}']) # find in view source
