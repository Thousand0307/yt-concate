from moviepy.editor import VideoFileClip, concatenate_videoclips

from yt_concate.pipeline.steps.step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_captions_time(found.time)
            print('++++++++++++++++++', start, end)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)

    def parse_captions_time(self, captions_time):
        start, end = captions_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self,tim_str):
        h, m, s = tim_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000


