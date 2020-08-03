from moviepy.editor import VideoFileClip
from pafy import new as pafy_new
from filedict import FileDict
import numpy as np

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
        func(*args, **kwargs)
        end_time = time()
        
        msg = "function {} (args = {}, kwargs = {}) takes {} seconds"
        print(msg.format(func.__name__, args, kwargs, end_time - start_time))
    wrapper.__name__ = "in_new_thread({}).wrapper".format(func.__name__)
    return wrapper


def get_stream_url(video_id):
    return pafy_new(video_id).getbest().url


def str_to_error_message(msg):
    return " ".join(list(msg.replace("\n", " ").split()))


def squeeze_sound(sound, x=1):
    sound_slice = np.arange(0, sound.shape[0] - 0.5, x).astype(int)
    return sound[sound_slice]

def image_to_new_size(image, new_w, new_h):
    image_h, image_w = image.shape[0], image.shape[1]

    k = max(image_w / new_w, image_h / new_h)
    h_slice = np.arange(0, image.shape[0] - 0.5, k).astype(int)
    w_slice = np.arange(0, image.shape[1] - 0.5, k).astype(int)
    image = image[:, w_slice, :][h_slice, :, :]
    # print(image.shape)
    image_h, image_w = image.shape[0], image.shape[1]
    
    black = np.zeros((new_h, new_w, 3)).astype(image.dtype)
    x_left, y_up = (new_w - image_w) // 2, (new_h - image_h) // 2
    black[y_up: y_up + image_h, x_left: x_left + image_w, :] = image
    return black

r"""
a = np.array([2, 1, 0, -1, -2, -1, 0, 1, 2, 1])
print(squeeze_sound(a, 1.75))
from PIL import Image

show = lambda image: Image.fromarray(image, 'RGB').show()

im = Image.open(r"C:\Users\m\Pictures\original.jpg")
ndarr = np.array(im)
rt = image_to_new_size(ndarr, 500, 500) # [170: 853][:1024][:]
# print('all', (ndarr == rt).all())
# print(ndarr, rt)
# show(ndarr)
show(rt)
#print(np.ones((1, 3)) == 1) """
"""
@in_new_thread
def my_print(a):
    for i in range(100):
        print("thread {} print {}\n".format(a, i), end = "")

for i in range(10):
    my_print(i)"""
