from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.downloaded_caption import DownLoadCaption
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils

CHANNEL_ID = 'UC1Oq-B1TgUzMTz0zSb8ZDrA'


def main():
    steps = [
        Preflight(),
        GetVideoList(),
        DownLoadCaption(),
        Preflight(),
    ]

    inputs = {
        'channel_id': 'UC1Oq-B1TgUzMTz0zSb8ZDrA',
    }

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()











