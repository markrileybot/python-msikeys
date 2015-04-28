from ._keyboard import Keyboard, Region


def get_keyboard():
    from ._io import IO
    io = IO()
    kb = Keyboard(io)
    kb.load()
    return kb

