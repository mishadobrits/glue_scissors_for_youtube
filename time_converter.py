import re


"""
Contain convert_times_in_comment(youtube_comment, times_converting_filepath) function.
This function find all times in youtube_comment (time in format m:s or h:m:s) and replace it
in correct times using .time_converting file.
For example: "abracadabra 0:30 qwerty 1:14 foo" -> "abracadabra 0:24 qwerty 1:00 foo"
"""


def file_iterator(filepath, chunk=2 ** 15):
    lines = 1
    with open(filepath) as f:
        while lines:
            lines = f.readlines(chunk)
            for elem in lines:
                yield elem


def convert_times_in_comment(youtube_comment, times_converting_filepath):
    """
    :comment: - string which function will parse
    :times_converting_filepath: - filepath to .time_converting file
    """
    youtube_comment = 'q' + youtube_comment
    expr = re.compile("((\d{1,2}:){1,2}\d{1,2})")  # (\d{1,2}:){,2}
    match = re.split(expr, youtube_comment)
    times, youtube_comment = match[1::3], match[0::3]

    def str_to_time(time_str):
        l = list(map(float, time_str.split(':')))[::-1]
        return sum(l[i] * 60 ** i for i in range(len(l)))

    times = [str_to_time(elem) for elem in times]
    new_times = [-1] * len(times)
    with open(times_converting_filepath) as f:
        last_values = (0, 0)
        for j, elem in enumerate(file_iterator(times_converting_filepath)):
            cur_values = list(map(float, elem.split()))
            for i, elem in enumerate(times):
                if last_values[0] <= elem <= cur_values[0]:
                    new_times[i] = (last_values[1] + cur_values[1]) / 2
            last_values = cur_values

    def time_to_str(seconds):
        s = int(seconds)
        h, m, s = s // (60 * 60), (s // 60) % 60, s % 60
        s = str(s)
        if len(s) == 1:
            s = "0" + s
        return f"{str(h) + ':' if h else ''}{m}:{s}"

    youtube_comment = list(youtube_comment)
    rt_comment = "".join([elem[0] + time_to_str(elem[1]) for elem in zip(youtube_comment, new_times)])
    rt_comment += youtube_comment[-1]
    rt_comment = rt_comment[1:]
    return rt_comment