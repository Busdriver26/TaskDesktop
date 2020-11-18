import ctypes
import struct
import os

class setWallPaper:
    def is_64_windows(self):
        """Find out how many bits is OS. """
        return struct.calcsize('P') * 8 == 64

    def getSysParametersInfo(self):
        """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
        return ctypes.windll.user32.SystemParametersInfoW if self.is_64_windows() \
            else ctypes.windll.user32.SystemParametersInfoA

    def changeWallPaper(self,imagepath):
        abspath = os.path.abspath(imagepath)
        sysParametersInfo = self.getSysParametersInfo()
        r = sysParametersInfo(20, 0, abspath, 3)
        if not r:
            print(ctypes.WinError())