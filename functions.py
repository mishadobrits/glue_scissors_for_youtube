from moviepy.editor import VideoFileClip
from pafy import new as pafy_new
from filedict import FileDict

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
    return "".join(list(msg.replace("\n", " ").split()))


"""
@in_new_thread
def my_print(a):
    for i in range(100):
        print("thread {} print {}\n".format(a, i), end = "")

for i in range(10):
    my_print(i)"""
