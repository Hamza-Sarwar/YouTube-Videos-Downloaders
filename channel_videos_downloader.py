import pandas as pd
from tasks import main
def load_urls():
    file = './data/yt_channels.csv'
    df = pd.read_csv(file)
    channel_ids = list(df['ID'])
    return channel_ids


if __name__ == '__main__':
    channel_ids = load_urls()
    for i, channel_id in enumerate(channel_ids):
        main.apply_async((channel_id,),)
        if i == 15:
            break
