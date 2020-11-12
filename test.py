from timeM import timeMethods as tm
from rw import readWriteJson as rwj

a = rwj()
b = a.readDat()
t = tm()

ino = {"Time":"2020-1-3","Job":"打一顿江33宇轩"}
#a.inputDat(ino)
a.deleteDat(ino,deleteAllInTime=True)
