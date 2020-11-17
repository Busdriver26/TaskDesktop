from timeM import timeMethods as tm
from rw import readWriteJson as rwj
from draw import readJsonAndDraw

r = readJsonAndDraw()
r.drawTask()
r.drawCalendar(text_size=50,offset=125)