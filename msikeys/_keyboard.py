
import msikeys

class Region(object):

    def __init__(self, id, io):
        self._id = id
        self._io = io
        self._color = msikeys.Color.OFF
        self._level = msikeys.Level.MED
    
    @property
    def id(self):
        return self._id

    @property
    def color(self):
        return self._color    

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def load(self):
        self._io.read_region(self)
        return self

    def commit(self):
        self._io.write_region(self)
        return self


class Keyboard(object):

    def __init__(self, io):
        self._io = io
        self._regions = [Region(msikeys.Region.LEFT, io),
                         Region(msikeys.Region.MIDDLE, io),
                         Region(msikeys.Region.RIGHT, io)]
        self._mode = msikeys.Mode.NORMAL

    def __iter__(self):
        return iter(self._regions)

    def _mkarr(self, arr):
        if type(arr) == int:
            arr = [arr for r in self]
        if len(arr) < 1:
            arr = [1 for r in self]
        while len(arr) < len(self._regions):
            arr += [arr[0]]
        return arr

    @property
    def colors(self):
        return [r.color for r in self]

    @colors.setter
    def colors(self, colors):
        colors = self._mkarr(colors)
        for i, region in enumerate(self):
            region.color = colors[i]

    @property
    def levels(self):
        return [r.level for r in self]

    @levels.setter
    def levels(self, levels):
        levels = self._mkarr(levels)
        for i, region in enumerate(self):
            region.level = levels[i]

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode

    def load(self):
        for region in self:
            region.load()
        self._io.read_keyboard(self)
        return self

    def commit(self):
        for region in self:
            region.commit()
        self._io.write_keyboard(self)
        return self