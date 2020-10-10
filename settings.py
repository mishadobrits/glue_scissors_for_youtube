# setting.py
import numbers
from functions import str_to_error_message



SETTING_EXTENTION = "SVA_settings"
TRIVIAL_DICT = {'global_speed': 1,
                'loud_speed': 1,
                'quiet_speed': 1,
                'min_quiet_time': 0.25,
                'max_quiet_time': 10 ** 10,
                'sound_threshold': 0.1,
                'volume_cooficient': 1,
                'quiet_volume_cooficient': 1,
                'loud_volume_cooficient': 1,
                'max_volume': 1,
                'decrease': 1,
                'brightness': 1,
                'contras_ratio': 1,
                'rotate_image': 0,
                'inverted': False,
               }


class Settings:
    """
    you can change it, read from file, save to file,
    convert it to and from dict
    argumets
         you canspecify only one among (filepath, kwargs)
             otherwise excecption will be raised
    ----filepath - Settings will be read from file
    ----kwargs in format global_speed=value
                         loud_speed=value
                              ...
                         inverted=value
            some of them can be skipped

    fields: self.
      (float)
        loud_speed - accelerating loud parts of video/audio
        quiet_speed - accelerating quiet parts of video/audio
        global_speed - multiplyied by loud_speed & quiet_speed
        min_quiet_time - the part of the video part that will not speed up
                         before min_quiet_time
        max_quiet_time - the part of the video part that will be skipped
                         after max_quiet_time
        sound_threshold - border between loud sound and quiet sound

        volume_cooficient - multiplied by sound
        quiet_volume_cooficient - multiplied by sound in quiet video parts 
        loud_volume_cooficient - multiplied by sound in loud video parts 
        max_volume - if cur_sound > max_volume: cur_sound = max_volume
        
        decrease - # number to !decrease! image
        brightness - number to make more bright
        contras_ratio - number to make more bright
        rotate_image (only 0, 1, 2, 3) - how many 90-turnes of video
        inverted (bool) - is image reversed relative vertical axis
        
    methods: 
        self.to_dict() - convert self to dict
        self.save_to_file() - save self to file
        self.set_X(value), self.get_X - set field X value and get field X
                for all fields X
    
    """
    def __init__(self, filepath="", **kwargs):
        """
        if filepath Settings will be read from file
        you can specify only one among (filepath, kwargs)
        filepath must be end by SETTING_EXTENTION
        format of dictionary is the same like format of self.to_dict() 
        """
        if filepath and kwargs:
            raise Exception("""Settings.__init__() takes filepath or kwargs
                            filepath = {}
                            kwargs = {}
                            were given""".format(str(filepath), str(kwargs)))

        filepath = filepath.strip()
        if filepath and not filepath.endswith("." + SETTING_EXTENTION):
            error = "'filepath' must be end in '{}', '{}' were given"
            raise Exception(error.format("." + SETTING_EXTENTION, filepath))

        if filepath:
            with open(filepath, "r") as f:
                kwargs = eval("".join(f.readlines()))

        for elem in TRIVIAL_DICT:
            self.__dict__[elem] = kwargs.get(elem, TRIVIAL_DICT[elem])

    def check_type_decorators_generator(excpected_type=numbers.Number):
        def check_type_decorator(func):
            def wrapper(self, arg1, *args, **kwargs):
                if not isinstance(arg1, excpected_type):
                   msg = f"""function '{__class__.__name__}.{func.__name__}'
                         expected '{excpected_type.__name__}' type
                         (or inherited classes).
                         Type({arg1}) = '{type(arg1).__name__}' were given."""
                   raise TypeError(str_to_error_message(msg))
                return func(self, arg1, *args, **kwargs)
            return wrapper
        return check_type_decorator

    @check_type_decorators_generator()                     
    def set_global_speed(self, value):
        self.global_speed = abs(value)
 
    def get_global_speed(self):
        return self.global_speed

    @check_type_decorators_generator()  
    def set_loud_speed(self, value):
        self.loud_speed = abs(value)

    def get_loud_speed(self):
        return self.loud_speed  # * self.global_speed
    
    @check_type_decorators_generator()  
    def set_quiet_speed(self, value):
        self.quiet_speed = abs(value)

    def get_quiet_speed(self):
        return self.quiet_speed  # * self.global_speed

    @check_type_decorators_generator()  
    def set_min_quiet_time(self, value):
        self.min_quiet_time = abs(value)

    def get_min_quiet_time(self):
        return self.min_quiet_time
    
    @check_type_decorators_generator()  
    def set_max_quiet_time(self, value):
        self.max_quiet_time = abs(value)

    def get_max_quiet_time(self):
        return self.max_quiet_time

    @check_type_decorators_generator()  
    def set_volume_cooficient(self, value):
        self.volume_cooficient = abs(value)

    def get_volume_cooficient(self):
        return self.volume_cooficient

    @check_type_decorators_generator()  
    def set_quiet_volume_cooficient(self, value):
        self.quiet_volume_cooficient = abs(value)

    def get_quiet_volume_cooficient(self):
        return self.quiet_volume_cooficient

    @check_type_decorators_generator()  
    def set_loud_volume_cooficient(self, value):
        self.loud_volume_cooficient = abs(value)

    def get_loud_volume_cooficient(self):
        return self.loud_volume_cooficient

    @check_type_decorators_generator()  
    def set_max_volume(self, value):
        self.max_volume = abs(value)

    def get_max_volume(self):
        return self.max_volume

    @check_type_decorators_generator()  
    def set_decrease(self, value):
        self.decrease = abs(value)

    def get_decrease(self):
        return self.decrease

    def get_brightness(self):
        return self.brightness

    @check_type_decorators_generator()  
    def set_brightness(self, value):
        self.brightness = abs(value)

    def get_contras_ratio(self):
        return self.contras_ratio

    @check_type_decorators_generator()  
    def set_contras_ratio(self, value):
        if value <= 0:
            return 
        self.contras_ratio = value

    @check_type_decorators_generator(int)  
    def set_rotate_image(self, value):
        self.rotate_image = value % 4

    def get_rotate_image(self):
        return self.rotate_image
    
    @check_type_decorators_generator(bool) 
    def set_inverted(self, value):
        self.inverted = value

    def get_inverted(self):
        return self.inverted
    
    def full_dict(self):
        """convert self to dict
        for inverse operation use smth = Settings(**dictionary)"""
        rt = {}
        for elem in TRIVIAL_DICT:
            if self.__dict__[elem] != TRIVIAL_DICT[elem]:
                rt[elem] = self.__dict__[elem]
        return rt

    def __getitem__(self, key):
        return self.full_dict()[key]

    def to_dict(self):
        full_dict, part_dict = self.full_dict(), {}
        for elem in full_dict:
            if full_dict[elem] != TRIVIAL_DICT[elem]:
                part_dict[elem] = full_dict[elem]
        return part_dict

    def __str__(self):
        d = self.to_dict()
        temp = ", ".join(["{} = {}".format(elem, d[elem]) for elem in d])
        return  "Settings({})".format(temp)

    def save_to_file(self, filepath):
        """Save self to filepath"""
        if not filepath.endswith("." + SETTING_EXTENTION):
            filepath += "." + SETTING_EXTENTION
        with open(filepath, "w") as f:
            print("{}: {}".format(filepath, self.to_dict()))
            f.write(str(self.to_dict()))

    def set_new_value(self, new_settings):
        if type(new_settings) != Settings:
            message = """Settings.set_new_value takes Settings
                         argument type({}) = {} were given
                      """.replace("\n", "")
            raise TypeError(message.format(new_settings, type(new_settings)))
        self = new_settings

    def is_trivial(self):
        return not bool(self.to_dict())

    

"""
Settings(sound_threshold=1).save_to_file(r"settings/without_speeding")
Settings().save_to_file(r"settings/usual_speeding")
Settings(volume_cooficient=0).save_to_file(r"settings/no_sound")
print("end") # """
r"""

# filepath = r"C:\Users\m\Desktop\PythonProjects\SmartAccelerator\2.1.0\no_sound.SVA_parameters
s = Settings(volume_cooficient = 0)
s.set_global_speed(1.1)
s.set_rotate_image(1.1)
print(s, s.to_dict(), bool(s), s.get_global_speed()) """

# s.save_to_file(filepath)
# t = Settings(filepath=filepath)
# print(str(t)) """

        
