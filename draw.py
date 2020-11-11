from pic import imgManipulate as imp
from rw import readWriteJson as rwj
import re

class readJsonAndDraw:
    #draw的输入为字典项：{"Time":"YYYY-MM-DD","Job":["1","2","3",..]}
    def draw(self,task,left,top,path="dat/dat.json"):
        time = task["Time"]
        jobs = task["Job"]