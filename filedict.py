#-*- coding: utf-8 -*-
import os
import sys


frozen = 'not'
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    frozen = 'ever so'
    bundle_dir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
MAIN_FOLDER = bundle_dir + "/_FileDict/"


def get_abs_path(relative_path):
    return MAIN_FOLDER + relative_path
###########################################################

abled_in_filepath = "qwertyuiopasdfghjklzxcvbnm1234567890_,?()'\" #"
abled_in_filepath += "йцукенгшщзхъфывапролджэячсмитьбю"
abled_in_filepath += abled_in_filepath.upper()


class FileDict:
    """
    FileDict is a dict[str] = abled_type with automatically saving to a file.
    Type 'A' is abled if for all type(obj) == A: A(str(obj)) == obj
    or 'A' is a tuple, list or set or dict ot abled types.
    So you can use it to memorize user's characteristic.

    
    __init__ arguments:
    ----folder - path relative to the MAIN_FOLDER folder
            __init__ create MAIN_FOLDER/folder directory
            all key-value pairs will be saved in this folder
            in format "in file your_folder/your_key.txt will be value"

    other public methods:
        self[your_key] = value (self[str] = str)
                         (self.__setitem__(your_key, value))
                         save string value to folder/your_key.txt 
                     
        self[your_key] - (self.__getitem__(your_key)) (self[str])
                          returned value from folder/your_key.txt
                          if file is not exist will e raised IndexError
                          
        del self[your_key] - (self.__delitem__(your_key)) (del self[str])
                          Delete folder/your_key.txt file
                          if file is not exist will e raised IndexError

    Exceptions tree
    │
    └──TypeError
        │
        ├───NotStrError
        │
        └───NotConvertableToStrError
    """
    class NotStrError(TypeError):
        def __init__(self, obj, func):
            message = """{} takes str argument; 
                         type({}) = {} were given""".replace("\n", "")
            message = " ".join(message.split())
            super().__init__(message.format(func.__name__, obj, type(obj)))
            
    class NotConvertableToStrError(TypeError):
        def __init__(self, obj, func):
            message = """{} takes argument 'obj' of type 'A'
                         Type 'A' is abled if for all type(obj) == A:
                         A(str(obj)) == obj
                         or 'A' is a tuple, list, set or dict ot abled types.
                         type({}) = {} were given""".replace("\n", "")
            message = " ".join(message.split())
            super().__init__(message.format(func.__name__, obj, type(obj)))
            # or list, tuple, set or dict of this types

    def __init__(self, folder=""):
        if folder[-1] not in r"\/": folder += "/"
        self.relative_folder = folder
        folder = MAIN_FOLDER + folder
        
        self.folder = folder
        s = folder + "1.txt"
        directory = os.path.dirname(s)
        directory = directory
        try:
            os.stat(directory)
        except:
            os.makedirs(directory)
        #print(directory)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise FileDict.NotStrError(key, FileDict.__getitem__)
        try:
            f = open(self._get_path(key))
        except FileNotFoundError as e:
            message = """Can't find key '{}' in FileDict({}).
                         Please, check the presence of a file {}
                         """.format(key, self.relative_folder,
                                    get_abs_path(self._get_path(key)))
            message.replace("\n", "")
            message = " ".join(message.split())
            raise KeyError(message)
        rt = f.readlines()
        """if len(rt) > 2:
            message = "file {} contain {}( > 2) stings".format(f, len(rt))
            ResourceWarning(message) """
        f.close()
        return from_text("".join(rt))

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise FileDict.NotStrError(key, FileDict.__setitem__)
        if not is_type_abled(value):
            raise FileDict.NotConvertableToStrError(value, FileDict.__setitem__)
        value = to_text(value)
        with open(self._get_path(key), "w") as f:
            f.write(value)
    
    def __delitem__(self, key):
        if not isinstance(key, str):
            raise FileDict.NotStrError(key, FileDict.__delitem__)
        try:
            with open(self._get_path(key)) as f:
                pass
        except FileNotFoundError:
            message = """Can't find key '{}' in FileDict({}).
                         Please, check the presence of a file {}
                         """.format(key, self.relative_folder,
                                    get_abs_path(self._get_path(key)))
            message.replace("\n", "")
            message = " ".join(message.split())
            
            raise KeyError(message) 
        os.remove(self._get_path(key))

    def get(self, key, spare_value):
        try:
            return self[key]
        except KeyError:
            return spare_value

    def get_and_write(self, key, spare_value):
        rt = self.get(key, spare_value)
        if rt == spare_value:
            self[key] = rt
        return rt

    def _get_path(self, key):
        return self.folder + get_path(key) + ".txt"


def to_text(obj):
    rt = type(obj).__name__ + "\n"
    if obj in [list, set, tuple]:
        rt += "[" + ", ".join("'" + to_text(elem) + "'" for elem in obj) + "]"
    elif obj == dict:
        d = {to_text(elem): to_text(obj[elem]) for elem in obj}
        rt += str(d)
    else:
        rt += str(obj)
    
    return "{}\n{}".format(type(obj).__name__, obj)


def from_text(text):
    l = list(text.split("\n"))
    obj_type = l[0]
    code_string = obj_type + "("
    text = "\n".join(l[1:])
    if obj_type in [list, set, tuple]:
        code_string += cur_type([from_text(elem) for elem in list(text)])
    elif obj_type == dict:
        d = dict(text)
        code_string += {from_text(elem) : from_text(d[elem]) for elem in d}
    elif obj_type == str:
        code_string += "'" + text + "'"
    else:
        code_string += text
    code_string += ")"  # l[0] + "(" + "\n".join(l[1:]) + ")"
    # print("code_string", code_string)
    return eval(code_string)


def get_path(key):
    key = key.replace("#", "#")
    rt = []
    for elem in key:
        if elem in abled_in_filepath:
            rt.append(elem)
        else:
            rt.append("#" + str(ord(elem)) + "#")
    return "".join(rt)


def is_type_abled(arg, print_exception=True):
    try:       # type(arg)(str(arg)) == arg or eval("{}({})".format(type(arg).__name__, str(arg))) == arg
        if type(arg)(str(arg)) == arg:
            return True
    except Exception as e:
        if print_exception:
            print(e)
    # """
    for cur_type in [list, tuple, set]:
        if arg == cur_type:
            return all(is_type_abled(elem) for elem in arg)
    if type(arg) == dict:
        rt = all(is_type_abled(elem) and is_type_abled(arg[elem]) for elem in arg)
        return rt   # """
    return False

# print(type("abc")(5))
# FileDict("folders")["abc:5"] = 5
# """
# print(is_type_abled([9, 10]))

# del FileDict("f")["4"]
"""
FileDict("f")["4"] = {"9": 10}
a = FileDict("f")["4"]
a[9] = 5
# a.append(5)
print(a, FileDict("f")["4"])  # """



# print(eval("list('\n[9, 10]')"))
"""
print(FileDict("folders")["screen"])
print(FileDict("folders").get("screen", 332))
"""
# f = FileDict("folder")
# FileDict("folder")["2"] = "1342"
# print(FileDict("folder")["2"]) # """
