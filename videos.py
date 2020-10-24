from moviepy.editor import VideoFileClip
from cv2 import VideoWriter
from settings import Settings
from functions import (in_new_thread, str_to_error_message, get_stream_url,
                       print_time, squeeze_sound, StoppableThread,
                       image_from_text, ignore_exceptions_decorator_maker)
import numpy as np
from bisect import bisect_right
from PIL import Image
from urllib.request import urlopen
import wave


# videos.py
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
    stream = VideoSaveStream(video, width, height)
    
    # 3) When you need get next n seconds of result video.
    stream.save_n_seconds(start_time, n, outputname, counter):
    # in file named output_name_withonut_extension.mp4 yours video part
    # in file named output_name_withonut_extension.mp3 yours audio part
                 #
    ############### OR #####################
                 #
    stream.save_part(start_time, end_time, outputname, counter):
    # save frames of video[start_time: end_time] in outputname + ".mp4"
    # save sound of video[start_time: end_time] in outputname + ".mp3"
    
    <!!!>You can send it to your server or do with it whatever you want</!!!>



Creating video:   #  Use 'HglSFYJDDE' for search
You can create this types of video
    VideoFromYoutubeURL   !!!!!      #  Use 'j7ItYy3N2n' for search
    VideoFromImageURL                #  Use 'fjR1wW8o9d' for search
    VideoFromText                    #  Use '55FPkUD5WO' for search
    VideoFromFrameFromYoutubeVideo   #  Use 'hBavQ96HNM' for search

    SumOfVideo             # or video1 + video2  #  Use '0kxprGdgk8' for search
    SeparatedVideoAndAudio # or video1 / video2  #  Use 'iPgx8iCcdC' for search
    PartOfVideo            # or video1[start:end]#  Use '1U9YldMWW2' for search
    VideoSettings          # or video1[kwargs]   #  Use '89FAQvklsC' for search
    PartsOfOneVideo        # or video1[slice1, slice2, ...] #  Use 'GnJ70Y0u1v' for search

#Import:
from videos import VideoFromYoutubeURL, VideoFromImageURL, VideoFromText
# from videos import (SumOfVideo, SeparatedVideoAndAudio,
#                     PartOfVideo, VideoSettings)


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
# brightness, speed, volume_cooficient and max_volume and e.c.t.
# like this.
rev9 = VideoFromYoutubeURL("2WemzwuAQF4")
rev9_8s = rev9[56: 64](speed=0.9, volume_cooficient=1.2)
rev9_3s = rev9[66: 69](speed=0.9, volume_cooficient=1.2)
# In all classes __init__ mathod copy video arguments, so in
# rev9_11s = rev9_8s + rev9_3s, rev9 woll loads twice 
# It is the same
# rev9_3s = VideoSettings(VideoFromYoutubeURL("2WemzwuAQF4")[66: 69],
#                                 Settings(speed=0.9, volume=1.2))

# You can contencate videos.   #  Use '0kxprGdgk8' for search
rev9_11s = rev9_8s + rev9_3s   # in "2WemzwuAQF4" will skipped 64-66
# it is the same rev9_11s = SumOfVideo((rev9_8s, rev9_3s))

# You also can use
rev9_11s = rev9[56: 64, 66: 69](speed=0.9, volume_cooficient=1.2)
# If you use this way (v2 = v1[st1:end1, st2:end3, st3:end3, ...])
# v1 will loads twice.

#And you can also share video and audio
                    # video        audio
sep_video_an_audio = rev9_11s / horror_11s
# It is the same
# rev9_11s = SeparatedVideoAndAudio(rev9_11s, horror_11s)


# VideoFromImageURL exmple    #  Use 'fjR1wW8o9d' for search
image_url = r"https://i.ibb.co/2K5q1y3/image.png"
image_10s = VideoFromImageURL(image_url, 10) # video duration; without sounds

#you can add sound using
image_with_sound_10s = image_10s / VideoFromYoutubeURL("7oEdx9IgPpo")[0: 10]


# VideoFromText exmple    #  Use '55FPkUD5WO' for search
text_8s = "Any text"
text_8s = VideoFromText("Any Text", 10)  # without sound

#You can add sound using
text_with_sound_8s = text_8s / VideoFromYoutubeURL("7oEdx9IgPpo")[10: 18]



Classes tree:
│
├moviepy.editor.VideoFileClip══╗
│                              ║
├Video┐                        ║    #  Use 'POFvmLHWHg' for search
│ '''if isistance(v1, Video) and isistance(v2, Video) then'
│    v1[start1:end1, start2:end2, ...] = PartsOfOneVideo(v1, slices_tuple)
│    v1[start_time:end_time] = PartOfVideo(v1, start_time, end_time) 
│    v1(**kwargs) = VideoSettings(v1, Settings(kwargs))
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
│    ├─SumOfVideo                   #  Use 'Ci1lua3fAb' for search  
│    │
│    ├─PartsOfOneVideo              #  Use 'GnJ70Y0u1v' for search
│    │     
│    ├─SeparatedVideoAndAudio       #  Use '0uceFGY5J0' for search  
│    │                               
│    └─VideoSettings                #  Use '89FAQvklsC' for search│
│          │
│          ├───SAV0                 #  Use 'uV8px2beVr' for search          
│          │
│          └─BadSAV0                # Use '9RBh009v8M' for search
│
└VideoSaveStream               #  Use 'FwLJImGxRF' for search

To check whether 'obj' is a video use isinstance(obj, Video)
Also All Video classes have __str__ method.


"""

AUDIO_FPS = 44100
VIDEO_FPS = 24
PRELOAD_FOR_SUM_OF_VIDEO = 10
WAIT_ONE_REQUEST_IN_SECONDS = 10


class Video:    # Use 'POFvmLHWHg' for search
    """
    Base video class.
    Contain 
        v1[start_time:end_time] = PartOfVideo(v1, start_time, end_time)
        v1[start1:end1, start2:end2, ...] = PartsOfOneVideo(v1, slices_tuple)
        v1 * number = v1[(:: for _ in range(n))] 
        v1 + v2 = SumOfVideo((v1, v2))
        v1(**kwargs) = VideoSettings(v1, Settings(kwargs))
        v1 / v2 = SeparatedVideoAndAudio(video=v1, audio=v2).
    
    All classes inherid of <class Video> must overload
        'get_nextsound(time)' method #  Use 'mrQvXrhkKg' for search
        'get_frame(time)'     method #  Use '0t1SPHSW8B' for search
        'get_duration(time)'         #  Use 'Ani5kkF30f' for search
            If you want to use SumOfVideo of your type
            !!! if you use SumOfVideo(your_type[start:end]) you don't need
            overload it becouse PartOfVideo have own 'get_duration' method.
    If you want to create VideoSaveStream(video)
    
    """
    def __add__(self, other):
        return SumOfVideo((self, other))

    def __truediv__(self, other):
        return SeparatedVideoAndAudio(self, other)

    def __mul__(self, other):
        if not isinstance(other, int):
            msg = f'''Video.__mul__ takes int argument{other}.
                  type({other}) = {type(other)} were given'''
            raise TypeError(msg)
        return RepeatedVideo(self, other)

    def __getitem__(self, arg):
        """
        return PartsOfOneVideo(self, arg.start, arg.stop)
                                             if args is list of slices
        return PartOfVideo(self, arg.start, arg.stop) if arg is slice
        return self.get_frame(arg) if arg is float
        """

        if isinstance(arg, slice):
            rt = PartOfVideo(self, arg.start, arg.stop)
            return rt if not arg.step else rt(global_speed=arg.step)
        elif isinstance(arg, (int, float)) and not isinstance(arg, bool):
            return self.get_frame(arg)
        elif isinstance(arg, tuple) and all(isinstance(e, slice) for e in arg):
            return PartsOfOneVideo(self, arg)
        
    def __call__(self, alg="SAV0", *args, **kwargs):
        """
        Create
            if alg == "SAV0"
                SAV0(self, VideoSettings(*args_without_sound_threshold, **kwargs), sound_threshold=0)
            ... (On this moment it is only one algorithm selecting voice from audio - SAV0)
        """
        if alg.upper() == "SAV0":
            if len(args) == 1 and isinstance(args[0], Settings):
                settings_dict = args[0].to_dict()
            elif not args:
                settings_dict = {}
            else:
                msg = '''in calling Video(alg="SAV0", *args, **kwargs): You can use
                         Video(alg="SAV0", **settings_dict) or Video(alg="SAV0", settings, **settings_dict), but
                         Video(*{}, **{}) were given'''.format(args, kwargs)
                raise TypeError(str_to_error_message(msg))

            settings_dict.update(kwargs)
            return SAV0(self, Settings(**settings_dict), settings_dict.get("sound_threshold", 0))

    def get_nextsound(self, *args, **kwargs):  # Use 'mrQvXrhkKg' for search
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
        raise Exception(str_to_error_message(msg.fotmat(__class__, "get_nextsound")))
    
    def get_frame(self, *args, **kwargs): # Use '0t1SPHSW8B' for search
        """
        Overloaded 'get_frame' method must takes time in arg 
        and return frame in that time.
        """
        msg = '''All classes inherited of {} must overload '{}' method;
                 #  Use '0t1SPHSW8B' for search'''
        msg = str_to_error_message(msg.format(__class__, "get_frame"))
        raise Exception(msg)

    def get_duration(self):       # Use 'Ani5kkF30f' for search
        """
        Function that return duration of video.
        You need overload it if you use SumOfVideo for your type
        You no need overload it if you use SumOfVideo for
        PartOfVideo of your type. (PartOfVideo have get_duration method)"""
        msg = '''You call {}.get_duration() (may be in SumOfVideo(v1, v2)
                 or v1 + v2) method but not overload it'''
        AttributeError(str_to_error_message(msg.format(self)))

    def check_time_decorator(func):
        def wrapper(self, time):
            if time > self.get_duration():
                err = f'''You ask about {time} but
                          {self.short_str()}.get_duration() is
                          {self.get_duration()}'''
                raise OSError(str_to_error_message(err))
            return func(self, time)
        return wrapper
    
    def deepcopy_video_decorator(func):
        def wrapper(self, *args, **kwargs):
            import copy
            args = list(args)
            for i, elem in enumerate(args):
                if isinstance(elem, Video):
                    args[i] = copy.deepcopy(elem)
            return func(self, *args, **kwargs)
        return wrapper

    def __str__(self):
        if "short_str" in dir(self):
            return self.short_str()
        else:
            return object.__str__(self)


Video.id = 0


class VideoFromYoutubeURL(VideoFileClip, Video):     # Use 'H6R9gbClEg' for search
    """
    VideoFromYoutubeURL let get video form YouTube
    
    __init__ argumnts:
    ----short_link - link like 'https://www.youtube.com/watch?v=2WemzwuAQF4'
                     or only video id ('2WemzwuAQF4')
    ----start_time - time in seconds    (float)
    ----end_time - time in seconds    (float)
    ----settings=Settings() - settings for video

    __init__ method doesn't load video.
    For loading video use video.get_frame(0) or video.get_nextsound(0).
    """
    def __init__(self, short_link, duration=-1):
        self.id = Video.id; Video.id += 1
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
            print("waiting")
            import time
            while not self.is_downloaded:
                time.sleep(0.01)
            return
        self.load()

    def load(self):
        self.start_downloading = True
        n = 10
        for i in range(n):
            try:
                link = r"https://www.youtube.com/watch?v=" + self.video_id
                super().__init__(get_stream_url(self.video_id))
                print(f"({self.id}): Video '{self.video_id}' successfully loaded")
                break
            except OSError as e:
                if i == n - 1:
                    raise e
            print(f"attempt {i}: failed. Start {i + 1} attempt")
        if i:
            print(f"Video successfully uploaded in {i + 1} attempts")

        self.audio = self.audio.set_fps(AUDIO_FPS)
        self.is_downloaded = True
        self.start_downloading = False

    def _download_webm_decorator(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            rt, is_func_finished = -1, False

            @ignore_exceptions_decorator_maker()
            def super_calling_func(*args, **kwargs):
                nonlocal rt, is_func_finished
                rt = func(*args, **kwargs)
                is_func_finished = True

            for attempt in range(10):
                stoppable_thread = StoppableThread(target=super_calling_func, args=args, kwargs=kwargs)
                stoppable_thread.start()
                stoppable_thread.join(WAIT_ONE_REQUEST_IN_SECONDS)
                stoppable_thread.stop()
                if is_func_finished:
                    return rt
                print(f"Asking {func.__name__}(*{args}, **{kwargs}) {attempt + 1} attempt: wait to long.", end=" ")
                print("Trying to reload video:", end=" ")
                try:
                    self.load()
                    print("Video successfully reloaded")
                except:
                    print("Video don't loaded")
                    pass
        return wrapper
    
    @_download_webm_decorator
    def get_frame(self, t):
        # print(f"asking time: {t}")
        t = self.get_frame_time(t)
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
    
    # @_download_webm_decorator
    def get_duration(self):
        if self.duration == -1:
            msg = ''' .But you don't point out duration in
                         {}.__init__({}, {}). It trror may be raised if int
                         SumOfVideo previos video have small duration and
                         this video didn't have time to download.
                      '''.format(__class__, self, self.video_id)
            raise AttributeError(str_to_error_message(msg))
        return self.duration

    def __deepcopy__(self, memo):
        return VideoFromYoutubeURL(self.video_id, self.duration)

    def short_str(self):
        return self.long_str()
        
    def long_str(self):
        msg = f'''{__class__.__name__}('{self.video_id}')'''
        return msg


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
        part['end time'] = t + 1 / VIDEO_FPS # self.get_duration()
        
        sound = np.zeros(AUDIO_FPS * self.sound_channels // VIDEO_FPS)
        part['sound'] = sound.reshape((-1, self.sound_channels))
        return part
    
    @Video.check_time_decorator
    def get_frame(self, t):
        return self.image
    
    def get_duration(self):
        return self.duration

    def short_str(self):
        return str(self)
        
    def long_str(self):
        msg = f'''{__class__.__name__}({self.image}, {self.duration},
                  sound_channels={self.sound_channels})'''
        return msg


class VideoFromText(VideoFromImage):       #  Use 'Pv1U9ovsOb' for search
    """
    Create VideoFromImage object with image with yours text
    ('text' in __init__ args)

    __init__ args, kwargs
    ----text
    ----duration
    ----args and kwargs for image_from_text from functions.py
                             #  Use '90kP2mTP9v' for search
    """
    def __init__(self, text, duration, *args, **kwargs):
        self.text, self.dur = text, duration
        self.args, self.kwargs = args, kwargs
        super().__init__(image_from_text(text, *args, **kwargs), duration)

    def short_str(self):
        args = str(self.args) if self.args else ""
        kwargs = str(self.kwargs) if self.kwargs else ""
        rt = f"{__class__.__name__}('{self.text}', {self.dur}"
        rt += ', ' if args or kwargs else ''
        rt += args + ", " if args and kwargs else "" + kwargs
        rt += ")"
        return rt

    def long_str(self):
        return self.short_str()


class VideoFromImageURL(VideoFromImage):   # Use 'f5vfFwOTVd' for search
    """
    Create VideoFromImage(image, duration) where image tooked from
    image_link URL.
    """
    def __init__(self, image_link, duration, sound_channels=2):
        from urllib.error import HTTPError
        self.image_link = image_link
        n = 10
        for attempt in range(n):
            try:
                image = Image.open(urlopen(image_link))
                break
            except HTTPError as e:
                print(f"Attempt {attempt} failed. Start attempt {attempt+1}.")
                if attempt == n - 1:
                    print(f"Image link {image_link} is incorrect or no Wi-fi")
                    raise e
        if attempt:
            print(f"Image successfully downloaded in {attempt+1} attempts")
        image_numpy_array = np.array(image)
        super().__init__(image_numpy_array, duration, sound_channels)
        
    def short_str(self):
        return str(self)
        
    def long_str(self):
        msg = f'''{__class__.__name__}({self.image_link}, {self.duration},
                  sound_channels={self.sound_channels})'''
        return msg


class VideoFromFrameFromYoutubeVideo(VideoFromImage):
    #  Use 'hBavQ96HNM' for search
    def __init__(self, video, time):
        self.time = time
        super().__init__(self, video[time])
        
    def short_str(self):
        return f"{__class__.__name__}({self.video.short_str()}, {self.time})"
        
    def long_str(self):
        return f"{__class__.__name__}({self.video}, {self.time})"


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
    @Video.deepcopy_video_decorator
    def __init__(self, video, start_time, end_time):
        self.video = video
        self.start_time = start_time if start_time else 0
        self.end_time = end_time if end_time else video.get_duration()

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
    
    def short_str(self):
        return f"{self.video.short_str()}[{self.start_time}:{self.end_time}]"
        
        # set_time(self, index, video_time)
    def long_str(self):
        rt = f'''{__class__.__name__}({self.video},
                 {self.start_time}, {self.end_time})'''
        return str_to_error_message(rt)
    

class SumOfVideo(Video):              #  Use 'Ci1lua3fAb' for search
    """
    sum_video = SumOfVideo((video_1, video_2, ...))   # or
    sep = video_1 + video_2    # if frames_video and sound_video inhired
                               # of <class Video>
    Play video_1 after that play video_2 after that play video_3 and e.c.t.
    It loading video_i in correct time
    """
    PRELOAD = PRELOAD_FOR_SUM_OF_VIDEO
    def __init__(self, videos_list, need_copy=True):
        self.need_copy = need_copy
        if need_copy:
            import copy
            self.videos_list = [copy.deepcopy(elem) for elem in videos_list]
        else:
            self.videos_list = videos_list
        self.is_video_load = [False] * len(videos_list)
        self.durations = [elem.get_duration() for elem in videos_list[:-1]]
        self.duration = "look SumOfVideo.get_duration"
        self.start_times = [0]
        for elem in self.videos_list[:-1]:
            self.start_times.append(self.start_times[-1] + elem.get_duration())
        self.is_downloaded = [False] * len(videos_list)

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
    
    def short_str(self):
        if self.need_copy:
            rt = "("
            rt += " + ".join([v.short_str() for v in self.videos_list])
            rt += ")"
            return rt
        rt = f'''{__class__.__name__}([v.short_str() for v in
                 self.videos_list], need_copy=False)'''
        return str_to_error_message(rt)
        
    def long_str(self, short=False):
        rt = f"{__class__.__name__}"
        rt += "[" + ", ".join([str(v) for v in self.videos_list]) + "]"
        if not self.need_copy:
            rt = ", need_copy=False"
        return rt + ")"


class PartsOfOneVideo(SumOfVideo):        # Use 'GnJ70Y0u1v' for search
    """
    Create sum of parts of one Video
    parts = PartsOfOneVideo(video, ((start0, end0), (start1, end1), ... ))
    parts = video[start0:end0, start1:end1, ...]
    # It is the same
    parts = video[start0:end0] + video[start1:end1] + video[start2:end2]...
    # But the second way, loads the video again and again.
    # The first one loads only twice
    """
    @Video.deepcopy_video_decorator
    def __init__(self, video, slices_list):
        self.video, self.slices_list = video, slices_list
        import copy
        video_list = []
        for i, video_slice in enumerate(slices_list):
            if i%2:
                video_list.append(video[video_slice])
            else:
                video_list.append(copy.deepcopy(video)[video_slice])
        super().__init__(video_list, need_copy=False)
    
    def short_str(self):
        rt =  f"{self.video.short_str()}["
        rt += ", ".join([f"{sl.start}: {sl.stop}" for sl in self.slices_list])
        return rt + "]"
    
    def long_str(self):
        return f"{self.video}{str(self.slices_list)}"


class RepeatedVideo(PartsOfOneVideo):
    """
    Repeat video n < MAXIMAL_N times.
    """
    MAXIMAL_N = 1000
    def __init__(self, video, n):
        self.n = n
        if n > RepeatedVideo.MAXIMAL_N:
            msg = f'n = {n} > RepeatedVideo.MAXIMAL_N = {RepeatedVideo.MAXIMAL_N}'
            raise ValueError(msg)
        super().__init__(video, tuple(slice(None) for _ in range(n)))

    def short_str(self):
        return f"{self.video.short_str()} * {self.n}"

    def long_str(self):
        return f"{__class__.__name__}({self.video.long_str()}, {self.n})"
    
                                           
class SeparatedVideoAndAudio(Video):  #  Use '0uceFGY5J0' for search
    """
    sep = SeparatedVideoAndAudio(frames_video, sound_video)   # or
    sep = frames_video / sound_video   # if frames_video and sound_video
                                       # inhired of <class Video>
    Take frames from frames_video and sound from sound_video
    If frames_video and sound_video have different duration, frames
    Video will be add with last frame of frames_video to sound_video.duration()
    """
    @Video.deepcopy_video_decorator
    def __init__(self, frames_video, sound_video):
        self.frames_video = frames_video
        self.frames_video_duration = self.frames_video.get_duration()
        self.sound_video = sound_video

    @Video.check_time_decorator
    def get_nextsound(self, time):
        return self.sound_video.get_nextsound(time)

    @Video.check_time_decorator
    def get_frame(self, time):
        time = min(time, self.frames_video_duration)
        return self.frames_video.get_frame(time)

    def get_duration(self):
        return self.sound_video.get_duration()

    def short_str(self):
        return f"{self.frames_video.short_str()}/ {self.sound_video.short_str()}"
    
    def long_str(self):
        return f"{__class__.__name__}({self.frames_video}, {self.sound_video})"

    def __str__(self):
        return self.long_str()


class VideoSettings(Video):   #  Use '89FAQvklsC' for search
    """
    Video that plays the silent and loud parts at different speeds.
    Look <class Settings> for info about options
    """
    @Video.deepcopy_video_decorator
    def __init__(self, video, settings, is_voice_func=lambda sound: True):
        self.video = video
        self.settings = settings
        self.last_loud_time = 0
        self.is_voice_func = is_voice_func

    def get_nextsound(self, time):
        s = self.settings
        
        part = self.video.get_nextsound(time)
        sound = part['sound']
        
        if self.is_voice_func(sound) or self.last_loud_time > time:
            self.last_loud_time = time
        if time - self.last_loud_time < s.get_min_quiet_time():
            k = s.get_loud_speed() * s.get_global_speed()
            sound = sound * s.get_loud_volume_cooficient()
        elif time - self.last_loud_time > s.get_max_quiet_time():
            k = 10 ** 10
        else:
            k = s.get_quiet_speed() * s.get_global_speed()
            sound = sound * s.get_quiet_volume_cooficient()
        k = abs(k)
            
        sound = squeeze_sound(sound, k)
        max_sound = min(s.get_max_volume(), 1)
        sound = np.maximum(np.minimum(sound, max_sound), -max_sound)
        sound = np.float32(sound * s.get_volume_cooficient())
        return {'end time': part['end time'], 'sound': sound}

    def get_frame(self, time):
        im = self.video.get_frame(time)
        if self.settings.get_brightness() != 1:
            im = np.maximum(im * self.settings.get_brightness(), 255)
            im = im.astype(np.uint8)
        for i in range(self.settings.get_rotate_image() % 4):
            im = np.transpose(im, (1, 0, 2))
            im = im[::-1]
        if self.settings.get_inverted():
            im = im[::-1]
        return im
    
    def get_duration(self):
        return self.video.get_duration()
    
    def short_str(self):
        return f"{self.video.short_str()}{str(self.settings)[8:]}"

    def long_str(self):
        return f"{__class__.__name__}({self.video}, {self.settings})"

    def __str__(self):
        return self.long_str()


class SAV0(VideoSettings):   # Use 'uV8px2beVr' for search
    def __init__(self, video, settings, sound_threshold=0.1):
        def is_voice_func(sound):
            return sound.max() > sound_threshold
        super().__init__(video, settings, is_voice_func=is_voice_func)


class BadSAV0(VideoSettings):  # Use '9RBh009v8M' for search
    def __init__(self, video, settings, frequency_cond):
        def is_voice_func(sound):
            number_of_zeros = (sound[1:] * sound[:-1] <= 0).sum()
            frequency = number_of_zeros / (len(sound) / AUDIO_FPS)
            # print(frequency, number_of_zeros, len(sound) / AUDIO_FPS, sound.shape)
            return frequency_cond(frequency)
        super().__init__(video, settings, is_voice_func=is_voice_func)
        
        
class VideoSaveStream:          # Use 'FwLJImGxRF' for search
    """
    VideoSaveStream - Stream for saving video.
    Syntax:
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

    def _save_part(self, start_time, folder, filecounter,
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

        class FakeClass:
            def close(self): pass

            def get_real_time(self): return 0

        mediawriter = FakeClass()
        last_shape, last_time = (-1, -1, 3), -1
        
        cur_time = start_time
        while eval(condition):
            cur_frame = self.video.get_frame(cur_time)[:, :, ::-1]
            if int(cur_time / 60) > int(last_time / 60):
                print(f"Start saving {int(cur_time / 60)} minute - real time: {mediawriter.get_real_time()}")
                last_time = cur_time
            
            part = self.video.get_nextsound(cur_time)
            check_type(part)

            if cur_frame.shape != last_shape:
                mediawriter.close()
                
                last_shape = cur_frame.shape                     
                path = f"{folder}{filecounter}"
                filecounter += 1
                mediawriter = MediaWriter(path, last_shape)
                
            mediawriter.write_audio_and_picture(part['sound'], cur_frame)
            cur_time = part['end time']
        
        mediawriter.close()
        return filecounter
    
    def save_part(self, start_time, end_time, folder, outputname):
        """
        Save video[start_time: end_time] in outputname:
            In outputname.mp4 save frames of video
            In outputname.mp3
        """
        rt = self._save_part(start_time, folder, outputname,
                             "cur_time < "+ str(end_time))
        return rt
    
    def save_n_seconds(self, start_time, n, folder, outputname):
        rt = self._save_part(start_time, outputname, folder,
                             "sound_len < AUDIO_FPS * " + str(n))
        return rt
    
    def short_str(self):
        return f"{__class__.__name__}({self.video.short_str()})"
    
    def long_str(self):
        return f"{__class__.__name__}({self.video})"

    def __str__(self):
        return self.long_str()

        
class MediaWriter:
    def __init__(self, filename, picture_shape):
        self.filename = filename
        self.outputname = f"{filename}.avi"
        self.videoname = f"{filename}_TEMP.mp4"
        self.audioname =  f"{filename}_TEMP.wav"

        self.videowriter = VideoWriter(self.videoname, -1, VIDEO_FPS, picture_shape[1::-1])
        self.audiowriter = wave.open(self.audioname, "w")
        self.audiowriter.setnchannels(4)
        self.audiowriter.setsampwidth(2)
        self.audiowriter.setframerate(AUDIO_FPS)

        self.sound_len, self.pictures = 0, 0

    def close(self):
        import os
        import subprocess
        
        self.videowriter.release()
        self.audiowriter.close()
        try:
            os.unlink(self.outputname)
        except FileNotFoundError:
            pass

        cmd = f'ffmpeg -i {self.videoname} -i {self.audioname} -c copy {self.outputname}'

        subprocess.call(cmd, shell=True)
        print("Video created: ", end = "")

        os.unlink(self.videoname)
        os.unlink(self.audioname)
        print("temp files deleted")

    def _write_picture(self, picture):
        self.pictures += 1
        self.videowriter.write(picture)

    def _write_audio(self, audio_n2_float_array):
        audio_n2_float_array = np.minimum(audio_n2_float_array, 1)
        audio_n2_float_array = np.maximum(audio_n2_float_array, -1)
        # print(np.abs(audio_n2_float_array).max())
        
        sound = audio_n2_float_array[:, 0] * (2 ** 15 - 1)
        sound = np.repeat(sound, 2).astype(int).reshape((-1, 2))
        # print(sound.max())
        self.sound_len += sound.shape[0]
        self.audiowriter.writeframes(sound.tobytes())

    def write_audio_and_picture(self, audio_n2float_array, picture):
        self._write_audio(audio_n2float_array)
        while self.sound_len / AUDIO_FPS > self.pictures / VIDEO_FPS:
            self._write_picture(picture)

    def get_real_time(self):
        return self.pictures / VIDEO_FPS


