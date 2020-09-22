import videos
from videos import (VideoFromYoutubeURL, VideoFromImageURL, VideoFromText,
                    VideoFromFrameFromYoutubeVideo, VideoSaveStream)
from filedict import FileDict
from functions import in_new_thread


def brakes_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return "(" + res + ")"
    return wrapper


# @brakes_decorator
def to_url(video):
    if type(video) == videos.VideoFromYoutubeURL:
        return f"'{video.video_id}'"
    elif type(video) == videos.PartOfVideo:
        return to_url(video.video)+f"[{video.start_time}: {video.end_time}]"
    elif type(video) == videos.SumOfVideo:
        rt = "+".join([to_url(elem) for elem in video.videos_list])
        return rt
    elif type(video) == videos.PartsOfOneVideo:
        rt = to_url(video.video) + '['
        rt += ", ".join(f"{s.start}: {s.stop}" for s in video.slices_list)
        return rt + ']'
    elif type(video) == videos.SeparatedVideoAndAudio:
        return f"{to_url(video.frames_video)} / {to_url(video.sound_video)}"
    elif type(video) == videos.SmartAcceleratedVideo:
        return "(" + to_url(video.video) + ")" + str(video.settings)[8:]

    
def video_from_very_short_str(string):
    it = 0   # iterator
    operators_info = {"+": {"operands_numb": 2, "priority": 1},
                      "*": {"operands_numb": 2, "priority": 2},
                      "/": {"operands_numb": 2, "priority": 2}}
    stack = ["end"]
    while it < len(s):
        if string[it] == "'":
            new_it = string[it:].find("'") + 1
            video_id = string[i: new_it]
            stack.append(videos.VideoFromYoutubeURL(video_id))
            it = new_it
        elif string[it] == '"':
            new_it = string[it:].find('"') + 1
            image_link = string[i: new_it]
            stack.append(videos.VideoFromImageURL(image_link))
            it = new_it
        elif string[it] == "[":
            new_it = string[it:].find("]") + 1
            slices = list(string[i: new_it].split(","))
            slices = [list(map(float, elem.split(":"))) for elem in slices]
            slices = [slice(*elem) for elem in slices]
            stack[-1] = stack[-1][slices]
            it = new_it
        elif 1:
            pass

@in_new_thread
def process_str(s, folder, chunk=5):
    import os
    try:
        os.stat(folder)
    except:
        os.makedirs(folder)

    stream = VideoSaveStream(eval(s))
    it, file_counter = 0, 0
    dur = stream.video.get_duration()
    while it < dur - chunk:
        # print(f"Writing... {it, it + chunk, folder, file_counter}")
        file_counter = stream.save_part(it, it + chunk, folder, file_counter)
        # file_counter -= 1
        it += chunk

    if it != dur:
        # print(f"last {it, dur}")
        stream.save_part(it, dur, folder, file_counter)
    print(f"Task '{s}' sucssesfully completed")


def bad_code_read_one_line_from_test_txt_and_process_it():
    with open("test.txt") as f:
        s = f.readline()
    print(s)
    # s = f"VideoFromYoutubeURL('KWbANha2iws')[71:77] + VideoFromImageURL('{image_url}', 7)"
    name = "108"
    folder = r"C:\Users\m\Desktop\PythonProjects\YouTube_GlueAndScissors\Code\glue_scissors_for_youtube\video\{}/".format(name)
    print(folder)
    process_str(s, folder, chunk=30 * 60)


bad_code_read_one_line_from_test_txt_and_process_it()

# r"""
# image_url = r"https://img2.akspic.ru/image/88423-burdzh_halifa-neboskreb-vyshka-zdanie-liniya_gorizonta-1920x1200.jpg"
# s = "VideoFromYoutubeURL('2WemzwuAQF4')[56: 63, 66: 69]/ VideoFromYoutubeURL('qiZLHchtX8c')[239:249](volume_cooficient = 1.2)"
# s = r"VideoFromText('Подборка самых\nжизненных фраз\nOneTwo', 3) + VideoFromYoutubeURL('KWbANha2iws')[307:309, 307:309:0.66](volume_cooficient=0) + VideoFromYoutubeURL('KWbANha2iws')[71:77] + VideoFromYoutubeURL('U3-6jv0NCkk')[206:212] +  VideoFromYoutubeURL('A8Fon7DWho4')[65:69]"
 # """

"""
temp = videos.VideoFromYoutubeURL('V1sRabJhGWs')
v1 = temp[0:10, 15:20]
v2 = temp[0:10]
v3 = v1 + v2
v4 = v3 / temp[0:25]
v5 = v4(volume_cooficient=0)
for v in [v1, v2, v3, v4, v5]:
    # print(v.short_str())
    print(to_url(v))   #https://youtu.be/1at7kKzBYxI """
