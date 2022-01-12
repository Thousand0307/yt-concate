from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UC1Oq-B1TgUzMTz0zSb8ZDrA'


def main():
    steps = [
        GetVideoList(),
    ]

    inputs = {
        'CHANNEL_ID': 'UC1Oq-B1TgUzMTz0zSb8ZDrA',
    }

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()











