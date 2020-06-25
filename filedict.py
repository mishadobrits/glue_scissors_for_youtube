# filedict
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
    
def get_abs_path(path):
    return bundle_dir + "/" + path

MAIN_FOLDER = get_abs_path("_FileDict/")


class FileDict:
    """
    FileDict is a dict[str] = str with automatically saving to a file.
    So you can use it to memorize user's characteristic

    
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
                          if file is not exist will be raised IndexError
                          
        del self[your_key] - (self.__delitem__(your_key)) (del self[str])
                          Delete folder/your_key.txt file
                          if file is not exist will be raised IndexError
      
    """
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
        if type(key) is not str:
            message = """FileDict.__getitem__ takes str argument
                         type({}) = {} were given""".replace("\n", "")
            message = " ".join(message.split())
            raise TypeError(message.format(key, type(key)))
        try:
            f = open(self.folder + key + ".txt")
        except FileNotFoundError as e:
            message = """Can't find key '{}' in FileDict({}).
                         Please, check the presence of a file {}
                         """.format(key, self.relative_folder,
                                    get_abs_path(self.folder + key + ".txt"))
            message.replace("\n", "")
            message = " ".join(message.split())
            raise KeyError(message)
        rt = f.readlines()
        if len(rt) > 1:
            message = "file {} contain {}( > 1) stings".format(f, len(rt))
            ResourceWarning(message)
        f.close()
        return "\n".join(rt)

    def __setitem__(self, key, value):
        if type(key) is not str or type(value) is not str:
            message = """FileDict.__setitem__ takes str argument
                         type({}) = {}, type({}) = {} were given
                         """.replace("\n", "")
            message = " ".join(message.split())
            message = message.format(key, type(key), value, type(value))
            raise TypeError(message)
        f = open(self.folder + key + ".txt", "w")
        f.write(value)
        f.close()
    
    def __delitem__(self, key):
        if type(key) is not str:
            message = """FileDict.__delitem__ takes str argument
                         type({}) = {} were given""".replace("\n", "")
            message = " ".join(message.split())
            raise TypeError(message.format(key, type(key)))
        try:
            with open(self.folder + key + ".txt") as f:
                pass
        except FileNotFoundError:
            message = """Can't find key '{}' in FileDict({}).
                         Please, check the presence of a file {}
                         """.format(key, self.relative_folder,
                                    get_abs_path(self.folder + key + ".txt"))
            message.replace("\n", "")
            message = " ".join(message.split())
            
            raise KeyError(message) 
        os.remove(self.folder + key + ".txt")

    def get(self, key, spare_value):
        try:
            return self[key]
        except KeyError:
            return spare_value


