#!/usr/bin/env python

import msikeys
from msikeys import Color, Mode
import time

def main():
    """
    Doesn't do much....just loads the keyboard config from the ini
    """
    colors = [
        Color.YELLOW, Color.ORANGE, Color.RED, Color.PURPLE, Color.BLUE,
        Color.PURPLE, Color.RED, Color.ORANGE
    ]
    kb = msikeys.get_keyboard()
    colors_len = len(colors)
    while True:
        for i in xrange(colors_len):
            for ii, region in enumerate(kb):
                region.color = colors[(i+ii) % colors_len]
            kb.commit()
            time.sleep(.1)

if __name__ == '__main__':
    main()
