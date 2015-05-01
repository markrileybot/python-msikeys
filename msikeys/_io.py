import os
import hid
import logging

from ConfigParser import SafeConfigParser
from msikeys import Color, Mode, Level, Region

class IOBase(object):

    def read_region(self, region):
        pass

    def write_region(self, region):
        pass

    def read_keyboard(self, keyboard):
        pass

    def write_keyboard(self, keyboard):
        pass


class IO(IOBase):

    def __init__(self, vid=None, pid=None, config=None):
        self._chain = DevIO(vid=vid, pid=pid, next=ConfigIO(config=config, next=None))

    def __del__(self):
        self._chain.close()

    def read_region(self, region):
        self._chain.read_region(region)

    def write_region(self, region):
        self._chain.write_region(region)

    def read_keyboard(self, keyboard):
        self._chain.read_keyboard(keyboard)

    def write_keyboard(self, keyboard):
        self._chain.write_keyboard(keyboard)


class IOLink(IOBase):

    def __init__(self, next=None):
        self._next = next

    def read_region(self, region):
        self._read_region(region)
        if self._next is not None:
            self._next.read_region(region)

    def write_region(self, region):
        self._write_region(region)
        if self._next is not None:
            self._next.write_region(region)

    def read_keyboard(self, keyboard):
        self._read_keyboard(keyboard)
        if self._next is not None:
            self._next.read_keyboard(keyboard)

    def write_keyboard(self, keyboard):
        self._write_keyboard(keyboard)
        if self._next is not None:
            self._next.write_keyboard(keyboard)

    def close(self):
        self._close()
        if self._next is not None:
            self._next.close()

    def _read_region(self, region):
        pass

    def _write_region(self, region):
        pass

    def _read_keyboard(self, keyboard):
        pass

    def _write_keyboard(self, keyboard):
        pass

    def _close(self):
        pass


class ConfigIO(IOLink):

    CFG_DIRS = ['$XDG_CONFIG_HOME', '~/.config', '~/']
    CFG_FILE = 'msikeys.ini'

    def __init__(self, config=None, next=None):
        super(ConfigIO, self).__init__(next)
        self._config_file = config if config is not None else ConfigIO._find_config_file()
        self._config = SafeConfigParser()
        self._config.read(self._config_file)

    @classmethod
    def _find_config_file(cls):
        config = None

        if config is None:
            for config_dir in cls.CFG_DIRS:
                config_dir = os.path.expandvars(os.path.expanduser(config_dir))
                if os.path.exists(config_dir):
                    config = os.path.join(config_dir, cls.CFG_FILE)
                    break

        if config is None:
            config = cls.CFG_FILE

        return config

    def _read_region(self, region):
        section = 'region_%s' % Region.values()[region.id].lower()
        if self._config.has_section(section):
            color_name = self._config.get(section, 'color')
            if color_name is not None:
                region.color = Color.names()[color_name]
            level_name = self._config.get(section, 'level')
            if level_name is not None:
                region.level = Level.names()[level_name]

    def _write_region(self, region):
        section = 'region_%s' % Region.values()[region.id].lower()
        if not self._config.has_section(section):
            self._config.add_section(section)
        self._config.set(section, 'color', Color.values()[region.color])
        self._config.set(section, 'level', Level.values()[region.level])

    def _read_keyboard(self, keyboard):
        if self._config.has_section('keyboard'):
            mode_name = self._config.get('keyboard', 'mode')
            if mode_name is not None:
                keyboard.mode = Mode.names()[mode_name]

    def _write_keyboard(self, keyboard):
        if not self._config.has_section('keyboard'):
            self._config.add_section('keyboard')
        self._config.set('keyboard', 'mode', Mode.values()[keyboard.mode])

    def _close(self):
        try:
            with open(self._config_file, 'w') as c:
                self._config.write(c)
        except IOError as e:
            logging.warn('Failed to write config %s', e)


class DevIO(IOLink):

    def __init__(self, vid=6000, pid=65280, next=None):
        super(DevIO, self).__init__(next)
        self._vid = vid
        self._pid = pid
        self._dev = hid.device()

        try:
            self._dev.open(vid, pid)
        except IOError as e:
            logging.error('Failed to read device.  Do you have permission?  (%s)', e)
            raise e

    def _write_region(self, region):
        self._dev.send_feature_report([1, 2, 66, region.id, region.color, region.level, 0, 236])

    def _write_keyboard(self, keyboard):
        self._dev.send_feature_report([1, 2, 65, keyboard.mode, 0, 0, 0, 236])

    def _close(self):
        self._dev.close()
