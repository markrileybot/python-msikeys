import hid

class IO(object):

    def __init__(self, vid=6000, pid=65280):
        self._vid = vid
        self._pid = pid
        self._dev = hid.device()
        self._dev.open(vid, pid)

    def __del__(self):
        self._dev.close()

    def read_region(self, region):
        pass

    def write_region(self, region):
        self._dev.send_feature_report([1, 2, 66, region.id, region.color, region.level, 0, 236])
        self._dev.send_feature_report([1, 2, 65, 1, 0, 0, 0, 236])
