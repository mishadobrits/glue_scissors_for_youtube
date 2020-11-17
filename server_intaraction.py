from videos import VideoSaveStream, VideoFromYoutubeURL
from functions import in_new_thread

ALPHABET = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

"""
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
"""


class UserProcessing:
    def __init__(self, video_string, folder, chunk=5, video_extension="mp4"):
        self.video_string = video_string
        self.folder, self.chunk = folder, chunk
        self.stopped, self.closed = False, False
        self.cur_time = 0
        self.video_format = video_extension

        self.process_str(folder, chunk=chunk, format=video_extension)

    @in_new_thread
    def process_str(self, folder, chunk=5, format="mp4"):
        import os
        try:
            os.stat(folder)
        except:
            os.makedirs(folder)

        stream = VideoSaveStream(eval(self.video_string), format=format)
        self.cur_time, file_counter = 0, 0
        dur = stream.video.get_duration()
        while self.cur_time < dur - chunk and not self.closed:
            # print(f"Writing... {it}, {it + chunk}, {folder}, {file_counter}")
            file_counter = stream.save_part(self.cur_time, self.cur_time + chunk, folder, file_counter)
            self.cur_time += chunk

        if self.cur_time != dur and not self.closed:
            stream.save_part(self.cur_time, dur, folder, file_counter)  # print(f"last {it, dur}")

        print(f"Task '{self.video_string}' successfully completed")

    def set_cur_time(self, cur_time):
        self.cur_time = cur_time

    def close(self):
        self.closed = True
        print(f"{self} closed, {self.closed}")

    def is_closed(self):
        return self.closed


# r"""
def bad_code_read_one_line_from_test_txt_and_process_it(name="108"):
    with open("test.txt") as f:
        s = f.readline()
    print(f"S: {s}")
    folder = "video/{}/".format(name)
    print(folder)
    UserProcessing(s, folder, chunk=5 * 60 * 60, video_extension="avi")


def start_interaction_with_server():
    users_dict = {}
    while True:
        try:
            with open("site_to_accelerator.txt", "r") as f:
                lines = f.readlines()
            with open("site_to_accelerator.txt", "w") as f:
                f.write("")
        except PermissionError:
            continue

        for line in lines:
            if line == "STOP_THE_PY_FILE":
                for user in users_dict:
                    users_dict[user].close()
                exit()

            splitted_line = list(line.split())
            if not splitted_line:
                continue
            if len(splitted_line) == 1:
                print(f"len(l) = len({splitted_line}) = {len(splitted_line)} - bad")
                continue

            user_id, command, argument = splitted_line[0], splitted_line[1].lower(), " ".join(splitted_line[2:])
            print(f"See 'user_id': {user_id}, 'command': {command}, argument: {argument}")

            if command == "new":
                users_dict[user_id] = UserProcessing(argument, f"video/{user_id}/")

            if command == "close":
                if user_id not in users_dict:
                    continue
                users_dict[user_id].close()

            if command == "set_time":
                if user_id not in users_dict:
                    continue
                for elem in u"бю/?,":
                    argument = argument.replace(elem, ".")
                try:
                    time = float(argument)
                except ValueError:
                    continue
                users_dict[user_id].set_cur_time(time)


# if you want to start interaction with server use
# start_interaction_with_server()
# elif you want accelerate one video and save it
bad_code_read_one_line_from_test_txt_and_process_it(name="109")

