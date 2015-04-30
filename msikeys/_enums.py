
class Region(object):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    _names = None
    _values = None

    @classmethod
    def names(cls):
        return cls._names

    @classmethod
    def values(cls):
        return cls._values


class Color(object):
    OFF = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    SKY = 5
    BLUE = 6
    PURPLE = 7
    WHITE = 8

    _names = None
    _values = None

    @classmethod
    def names(cls):
        return cls._names

    @classmethod
    def values(cls):
        return cls._values


class Level(object):
    LIGHT = 3
    LOW = 2
    MED = 1
    HIGH = 0

    _names = None
    _values = None

    @classmethod
    def names(cls):
        return cls._names

    @classmethod
    def values(cls):
        return cls._values


class Mode(object):
    NORMAL = 1
    GAMING = 2
    BREATHE = 3
    DEMO = 4
    WAVE = 5

    _names = None
    _values = None

    @classmethod
    def names(cls):
        return cls._names

    @classmethod
    def values(cls):
        return cls._values


def _enum_vals(enums):
    for enum in enums:
        d = dict(enum.__dict__)
        for k, v in enum.__dict__.items():
            if k[0] == '_' or type(v) == classmethod:
                del d[k]
        enum._names = d
        enum._values = {v: k for k, v in d.items()}

_enum_vals([Region, Color, Level, Mode])
