from pafy import new as pafy_new
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageColor
import threading
import subprocess
import os


""""""


def empty_func(): pass


def process_float_sound(audio_n2_float_array):
    audio_n2_float_array = np.minimum(audio_n2_float_array, 1)
    audio_n2_float_array = np.maximum(audio_n2_float_array, -1)
    # print(np.abs(audio_n2_float_array).max())

    sound = audio_n2_float_array[:, 0] * (2 ** 15 - 1)
    sound = np.repeat(sound, 2).astype(int).reshape((-1, 2))
    # print(sound.max())
    return sound


def merge_video_and_audio_and_delete_source(video_name, audio_name, output_name):
    try:
        os.unlink(output_name)
    except FileNotFoundError:
        pass
    cmd = f'ffmpeg -i {video_name} -i {audio_name} -c copy {output_name}'
    print(cmd)
    subprocess.call(cmd, shell=True)
    print("Video created: ", end="")

    os.unlink(video_name)
    os.unlink(audio_name)
    print("temp files deleted")


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
        print(msg.format(func.__name__, args, kwargs, end_time - start_time))
        return rt
    wrapper.__name__ = "print_time({}).wrapper".format(func.__name__)
    return wrapper


def get_stream_url(video_id):
    return pafy_new(video_id).getbest().url


def str_to_error_message(msg):
    """Delete \n from msg and replace ' '*n -> ' '"""
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


def image_from_text(text, bg="black", fg="white", font="arial",
                    letter_size=40, align="center", indent=5, up_indent=-1,
                    right_indent=-1, down_indent=-1, left_indent=-1):
    #  Use '90kP2mTP9v' for search
    """
    Create image with specified text.
    kwargs:
    ----bg="black", fg="white - background and frontground color
             in im_type format. You can use tuple in 'RGB' format.
             for example (0, 0, 0) - black in 'RGB'.
    ----font="arial" (can be )
    ----letter_size=40 - size of one letter
    ----align="center"(or "left" or "right") - aling of text
    ----indent=5 - defoult indent
    ----up_indent, right_indent, down_indent, left_indent=-1 - indents from
            up, right, down and left.
            If value not specified it will beconsidered equal 'indent' value
    """
    try:
        ImageFont.truetype(font + ".ttf")
    except Exception as e:
        print(e)
        raise ValueError(f'image_from_text(...) takes wrong front {font}.ttf')

    def check_color_existence(arg):
        if isinstance(arg, str):
            try:
                ImageColor.getcolor(arg, "RGB")
            except:
                raise ValueError(f"color '{arg}' is not exist")
        elif isinstance(arg, tuple):
            if len(arg) != 3:
                msg = f'''color tuple must have lenght 3'.
                          len({arg}) = {len(arg)} were given'''
                raise ValueError(str_to_error_message(msg))
        else:
            msg = f'''color argument must be 'str' or 'tuple'.
                      type({arg}) = {type(arg)} were given'''
            raise ValueError(str_to_error_message(msg))

    check_color_existence(bg)
    check_color_existence(fg)

    im = Image.new("RGB", (1000, 1000), color=bg)
    bg_only = np.array(im)
    ImageDraw.Draw(im).text(
        (0, 0),  # Coordinates
        text=text,  # Text
        fill=fg,  # Color
        font=ImageFont.truetype(font + ".ttf", letter_size, encoding='UTF-8'),
        align=align
    )
    im_arr = np.array(im)
    
    columns = (im_arr != bg_only).astype(int).max(axis=(0, 2))
    columns = np.vstack((columns, np.arange(len(columns))))
    columns = columns[:, columns[0] != 0]
    left, right = columns[1].min(), columns[1].max() + 1

    rows = (im_arr != bg_only).astype(int).max(axis=(1, 2))
    rows = np.vstack((rows, np.arange(len(rows))))
    rows = rows[:, rows[0] != 0]
    top, bottom = rows[1].min(), rows[1].max() + 1
    im_arr = im_arr[top: bottom, left: right] 
     
    def get_indent(value):
        return value if value != -1 else indent
    
    up_indent, down_indent = get_indent(up_indent), get_indent(down_indent)
    right_indent, left_indent = get_indent(right_indent), get_indent(left_indent)

    rt = bg_only[:up_indent + down_indent + bottom - top,
                 :right_indent + left_indent + right - left]
    rt[up_indent: -down_indent, left_indent: -right_indent] = im_arr
    # Image.fromarray(rt).show()
    return rt


def ignore_exceptions_decorator_maker(exceptions_expression=Exception, exception_func=empty_func):
    def ignore_exceptions_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exceptions_expression:
                return exception_func()
        return wrapper
    return ignore_exceptions_decorator


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
