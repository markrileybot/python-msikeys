import os
import hid
import logging

from ConfigParser import SafeConfigParser
from msikeys import Color, Mode, Level, Region

__CFG_DIRS = ['$XDG_CONFIG_HOME', '~/.config', '~/']
__CFG_FILE = 'msikeys.ini'

def _find_config_file():
    config = None

    if config is None:
        for config_dir in __CFG_DIRS:
            config_dir = os.path.expandvars(os.path.expanduser(config_dir))
            if os.path.exists(config_dir):
                config = os.path.join(config_dir, __CFG_FILE)
                break

    if config is None:
        config = __CFG_FILE

    return config


class IO(object):

    def __init__(self, vid=6000, pid=65280, config=None):
        self._vid = vid
        self._pid = pid
        self._config_file = config if config is not None else _find_config_file()
        self._dev = hid.device()
        self._config = SafeConfigParser()

        try:
            self._dev.open(vid, pid)
        except IOError as e:
            logging.error('Failed to read device.  Do you have permission?  (%s)', e)
            raise e
        self._config.read(self._config_file)

    def __del__(self):
        self._dev.close()
        try:
            with open(self._config_file, 'w') as c:
                self._config.write(c)
        except IOError as e:
            logging.warn('Failed to write config %s', e)

    def read_region(self, region):
        section = 'region_%s' % Region.values()[region.id].lower()
        if self._config.has_section(section):
            color_name = self._config.get(section, 'color')
            if color_name is not None:
                region.color = Color.names()[color_name]
            level_name = self._config.get(section, 'level')
            if level_name is not None:
                region.level = Level.names()[level_name]

    def write_region(self, region):
        self._dev.send_feature_report([1, 2, 66, region.id, region.color, region.level, 0, 236])
        section = 'region_%s' % Region.values()[region.id].lower()
        if not self._config.has_section(section):
            self._config.add_section(section)
        self._config.set(section, 'color', Color.values()[region.color])
        self._config.set(section, 'level', Level.values()[region.level])

    def read_keyboard(self, keyboard):
        if self._config.has_section('keyboard'):
            mode_name = self._config.get('keyboard', 'mode')
            if mode_name is not None:
                keyboard.mode = Mode.names()[mode_name]

    def write_keyboard(self, keyboard):
        self._dev.send_feature_report([1, 2, 65, keyboard.mode, 0, 0, 0, 236])
        if not self._config.has_section('keyboard'):
            self._config.add_section('keyboard')
        self._config.set('keyboard', 'mode', Mode.values()[keyboard.mode])
