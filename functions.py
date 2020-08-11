from moviepy.editor import VideoFileClip
from pafy import new as pafy_new
from filedict import FileDict
import numpy as np
from PIL import Image

url = 'http://youtube.com/watch?v=iwGFalTRHDA'


def in_new_thread(function):
    from functools import wraps
    wraps(function)
    def wrapper(*args, **kwargs):
        from threading import Thread
        t = Thread(target=function, args=args, kwargs=kwargs)
        name = "Thread - {} (args={}, kwargs={})".format(function.__name__,
                                                         args, kwargs)
        t.setName(name)
        t.start()
    wrapper.__name__ = "in_new_thread({}).wrapper".format(function.__name__)
    return wrapper


def print_time(func):
    from functools import wraps
    wraps(func)
    def wrapper(*args, **kwargs):
        from time import time
        start_time = time()
        rt = func(*args, **kwargs)
        end_time = time()
        
        msg = "function {} (args = {}, kwargs = {}) takes {} seconds"
        # print("time", end_time - start_time)
        print(msg.format(func.__name__, args, kwargs, end_time - start_time))
        return rt
    #print("func", func, "func")
    wrapper.__name__ = "print_time({}).wrapper".format(func.__name__)
    return wrapper


def get_stream_url(video_id):
    return pafy_new(video_id).getbest().url


def str_to_error_message(msg):
    return " ".join(list(msg.replace("\n", " ").split()))


def squeeze_sound(sound, x=1):
    sound_slice = np.arange(0, sound.shape[0] - 0.5, x).astype(int)
    return sound[sound_slice]

# @print_time
def image_to_new_size(image, new_w, new_h):
    image_h, image_w = image.shape[0], image.shape[1]
    if (image_h, image_w) == (new_w, new_h):
        return image
    k = max(image_w / new_w, image_h / new_h)
    if k != 1:
        image = Image.fromarray(image, "RGB")
        image = image.resize((int(image_w / k), int(image_h/k)))
        image = np.array(image)

    image_h, image_w = image.shape[0], image.shape[1]
    black = np.zeros((new_h, new_w, 3), dtype=image.dtype)
    
    x_left, y_up = (new_w - image_w) // 2, (new_h - image_h) // 2
    black[y_up: y_up + image_h, x_left: x_left + image_w, :] = image

    return black

