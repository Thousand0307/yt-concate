import time

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step, StepException


class DownLoadCaption(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print(yt.url)
            if utils.caption_file_exist(yt):
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except (KeyError, AttributeError):
                print('KeyError or AttributeError in', yt.url)
                continue

            # save the caption to a file named Output.txt
            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', start - end, 'second')
        return data




# def test():
#     source = YouTube('https://www.youtube.com/watch?v=wwnVslMwSzk')
#
#     en_caption = source.captions.get_by_language_code('a.en')
#
#     en_caption_convert_to_srt = (en_caption.generate_srt_captions())
#
#     print(en_caption_convert_to_srt)
#
# test()