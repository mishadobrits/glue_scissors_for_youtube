
#todo
#videos
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
    v = ... # creating video 1)    #  Use 'HglSFYJDDE' for search
    while not v.get_is_downloaded(): # video itself loads everything 
        from time import sleep       # that is part of it
        sleep(0.01)                  # SO YOU NEED LOAD ONLY THE RESULT VIDEO
    video_id = v.get_id()  # getting id (str) 1.1)
    
    # set the user's current viewing time frequently 
    v.set_users_cur_viewing_time(t)   # often  2)
    
    cur_video_filename = get_video_filename(video_id, inside_time_range)
    cur_audio_filename = get_audio_filename(video_id, inside_time_range)
    # in file named cur_video_filename yours video part
    # in file named cur_audio_filename yours audio part

    # you can send it to your server or do with it whatever you want



Code: Creating video: #  Use 'HglSFYJDDE' for search
You can create this types of video
    VideoFromYoutubeURL   #  Use 'j7ItYy3N2n' for search
    VideoFromImageURL     #  Use 'fjR1wW8o9d' for search
    VideoFromText         #  Use '55FPkUD5WO' for search

    SumOfVideo               # or video1 + video2 #  Use '0kxprGdgk8' for search
    SeparatedVideoAndAudio   # or video1 / video2 #  Use 'iPgx8iCcdC' for search



from videos import VideoFromYoutubeURL, VideoFromImageURL, VideoFromText
# import


horror_11s = VideoFromYoutubeURL("https://www.youtube.com/watch?v=qiZLHchtX8c",
                                 239, 250)     #  Use 'j7ItYy3N2n' for search
        #  __init__ args:  link or video id, start time(st), end time(et)  
# it is the same               video_id   st  et
test = VideoFromYoutubeURL("qiZLHchtX8c", 56, 64)
test.start_downloading_webm()


# You can set **kwargs that in Settings:
# brightness, speed, volume and max_volume and e.c.t.
# like this. 
rev9_8s = VideoFromYoutubeURL("2WemzwuAQF4", 56, 64, speed=0.9, volume=1.2)
rev9_3s = VideoFromYoutubeURL("2WemzwuAQF4", 66, 69, speed=0.9, volume=1.2)



# You can contencate videos.   #  Use '0kxprGdgk8' for search
rev9_11s = rev9_8s + rev9_3s # in "2WemzwuAQF4" will skipped 64-66
# it is the same rev9_11s = SumOfVideo(rev9_8s, rev9_3s)


# and you can also separate_video and audio
                    # video        audio
sep_video_an_audio = rev9_11s / horror_11s
# it is the same rev9_11s = SeparatedVideoAndAudio(rev9_11s, horror_11s)


#!!! again what, you may not download videos immediately
#!!! if you start load SumOfVideo or SeparatedVideoAndAudio it itself loads
#!!! all its part 


# VideoFromImageURL exmple    #  Use 'fjR1wW8o9d' for search
image_url = r"https://i.ibb.co/2K5q1y3/image.png"
image_10s = VideoFromImageURL(image_url, 10) # text duration; without sounds
# you can set any kwargs, duration will be divided by speeding
image_10s = VideoFromText("Any Text", 10, rotate=2)

#you can add sound using
image_with_sound_10s = image_10s / VideoFromYoutubeURL("7oEdx9IgPpo", 0, 10)


# VideoFromText exmple    #  Use '55FPkUD5WO' for search
text_8s = "Any text"
text_8s = VideoFromImageURL(image_url, 10)  #without sounds
# you can set any kwargs, duration will be divided by speeding
text_8s = VideoFromText("Any Text", 8, inverted=True)

#you can add sound using
text_with_sound_8s = image_10s / VideoFromYoutubeURL("7oEdx9IgPpo", 10, 18)

classes tree:
│
├moviepy.editor.VideoFileClip══╗
│                              ║
└Video┐                        ║    #  Use 'POFvmLHWHg' for search
  '''if isistance(v1, Video) and isistance(v2, Video) then
     v1 + v2 = SumOfVideo((v1, v2))
     v1 / v2 = SeparatedVideoAndAudio(video=v1, audio=v2)
  '''┌┘                        ║
     │                         ║
     ├VideoFromYoutubeURL══════╝    #  Use 'H6R9gbClEg' for search  
     │                              
     ├VideoFromImage                #  Use 'hDygGaJlAH' for search   
     │     │
     │     ├────VideoFromText       #  Use 'Pv1U9ovsOb' for search
     │     │
     │     ├────VideoFromImageURL   #  Use 'f5vfFwOTVd' for search
     │     │
     │     └────VideoFromFrameFromYoutubeVideo═════╗
     │                              #  Use 'hBavQ96HNM' for search
     │     
     ├SeparatedVideoAndAudio       #  Use '0uceFGY5J0' for search   
     │                               
     └SumOfVideo                    #  Use 'Ci1lua3fAb' for search  
             
"""

from moviepy.editor import VideoFileClip
from cv2 import VideoWriter
from stupid_settings import StupidSettings
from pafy import new as pafy_new
from functions import in_new_thread, print_time, update_stream_url
from filedict import FileDict


class Video:    #  Use 'POFvmLHWHg' for search
    def __add__(self, other):
        return SumOfVideo((self, other))

    def __div__(self, other):
        return SeparatedVideoAndAudio(self, other)

    @in_new_thread
    @print_time
    def save_subclip(self, start_time, end_time):
        delta = end_time - start_time
        N = int(25 * delta)
        frames = [self.get_frame(start_time + delta * i/N) for i in range(N)]

        w, h = frames[0].shape[0], frames[0].shape[1]
        out_name = "{}_{}-{}.mp4".format(self.__name__, start_time, end_time)
        out = VideoWriter(out_name, -1, 25, (h, w))
        for frame in frames:
            out.write(frame[:, :, ::-1])
        out.release()


class VideoFromYoutubeURL(VideoFileClip, Video):     # Use 'H6R9gbClEg' for search
    """

    __init__ argumnts:
    ----short_link - link like 'https://www.youtube.com/watch?v=2WemzwuAQF4'
                     or only video id ('2WemzwuAQF4')
    ----start_time - time in seconds    (float)
    ----end_time - time in seconds    (float)
    ----stupid_settings=StupidSettings() - settings for video

    """
    def __init__(self, short_link, start_time, end_time,
                 stupid_settings=StupidSettings()):
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

        self.video_id = get_id(url)
        self.start_time, self.end_time = start_time, end_time
        self.stupid_settings = stupid_settings
        self.__name__ = self.video_id
        self.is_downloaded = False

    @in_new_thread
    @print_time
    def start_downloading_webm(self):
        def call_super(self, video_id):
            super().__init__(FileDict("youtube_urls")[video_id])

        try:
            call_super(self, video_id)
        except (KeyError, OSError):
            print("update: {}".format(self.video_id))
            update_stream_url(self.video_id)
            call_super(self, video_id)

        self.get_frame(0)   # loading first frame
                            #get_frame function takes into account start_time
        self.is_downloaded = True
        print("end")

    def get_frame(self, t):
        if self.start_time + t > self.end_time:
            # print(t)
            msg = '''you asking about {}s,
                     but duration is start_time - end_time =
                     {} - {} = {}
                     '''.replace("\n", "").replace("  ", "")
            msg = msg.format(t, self.end_time, self.start_time,
                             self.end_time - self.start_time)
            raise ValueError(msg)
        
        # super() - VideoFileClip
        return super().get_frame(self.start_time + t)

    def get_is_downloaded(self):
        return self.is_downloaded

    
class VideoFromImage(Video):          #  Use 'hDygGaJlAH' for search
    pass


class VideoFromText(VideoFromImage):       #  Use 'Pv1U9ovsOb' for search
    pass


class VideoFromImageURL(VideoFromImage):   #  Use 'hDygGaJlAH' for search
    pass


class VideoFromFrameFromYoutubeVideo(VideoFromFrameFromYoutubeVideo):
    pass


class SumOfVideo(Video):              #  Use 'Ci1lua3fAb' for search
    pass


class SeparatedVideoAndAudio(Video): #  Use '0uceFGY5J0' for search
    pass


"""
url = "https://www.youtube.com/watch?v=2WemzwuAQF4" #t=56s"
video_id = "2WemzwuAQF4"
v = VideoFromYoutubeURL(video_id, 56, 69)
v.start_downloading_webm()
while not v.get_is_downloaded():
    from time import sleep
    sleep(0.1)
v.save_subclip(0, 10)  """
