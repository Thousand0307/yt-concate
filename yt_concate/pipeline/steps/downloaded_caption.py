import time

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step, StepException


class DownLoadCaption(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print(url)
            if utils.caption_file_exist(url):
                continue
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except (KeyError, AttributeError):
                print('KeyError or AttributeError in', url)
                continue

            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', start - end, 'second')




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