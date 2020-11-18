from timeM import timeMethods as tm
from rw import readWriteJson as rwj
from draw import readJsonAndDraw

r = rwj()
job = {
            "Time": "2020-11-9",
            "Job": "大数据作业"
        }
print(r.searchDat(job))