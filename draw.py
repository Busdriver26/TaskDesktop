from pic import imgManipulate as imp
from rw import readWriteJson as rwj
from calendar import TextCalendar as TC
from timeM import timeMethods as tm
import datetime
import calendar

class readJsonAndDraw:
    teRw = rwj()
    teImp = imp()
    #draw的输入为字典项：{"Time":"YYYY-MM-DD","Job":["1","2","3",..]}
    def drawTask(self,year= True,left=1000,top=500,lineHeight = 30,path="dat/dat.json",pathLoad="pic/black.png", pathSave="pic/bckgrnd.png"):
        try:
            data = self.teRw.readDat()
            outputT = ""
            outputJ = ""
            for dic in data:
                time = dic["Time"]   #yyyy-mm-dd
                jobs = dic["Job"]    #[t1,t2,t3,...]
                for job in jobs:
                    while len(time)<10:
                        time = time+" "
                    if year:
                        outputT += time+"\n"
                        outputJ += job+"\n"
                    else:
                        outputT += time[5:]+"\t"+job+"\n\n"
            self.teImp.imageAddText(outputT,left,top,text_size=40,pathLoad = pathLoad,pathSave = pathSave)
            self.teImp.imageAddText(outputJ,left+300,top,text_size=40,pathLoad = pathSave,pathSave = pathSave)
            return pathSave
        except:
            pass
            return

    # 思路：由于排版必须列输出，每一列是某周的某一天+7重复。
    # 本版本只放本日起至下月月底的日历（beta）
    def drawCalendar(self,left=1000,top=500,lineHeight = 30,showdates = 30,path="dat/dat.json",pathLoad="pic/black.png", pathSave="pic/bckgrnd.png"):
        try:
            temptm = tm()
            data = self.teRw.readDat()
            today = temptm.getTime(str(datetime.date.today()))
            cal = TC()
            #dates[i]的字符串就是周i+1的日期
            dates = ["Mo\n","Tu\n","We\n","Th\n","Fr\n","Sa\n","Su\n"]
            for dat in data:
                dates.append(temptm.getTime(dat["Time"]))
            thisMonth = cal.monthdays2calendar(int(today["year"]), int(today["month"]))
            if today["month"] == 12:
                nextMonth = cal.monthdays2calendar(int(today["year"])+1, 1)
            else:
                nextMonth = cal.monthdays2calendar(int(today["year"]),int(today["month"])+1)
            startFlag = 0
            for week in thisMonth:
                for days in week:
                    if days[0]>=today["day"]:
                        dates[days[1]] = dates[days[1]] + str(days[0]) + "\n"
                        startFlag = 1
                    elif startFlag == 1: #当本月日期结束后退出
                        break
                    else:
                        dates[days[1]] += '\n'

            
            print(output)
            self.teImp.imageAddText(output,left,top,text_size=40,pathLoad = pathLoad,pathSave = pathSave)
        except:
            pass

r = readJsonAndDraw()
r.drawCalendar()