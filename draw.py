from pic import imgManipulate as imp
from rw import readWriteJson as rwj
from calendar import TextCalendar as TC
from timeM import timeMethods as tm

class readJsonAndDraw:
    teRw = rwj()
    teImp = imp()
    #draw的输入为字典项：{"Time":"YYYY-MM-DD","Job":["1","2","3",..]}
    def drawTask(self,year= True,left=1000,top=500,lineHeight = 30,path="dat/dat.json",pathLoad="pic/black.png", pathSave="pic/bckgrnd.png"):
        try:
            data = self.teRw.readDat()
            output = ""
            for dic in data:
                time = dic["Time"]   #yyyy-mm-dd
                jobs = dic["Job"]    #[t1,t2,t3,...]
                for job in jobs:
                    print(time+":"+str(len(time)))
                    while len(time)<10:
                        time = time+" "
                    if year:
                        output += time+"\t"+job+"\n\n"
                    else:
                        output += time[5:]+"\t"+job+"\n\n"
            print(output)
            self.teImp.imageAddText(output,left,top,text_size=40,pathLoad = pathLoad,pathSave = pathSave)
            return pathSave
        except:
            pass
            return

    def drawCalendar(self,left=1000,top=500,lineHeight = 30,path="dat/dat.json",pathLoad="pic/black.png", pathSave="pic/bckgrnd.png"):
        #try:
        data = self.teRw.readDat()
        output = ""
        cal = TC()
        temptm = tm()
        for dic in data:
            time = dic["Time"]
            timeDict = temptm.getTime(time)
        output = cal.formatmonth(timeDict["year"], timeDict["month"])
        print(output)
        #except:
        #    pass

r = readJsonAndDraw()
r.drawCalendar()