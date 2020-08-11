
#todo
#videos.py
"""use for comments"""
'''use for stings'''
"""
This module contains all video types



This module navigation
In the end of most important code strings is comment in format
    #  Use '*****' for search
It means that you can use ***** in code search
if you want to go to desired string



Idea:
    # 1) Create video.
    video = ... # creating video  #  Use 'HglSFYJDDE' for search

    # 2)
    stream = VideoStream(video, width, height)
    
    # 3) When you need get next n seconds of result video.
    stream.save_n_seconds(start_time, n, outputname):
    # in file named output_name_withonut_extension.mp4 yours video part
    # in file named output_name_withonut_extension.mp3 yours audio part
                 #
    ############### OR #####################
                 #
    stream.save_part(start_time, end_time, outputname):
    # save frames of video[start_time: end_time] in outputname + ".mp4"
    # save sound of video[start_time: end_time] in outputname + ".mp3"
    
    <!!!>You can send it to your server or do with it whatever you want</!!!>



Creating video: #  Use 'HglSFYJDDE' for search
You can create this types of video
    VideoFromYoutubeURL   #  Use 'j7ItYy3N2n' for search
    VideoFromImageURL     #  Use 'fjR1wW8o9d' for search
    VideoFromText         #  Use '55FPkUD5WO' for search

    SumOfVideo               # or video1 + video2 #  Use '0kxprGdgk8' for search
    SeparatedVideoAndAudio   # or video1 / video2 #  Use 'iPgx8iCcdC' for search
    PartOfVideo                  #  Use '1U9YldMWW2' for search
    SmartAcceleratedVideo        #  Use '89FAQvklsC' for search

#Import:
from videos import VideoFromYoutubeURL, VideoFromImageURL, VideoFromText
# from videos import (SumOfVideo, SeparatedVideoAndAudio,
#                     PartOfVideo, SmartAcceleratedVideo)


horror = VideoFromYoutubeURL("https://www.youtube.com/watch?v=qiZLHchtX8c")
#  Use 'j7ItYy3N2n' for search
#  __init__ args:  link or video_id
# it is the same               video_id
horror = VideoFromYoutubeURL("qiZLHchtX8c")

# you can cut a part from video using
horror_11s = horror[239:250]
# it is the same
# horror_11s = PartOfVideo(horror, 239, 250)


# You can set **kwargs that in Settings:
# brightness, speed, volume and max_volume and e.c.t.
# like this.
rev9_8s = VideoFromYoutubeURL("2WemzwuAQF4")[56: 64](speed=0.9, volume=1.2)
rev9_3s = VideoFromYoutubeURL("2WemzwuAQF4")[66: 69](speed=0.9, volume=1.2)
# it is the same
# rev9_3s = SmartAcceleratedVideo(VideoFromYoutubeURL("2WemzwuAQF4")[66: 69],
#                                 Settings(speed=0.9, volume=1.2))

# You can contencate videos.   #  Use '0kxprGdgk8' for search
rev9_11s = rev9_8s + rev9_3s  # in "2WemzwuAQF4" will skipped 64-66
# it is the same rev9_11s = SumOfVideo(rev9_8s, rev9_3s)


# and you can also separate_video and audio
                    # video        audio
sep_video_an_audio = rev9_11s / horror_11s
# it is the same
# rev9_11s = SeparatedVideoAndAudio(rev9_11s, horror_11s)


# VideoFromImageURL exmple    #  Use 'fjR1wW8o9d' for search
image_url = r"https://i.ibb.co/2K5q1y3/image.png"
image_10s = VideoFromImageURL(image_url, 10) # video duration; without sounds

#you can add sound using
image_with_sound_10s = image_10s / VideoFromYoutubeURL("7oEdx9IgPpo")[0: 10]


# VideoFromText exmple    #  Use '55FPkUD5WO' for search
text_8s = "Any text"
text_8s = VideoFromText("Any Text", 10)  #without sounds

#you can add sound using
text_with_sound_8s = text_8s / VideoFromYoutubeURL("7oEdx9IgPpo")[10: 18]



classes tree:
│
├moviepy.editor.VideoFileClip══╗
│                              ║
├Video┐                        ║    #  Use 'POFvmLHWHg' for search
│ '''if isistance(v1, Video) and isistance(v2, Video) then'
│    v1[start_time:end_time] = PartOfVideo(v1, start_time, end_time) 
│    v1(**kwargs) = SmartAcceleratedVideo(v1, Settings(kwargs))
│    v1 + v2 = SumOfVideo((v1, v2))
│    v1 / v2 = SeparatedVideoAndAudio(video=v1, audio=v2)
│ '''┌┘                        ║
│    │                         ║
│    ├─VideoFromYoutubeURL═════╝    #  Use 'H6R9gbClEg' for search  
│    │                              
│    ├─VideoFromImage               #  Use 'hDygGaJlAH' for search   
│    │     │
│    │     ├────VideoFromText       #  Use 'Pv1U9ovsOb' for search
│    │     │
│    │     ├────VideoFromImageURL   #  Use 'f5vfFwOTVd' for search
│    │     │
│    │     └────VideoFromFrameFromYoutubeVideo═════╗
│    │                              #  Use 'hBavQ96HNM' for search
│    │
│    ├─PartOfVideo                  #  Use '1U9YldMWW2' for search            
│    │
│    ├─SmartAcceleratedVideo        #  Use '89FAQvklsC' for search
│    │     
│    ├─SeparatedVideoAndAudio       #  Use '0uceFGY5J0' for search   
│    │                               
│    └─SumOfVideo                   #  Use 'Ci1lua3fAb' for search  
│
└VideoSaveStream               #  Use 'FwLJImGxRF' for search

To check whether 'obj' is a video use isinstance(obj, Video)

"""



from moviepy.editor import VideoFileClip
from moviepy.audio.AudioClip import AudioArrayClip
from cv2 import VideoWriter
from settings import Settings
from pafy import new as pafy_new
from functions import (in_new_thread, str_to_error_message, get_stream_url,
                       print_time, squeeze_sound, image_to_new_size)
from filedict import FileDict
import numpy as np
from bisect import bisect_right
from PIL import Image
from urllib.request import urlopen


constants = FileDict("constants")
AUDIO_FPS = constants.get_and_write("AUDIO_FPS", 44100)
VIDEO_FPS = constants.get_and_write("VIDEO_FPS", 25)
# print(VIDEO_FPS)

class Video:    #  Use 'POFvmLHWHg' for search
    """
    Base video class.
    Contain 
        v1[start_time:end_time] = PartOfVideo(v1, start_time, end_time) 
        v1(**kwargs) = SmartAcceleratedVideo(v1, Settings(kwargs))
        v1 + v2 = SumOfVideo((v1, v2))
        v1 / v2 = SeparatedVideoAndAudio(video=v1, audio=v2).
    
    All classes inherid of <class Video> must overload
        'get_nextsound(time)' method #  Use 'mrQvXrhkKg' for search
        'get_frame(time)'     method #  Use '0t1SPHSW8B' for search
        'get_duration(time)'         #  Use 'Ani5kkF30f' for search
            If you want to use SumOfVideo of your type
            !!! if you use SumOfVideo(your_type[start:end]) you don't need
            overload it becouse PartOfVideo have own 'get_duration' method.
    
    """
    def __add__(self, other):
        return SumOfVideo((self, other))

    def __truediv__(self, other):
        return SeparatedVideoAndAudio(self, other)

    def __getitem__(self, arg):
        """
        return PartOfVideo(self, arg.start, arg.stop) if arg is slice
        return self.get_frame(arg) if arg is float
        """
        if isinstance(arg, slice):
            return PartOfVideo(self, arg.start, arg.stop)
        elif isinstance(arg, (int, float)) and not isinstance(arg, bool):
            return self.get_frame(arg)

    def __call__(self, *args, **kwargs):
        """
        Create SmartAcceleratedVideo(self, Settings(**dict)) where 'dict' is
            if not args:
                dict = kwargs
            if args is (settings_obj):
                dict = settings_obj.to_dict().update(kwargs)        
        """
        if not args:
            settings_dict = kwargs  
        elif len(args) == 1 and isinstance(args[0], Settings):
            settings_dict = args[0].to_dict()
            settings_dict.update(kwargs)
        elif len(args) == 1:
            msg = '''arg in Video(arg, **kwargs) must be <class Settings>
                    type type({}) = {} were given'''.format(arg, type(arg))
            raise TypeError(str_to_error_message(msg))
        else: 
            msg = '''Video(*args, **kwargs) takes 0 or 1 argument in *args
                     Video(*{}, **{}) were given'''.format(args, kwargs)
            raise TypeError(str_to_error_message(msg))

        return SmartAcceleratedVideo(self, Settings(**settings_dict))
            

    def get_nextsound(self, *args, **kwargs): #  Use 'mrQvXrhkKg' for search
        """
        Overloaded 'get_nextsound(self, time)' method must generate
        chunk of video after 'time'.
        This function must
            1) takes time in arg (def get_nextsound(self, time))
             
            2) create dict 'part' in format
                   part['end time'] = time of end of chunk
                   part['sound'] = np.ndarray of sound

            3) return part
        """
        msg = '''All classes inherited of {} must overload '{}' method;
                 #  Use 'mrQvXrhkKg' for search in videos.py'''
        msgstr_to_error_message(msg.fotmat(__class__, "get_nextsound"))
        raise Exception(msg)
    
    def get_frame(self, *args, **kwargs): #  Use '0t1SPHSW8B' for search
        """
        Overloaded 'get_frame' method must takes time in arg 
        and return frame in that time.
        """
        msg = '''All classes inherited of {} must overload '{}' method;
                 #  Use '0t1SPHSW8B' for search'''
        msg = str_to_error_message(msg.fotmat(__class__, "get_frame"))
        raise Exception(msg)

    def get_duration(self):       #  Use 'Ani5kkF30f' for search
        """
        Function that return duration of video.
        You need overload it if you use SumOfVideo for your type
        You no need overload it if you use SumOfVideo for
        PartOfVideo of your type. (PartOfVideo have get_duration method)"""
        msg = '''You call {}.get_duration() (may be in SumOfVideo(v1, v2)
                 or v1 + v2) method but not overload it'''
        AttributeError(str_to_error_message(msg.format(self)))

    def check_time_decorator(func):
        def rt(self, time):
            if time > self.get_duration():
                err = '''you ask about {} but {}.get_duration() is {}'''
                raise OSError(err.format(time, self, self.get_duration()))
            return func(self, time)
        return rt


class VideoFromYoutubeURL(VideoFileClip, Video):     # Use 'H6R9gbClEg' for search
    """
    VideoFromYoutubeURL let get video form YouTube
    
    __init__ argumnts:
    ----short_link - link like 'https://www.youtube.com/watch?v=2WemzwuAQF4'
                     or only video id ('2WemzwuAQF4')
    ----start_time - time in seconds    (float)
    ----end_time - time in seconds    (float)
    ----settings=Settings() - settings for video

    """
    def __init__(self, short_link, duration=-1):
        def get_id(url):
            if not url.startswith("http"):
                return url
            from urllib.parse import urlparse, parse_qs          
            """
            tooked from
            https://stackoverflow.com/questions/45579306/get-youtube-video-url-or-youtube-video-id-from-a-string-using-regex
            look it for more info
            """
            u_pars = urlparse(url)
            quer_v = parse_qs(u_pars.query).get('v')
            if quer_v:
                return quer_v[0]
            pth = u_pars.path.split('/')
            if pth:
                return pth[-1]

        self.video_id = get_id(short_link)
        self.duration = -1
        self.__name__ = self.video_id
        
        self.is_downloaded = False
        self.start_downloading = False
        
    # @print_time
    def download_webm(self):
        """
        This function uploading video (after this function video will load).
        If video has already uploaded this funtion does nothing.
        """
        if self.is_downloaded:
            return
        if self.start_downloading and not self.is_downloaded:
            import time
            while not self.is_downloaded:
                time.sleep(0.01)
            return
                
        self.start_downloading = True
        # loading
        n = 10
        for i in range(n):
            try:
                link = r"https://www.youtube.com/watch?v=" + self.video_id
                super().__init__(get_stream_url(link))
                break
            except OSError as e:
                if i == n - 1:
                    raise e
            print("attemp {}: failed. Start {} attemp".format(i, i + 1))
        if i:
            print("Video sucsessfuly uploaded in {} attemps".format(i))

        self.audio = self.audio.set_fps(AUDIO_FPS)
        self.is_downloaded = True
        self.start_downloading = False

    def _download_webm_decorator(func):
        def wrapper(self, *args, **kwargs):
            self.download_webm()
            return func(self, *args, **kwargs)
        return wrapper

    @_download_webm_decorator
    def get_frame(self, t):
        t = self.get_frame_time(t)
        """if self._get_downloaded_status() == "downloading don't started":
            self._start_downloading_webm()
        elif self._get_downloaded_status() == "now downloading":
            import time
            while self._get_downloaded_status != "downloaded":
                time.sleep(0.01)"""
        return super().get_frame(t) 

    def get_frame_time(self, time):
        return time - time % (1 / VIDEO_FPS)

    @_download_webm_decorator
    def get_nextsound(self, time):     
        end_time = time + 1 / VIDEO_FPS
        self.last_asked_time = end_time
        
        part = {}
        part['end time'] = end_time
        part['sound'] = self.audio.subclip(time, end_time).to_soundarray()
        return part

    def get_duration(self):
        if self.duration == -1:
            try:
                super(Video, self).get_duration()
            except AttributeError as e:
                msg = ''' .But you don't point out duration in
                         {}.__init__({}, {}). It trror may be raised if int
                         SumOfVideo previos video have small duration and
                         this video didn't have time to download.
                      '''.format(__class__, self, self.video_id)
                raise AttributeError(str(e) + msg)

        return self.duration


class PartOfVideo(Video):             #  Use '1U9YldMWW2' for search
    """
    part = PartOfVideo(your_video, start_time, end_time)  # or
    part = your_video[start_time:end_time]

    Create part of your video between start_time and end_time.
        (PartOfVideo.get_frame and PartOfVideo.get_nextsound use your_video
        methods takes into time range
    PartOfVideo have own get_duration() method so if you use
    SumOfVideo(video1[start1:end1], video2[start1:end1]) video1 and video2
    don't have to overload get_duration method
    """
    
    def __init__(self, video, start_time, end_time):
        self.video = video
        self.start_time, self.end_time = start_time, end_time

    @Video.check_time_decorator   
    def get_nextsound(self, time):
        part = self.video.get_nextsound(self.start_time + time)
        part['end time'] -= self.start_time
        return part

    @Video.check_time_decorator
    def get_frame(self, time):
        return self.video.get_frame(time + self.start_time)

    def get_duration(self):
        return self.end_time - self.start_time


class SmartAcceleratedVideo(Video):   #  Use '89FAQvklsC' for search
    """
    Video that plays the silent and loud parts at different speeds.
    Look <class Settings> for info about options
    """
    def __init__(self, video, settings):
        self.video = video
        self.settings = settings
        self.last_loud_time = -10 ** 10

    def get_nextsound(self, time):
        s = self.settings
        # print(s)
        
        part = self.video.get_nextsound(time)
        sound = part['sound']
        cur_max = sound.max()
        
        if cur_max > s.get_sound_threshold() or self.last_loud_time > time:
            self.last_loud_time = time
        if time - self.last_loud_time < s.get_min_quiet_time():
            k = s.get_loud_speed() * s.get_global_speed()
            sound = sound * s.get_loud_volume_cooficient()
        elif time - self.last_loud_time > s.get_max_quiet_time():
            k = 10 ** 10
        else:
            k = s.get_quiet_speed() * s.get_global_speed()
            sound = sound * s.get_quiet_volume_cooficient()
            # print("k", k)
        k = abs(k) if k else 1
            
        sound = squeeze_sound(sound, k)
        sound = np.minimum(sound, s.get_max_volume())
        sound = np.maximum(sound, -s.get_max_volume())
        sound = np.float32(sound * s.get_volume_cooficient())
        return {'end time': part['end time'], 'sound': sound}

    def get_frame(self, time):
        im = self.video.get_frame(time) # * self.settings.get_brightness()
        for i in range(self.settings.get_rotate_image() % 4):
            im = np.transpose(im, (1, 0, 2))
            im = im[::-1]
        if self.settings.get_inverted():
            im = im[::-1]
        return im
    
    def get_duration(self):
        return self.video.get_duration()


class VideoFromImage(Video):          #  Use 'hDygGaJlAH' for search
    """
    VideoFromImage(image, duration) create Video object
    of duration 'duration' with a constant image 'image' 
    """
    def __init__(self, image, duration, sound_channels=2):
        self.image = image
        self.duration = duration
        self.sound_channels = sound_channels

    @Video.check_time_decorator
    def get_nextsound(self, t):
        part = {}
        part['end time'] = t + self.get_duration()
        
        sound = np.zeros(self.get_duration() * AUDIO_FPS * self.sound_channels)
        part['sound'] = sound.reshape((-1, self.sound_channels))
        return part
    
    @Video.check_time_decorator
    def get_frame(self, t):
        return self.image
    
    def get_duration(self):
        return self.duration


class VideoFromText(VideoFromImage):       #  Use 'Pv1U9ovsOb' for search
    pass


class VideoFromImageURL(VideoFromImage):   #  Use 'hDygGaJlAH' for search
    def __init__(self, image_link, duration, sound_channels=2):
        im = Image.open(urlopen(image_link))
        # im.show()
        ndarr = np.array(im)
        super().__init__(ndarr, duration, sound_channels)


class VideoFromFrameFromYoutubeVideo(VideoFromImage):
                                           #  Use 'hBavQ96HNM' for search 
    pass


class SumOfVideo(Video):              #  Use 'Ci1lua3fAb' for search
    """
    sum_video = SumOfVideo((video_1, video_2, ...))   # or
    sep = video_1 + video_2    # if frames_video and sound_video inhired
                               # of <class Video>
    Play video_1 after that play video_2 after that play video_3 and e.c.t.
    It loading video_i in correct time
    """
    PRELOAD = constants.get_and_write("SumOfVideo.PRELOAD", 10)
    def __init__(self, videos_list):
        self.videos_list = videos_list
        self.is_video_load = [False] * len(videos_list)
        self.durations = [elem.get_duration() for elem in videos_list[:-1]]
        self.duration = "look SumOfVideo.get_duration"
        self.start_times = [0]
        for elem in self.videos_list[:-1]:
            self.start_times.append(self.start_times[-1] + elem.get_duration())
        self.is_downloaded = [False] * len(videos_list)
        # print(self.durations)


    @Video.check_time_decorator
    def _get_index_and_time(self, time):
        index = bisect_right(self.start_times, time) - 1
        time_in_video = time - self.start_times[index]
        return index, time_in_video

    def set_users_cur_viewing_time(self, index, video_time):
        def load_video(self, index):
            self.is_video_load[index] = True
            self.videos_list[index].get_frame(0)
        # set_time(self, index, video_time)
        for index1 in range(index + 1, len(self.videos_list)):
            if self.start_times[index1] < video_time + SumOfVideo.PRELOAD and \
                       not self.is_video_load[index1]:
                in_new_thread(lambda : load_video(self, index1))()
            else:
                break
    
    @Video.check_time_decorator
    def get_frame(self, time):
        index, video_time = self._get_index_and_time(time)
        self.set_users_cur_viewing_time(index, video_time)
        # print(index, video_time)
        return self.videos_list[index].get_frame(video_time)

    @Video.check_time_decorator
    def get_nextsound(self, time):
        index, video_time = self._get_index_and_time(time)
        try:
            part = self.videos_list[index].get_nextsound(video_time)
        except OSError:
            part = self.videos_list[index + 1].get_nextsound(0)
        part['end time'] += -video_time + time
        return part

    def get_duration(self):
        if self.duration != "look SumOfVideo.get_duration":
            return self.duration
        self.duration = sum(self.durations) + self.videos_list[-1].get_duration()
        return self.duration

    
class SeparatedVideoAndAudio(Video):  #  Use '0uceFGY5J0' for search
    """
    sep = SeparatedVideoAndAudio(frames_video, sound_video)   # or
    sep = frames_video / sound_video   # if frames_video and sound_video
                                       # inhired of <class Video>
    Take frames from frames_video and sound from sound_video
    If frames_video and sound_video have different duration, frames
    Video will be add with last frame of frames_video to sound_video.duration()
    """
    def __init__(self, frames_video, sound_video):
        self.frames_video = frames_video
        self.frames_video_duration = self.frames_video.get_duration()
        self.sound_video = sound_video

    @Video.check_time_decorator
    def get_nextsound(self, time):
        # print(self.sound_video, self.sound_video.get_nextsound(time))
        return self.sound_video.get_nextsound(time)

    @Video.check_time_decorator
    def get_frame(self, time):
        time = min(time, self.frames_video_duration)
        return self.frames_video.get_frame(time)

    def get_duration(self):
        return self.sound_video.get_duration()


class VideoSaveStream:          #  Use 'FwLJImGxRF' for search
    """
    VideoSaveStream - Stream for saving video.
    Syntaxis:
        stream = VideoSaveStream(video, width, height)
        
        # for saving next n seconds
        stream.save_next(seconds, outputname)
        # outputname should be without extension
        # save frames of next n seconds in outputname + ".mp4"
        # save sound of next n seconds in outputname + ".mp3"

    Public methods:  (all methods return nothing)
        __init__(video):

        save_n_seconds(start_time, n, outputname):
        # save frames of next n seconds in outputname + ".mp4"
        # save sound of next n seconds in outputname + ".mp3"
                 #
        ############### OR #####################
                 #
        save_part(start_time, end_time, outputname):
        # save frames of video[start_time: end_time] in outputname + ".mp4"
        # save sound of video[start_time: end_time] in outputname + ".mp3"
        
    """
    def __init__(self, video, width=-1, height=-1):
        if not isinstance(video, Video):
            msg = '''VideoStream.__init__  argument must be inherit of
                     Video, type({}) = {} were given'''
            raise TypeError(msg.format(video, type(video)))

        self.video = video
        frame = self.video.get_frame(0)  # loading
        self.w = width if width != -1 else frame.shape[1]
        self.h = height if height != -1 else frame.shape[0]
        self.video.get_nextsound(0)

    @print_time
    def _save_part(self, start_time, outputname,
                   condition="cur_time < end_time"):
        def check_type(part):
            nessery_keys = ['sound', 'end time']
            if not isinstance(part, dict):
                msg = '''Video.get_nextsound must return 'dict' argument,
                      type({}) = {} were given'''.format(part, type(part))
                raise TypeError(str_to_error_message(msg))
            for key in nessery_keys:
                if not key in part:
                    msg = '''VideoStream.get_nextsound argument must contain {}, 
                          {} were given'''.format(key, part)
                    raise TypeError(str_to_error_message(msg))
            return True

        videoname, audioname = outputname + ".mp4", outputname + ".mp3"
        videowriter = VideoWriter(videoname, -1, VIDEO_FPS, (self.w, self.h))
        sound = []
        sound_len, frames_len = 0, 0
        cur_time = start_time
        cur_frame = self.video.get_frame(cur_time)
        rt = 0
        while eval(condition):
            # time.sleep(0.01)
            part = self.video.get_nextsound(cur_time)
            check_type(part)

            sound.append(part['sound'])
            sound_len += len(sound[-1])
            if sound_len / AUDIO_FPS > frames_len / VIDEO_FPS:
                cur_frame = image_to_new_size(cur_frame, self.w, self.h)
                cur_frame = cur_frame[:, :, ::-1]
            while sound_len / AUDIO_FPS > frames_len / VIDEO_FPS:
                frames_len += 1
                videowriter.write(cur_frame)
            cur_time = part['end time']
            cur_frame = self.video.get_frame(cur_time)
            # print(cur_time)
        videowriter.release()
        sound = np.vstack(sound)
        AudioArrayClip(sound, AUDIO_FPS).write_audiofile(audioname, logger=None)             

    def save_part(self, start_time, end_time, outputname):
        """
        Save video[start_time: end_time] in outputname:
            In outputname.mp4 save frames of video
            In outputname.mp3
        """
        self._save_part(start_time, outputname, "cur_time < "+ str(end_time))

    def save_n_seconds(self, start_time, n, outputname):
        self._save_part(start_time, outputname, "sound_len < AUDIO_FPS * " + str(n))

import time
#t = time.time()
at, cur_time = [0] * 20, time.time()
def print_time(i):
    global at, cur_time
    # print(time.time() - t, i)
    #if i == 1:
    #    print(at, bt, time.time())
    at[i] += time.time() - cur_time
    cur_time = time.time()
    
#"""
def main0(i):    
    rev9_url = r"https://www.youtube.com/watch?v=2WemzwuAQF4" #t=56s"
    rev9_8s = VideoFromYoutubeURL(rev9_url)[56: 64]
    rev9_3s = VideoFromYoutubeURL(rev9_url)[66: 69]
    horror_url = r"https://www.youtube.com/watch?v=qiZLHchtX8c"
    horror_8s = VideoFromYoutubeURL(horror_url)[239:247]
    horror_11s = VideoFromYoutubeURL(horror_url)[239:250]

    # print(dir(rev9_8s))
    video = (rev9_8s + rev9_3s) / horror_11s
    stream = VideoSaveStream(video)
    #import time
    #t = time.time()
    stream.save_part(0, 5, "outname0-5")
    stream.save_part(0, 5, "outname5-10")
    print("---------------------------------" + str(i))
    #print(time.time() - t)

def main1(i):
    im_urls = []
    im_urls += [r"https://img1.goodfon.ru/original/2048x2048/3/da/dubai-city-skyscrapers.jpg"]
    im_urls += [r"https://i.pinimg.com/736x/42/5c/c6/425cc6264e40b0956322c94af5a447b9.jpg"]
    im_urls += [r"https://img3.goodfon.ru/original/1680x1050/c/2d/kuala-lumpur-malayziya-kuala.jpg"]
    im_urls += [r"https://mirpokrytij.ru/upload/iblock/83c/83c06d6848db17f5068a79f2cbc38ab1.jpg"]

    video = SumOfVideo([VideoFromImageURL(elem, 2) for elem in im_urls])
    stream = VideoSaveStream(video, 1700, 1000)
    stream.save_part(0, 8, "cities")
    
def main2(i):
    video_id = "V1sRabJhGWs"
    video = VideoFromYoutubeURL(video_id)

    settings = Settings(min_quiet_time=0.3,
                        sound_threshold = 0.2,
                        quiet_speed = 6)
    sva = video(settings)
    w, h = video.get_frame(0).shape[1], video.get_frame(0).shape[0]
    stream = VideoSaveStream(sva, w, h + 100)
    stream.save_n_seconds(0, 30, "sva_output0-30")
    
# print(time.time() - t)
#for _ in range(100):
main2(0)
