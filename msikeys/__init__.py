from ._keyboard import Keyboard, Region
from ._enums import Color, Level, Mode, Region

__global_kb = None

def get_keyboard(vid=6000, pid=65280, config=None):
    from ._io import IO
    global __global_kb
    if __global_kb is None:
        io = IO(vid=vid, pid=pid, config=config)
        __global_kb = Keyboard(io).load().commit()
    return __global_kb
