from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.downloaded_caption import DownLoadCaption
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils


CHANNEL_ID = 'UC1Oq-B1TgUzMTz0zSb8ZDrA'


def main():
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownLoadCaption(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    inputs = {
        'channel_id': 'UC1Oq-B1TgUzMTz0zSb8ZDrA',
        'search_word': 'love',
        'limit' : 20
    }

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()














