# stupid_settings.py


class StupidSettings:
    """
    you can change it, read from file, save to file,
    convert it to and from dict
    argumets
         you canspecify only one among (filepath, kwargs)
         
    __init__ argumets
         you can specify only one among (filepath, kwargs)
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
        
        resize - # number to !decrease! image
        brightness - number to make more bright
        contras_ratio - number to make more bright

    fields: self.
      (float)
        speed - multiplyied by loud_speed & quiet_speed

        volume_cooficient - multiplied by sound
        max_volume - if cur_sound > max_volume: cur_sound = max_volume
        
        decrease -  number to !decrease! image
        brightness - number to make more bright
        contras_ratio - number to make more bright ???
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
            # print(kwargs)
        def value(key, value):
            return kwargs.get(key, value)
        self.global_speed = value("global_speed", 1)
        self.loud_speed = value("loud_speed", 1)
                # accelerating loud  parts of video/audio
        self.quiet_speed = value("quiet_speed", 1)
        #print(self.quiet_speed)
                # accelerating quiet parts of video/audio
        self.min_quiet_time = value("min_quiet_time", 0.4) # in seconds
        self.max_quiet_time = value("max_quiet_time", 10)  # in seconds
        self.sound_threshold = value("sound_threshold", 0.02)
                # minimal loud sound
        self.volume_cooficient = value("volume_cooficient", 1) 
        self.quiet_volume_cooficient = value("quiet_volume_cooficient", 1)
        self.loud_volume_cooficient = value("loud_volume_cooficient", 1)
        self.max_volume = value("max_volume", 1)  #maximal able volume
        
        self.resize = value("video_fps", 0.1)   # number to decrease image
        self.brightness = value("brightness", 0)
        self.contras_ratio = value("contras_ratio", 1)
        self.rotate_image = value("video_fps", 0)  # 0-3 (image angle)/90
        self.inverted = value("video_fps", False)  
                # invertion relative to vertical axis
    
    def set_global_speed(self, value):
        self.global_speed = abs(value)

    def get_global_speed(self):
        return self.global_speed

    def set_loud_speed(self, value):
        self.loud_speed = abs(value)

    def get_loud_speed(self):
        # print("eeeeeee")
        # print(self.loud_speed)
        return self.loud_speed  # * self.global_speed
    
    def set_quiet_speed(self, value):
        self.quiet_speed = abs(value)

    def get_quiet_speed(self):
        return self.quiet_speed  # * self.global_speed

    def set_min_quiet_time(self, value):
        self.min_quiet_time = abs(value)

    def get_min_quiet_time(self):
        return self.min_quiet_time
    
    def set_max_quiet_time(self, value):
        self.max_quiet_time = abs(value)

    def get_max_quiet_time(self):
        return self.max_quiet_time
    
    def set_sound_threshold(self, value):
        self.sound_threshold = abs(value)

    def get_sound_threshold(self):
        return self.sound_threshold
                # accelerating loud  parts of video/audio
        self.speed = value("speed", 1)
        #print(self.quiet_speed)
        
        self.volume_cooficient = value("volume_cooficient", 1) 
        self.max_volume = value("max_volume", 1)  #maximal able volume
        
        self.decrease = value("decrease", 0.1)   # number to decrease image
        self.brightness = value("brightness", 0)
        self.contras_ratio = value("contras_ratio", 1)
        self.rotate_image = value("rotate_image", 0)  # 0-3 (image angle)/90
        self.inverted = value("video_fps", False)  
                # invertion relative to vertical axis
    def set_speed(self, value):
        self.speed = abs(value)

    def get_speed(self):
        return self.speed  # * self.global_speed

    def set_volume_cooficient(self, value):
        self.volume_cooficient = abs(value)

    def get_volume_cooficient(self):
        return self.volume_cooficient

    def set_quiet_volume_cooficient(self, value):
        self.quiet_volume_cooficient = abs(value)

    def get_quiet_volume_cooficient(self):
        return self.quiet_volume_cooficient

    def set_loud_volume_cooficient(self, value):
        self.loud_volume_cooficient = abs(value)

    def get_loud_volume_cooficient(self):
        return self.loud_volume_cooficient

    def set_max_volume(self, value):
        self.max_volume = abs(value)

    def get_max_volume(self):
        return self.max_volume

    def set_decrease(self, value):
        self.decrease = abs(value)

    def get_decrease(self):
        return self.decrease

    def get_brightness(self):
        return self.brightness

    def set_brightness(self, value):
        self.brightness = abs(value)

    def get_contras_ratio(self):
        return self.contras_ratio

    def set_contras_ratio(self, value):
        if value <= 0:
            return 
        self.contras_ratio = value

    def set_rotate_image(self, value):
        self.rotate_image = value

    def get_rotate_image(self):
        return self.rotate_image

    def set_inverted(self, value):
        self.inverted = value

    def get_inverted(self):
        return self.inverted
    
    def to_dict(self):
        """convert self to dict
        for inverse operation use smth = Settings(**dictionary)"""
        return {
            'global_speed': self.get_global_speed(),
            'speed': self.get_speed(),
            'volume_cooficient': self.get_volume_cooficient(),
            'max_volume': self.get_max_volume(),
            'decrease': self.get_decrease(),
            'brightness': self.get_brightness(),
            'contras_ratio': self.get_contras_ratio(),
            'rotate_image': self.get_rotate_image(),
            'inverted': self.get_inverted(),
            }

    def __str__(self):
        d = self.to_dict()
        temp = ", ".join(["{} = {}".format(elem, d[elem]) for elem in d])
        return  "Settings({})".format(temp)

    def save_to_file(self, filepath):
        """save self to filepath"""
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
    """
    def set_new_value(self, new_settings):
        if type(new_settings) != Settings:
            message = '''Settings.set_new_value takes Settings
                         argument type({}) = {} were given
                      '''.replace("\n", "")
            raise TypeError(message.format(new_settings, type(new_settings)))
        self = new_settings
    """

    

"""
Settings(sound_threshold=1).save_to_file(r"settings/without_speeding")
Settings().save_to_file(r"settings/usual_speeding")
Settings(volume_cooficient=0).save_to_file(r"settings/no_sound")
print("end")
r"""
#filepath = r"C:\Users\m\Desktop\PythonProjects\SmartAccelerator\2.1.0\no_sound.SVA_parameters"
#s = Settings(volume_cooficient = 0)
#s.save_to_file(filepath)
#t = Settings(filepath=filepath)
#print(str(t)) """
