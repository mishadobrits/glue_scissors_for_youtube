from videos import VideoFromYoutubeURL, VideoFromText, SumOfVideo, VideoSaveStream
from time_converter import convert_times_in_comment


def generate_sum_of_topology_videos(list_of_urls):
    videos_list = [VideoFromYoutubeURL(elem) for elem in list_of_urls]

    t = 0
    def time_to_str(seconds):
        s = int(seconds)
        h, m, s = s // (60 * 60), (s // 60) % 60, s % 60
        return f"{str(h) + ':' if h else ''}{m}:{s}"

    time_comment = ""
    for i, elem in enumerate(videos_list):
        s = f"{time_to_str(t)} - ({i + 1}) - https://youtu.be/{elem.video_id}"
        time_comment += s + "\n"
        t += elem.get_duration() + 3

    # """
    videos_list = [elem(sound_threshold=0.03, quiet_volume_coefficient=0.04, min_quiet_time=0.2, volume_coefficient=1.2,
                        max_quiet_time=4.5) for elem in videos_list]
    text = u"Конец этой части\nСледущая часть начнётся в течение\n3 секнунд"
    shape = videos_list[0].get_frame(0).shape
    sep_video = VideoFromText(text, 3, bg="black", fg="white", width=shape[1], height=shape[0])

    print(shape == sep_video.get_frame(0).shape)

    rt = SumOfVideo([elem + sep_video for elem in videos_list])
    print(rt.get_duration())
    VideoSaveStream(rt, format="avi").save_part(0, rt.get_duration(), "video/108/", 0)  # """
    print(convert_times_in_comment(time_comment, "video/108/0.time_converting"))


"""
You can specify any array of [correct] links
Program will merge its with seperated video with text 'next video is starting in next 3 second'
"""

a = ['https://youtu.be/nlC-v3dxqDE',
     'https://youtu.be/X4UIb5gHIc4',
     'https://youtu.be/9MP2fd4jM2o']

generate_sum_of_topology_videos(a)
