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
    def drawTask(self,year= True,left=1000,top=500,lineHeight = 30,path="dat/dat.json",text_size=50,pathLoad="pic/black.png", pathSave="pic/bckgrnd.png"):
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
            print("Drawing Tasks...")
            self.teImp.imageAddText(outputT,left,top,text_size=text_size,pathLoad = pathLoad,pathSave = pathSave)
            self.teImp.imageAddText(outputJ,left+300,top,text_size=text_size,pathLoad = pathSave,pathSave = pathSave)
            print("Drawing Tasks Done.")
            return pathSave
        except:
            print("Error: Drawing Task Failed.")
            return

    def drawFinTask(self,year= True,left=1000,top=500,lineHeight = 30,path="dat/fin.json",text_size=50,pathLoad="pic/black.png", pathSave="pic/bckgrnd.png"):
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
            print("Drawing Finished Tasks...")
            self.teImp.imageAddText(outputT,left,top,text_size=text_size,pathLoad = pathLoad,pathSave = pathSave)
            self.teImp.imageAddText(outputJ,left+300,top,text_size=text_size,pathLoad = pathSave,pathSave = pathSave)
            print("Drawing Finished Tasks Done.")
            return pathSave
        except:
            print("Error: Drawing Finished Task Failed.")
            return
    # 思路：由于排版必须列输出，每一列是某周的某一天+7重复。
    # 本版本只放本日起至下月月底的日历（beta）
    def drawCalendar(self,left=2500,top=500,lineHeight = 30,showdates = 30,path="dat/dat.json",text_size=50,pathLoad="pic/black.png", pathSave="pic/bckgrnd.png",offset = 125):
        try:
            temptm = tm()
            data = self.teRw.readDat()
            today = temptm.getTime(str(datetime.date.today()))
            cal = TC()
            #dates[i]的字符串就是周i+1的日期
            dates = ["Mo\n","Tu\n","We\n","Th\n","Fr\n","Sa\n","Su\n"]
            dates_colored = ["Mo\n","Tu\n","We\n","Th\n","Fr\n","Sa\n","Su\n"]
            deadLine = {}
            for dat in data:
                tempT = temptm.getTime(dat["Time"])
                tempMonth = int(tempT["month"])
                tempDay = int(tempT["day"])
                if tempMonth not in deadLine:
                    deadLine[tempMonth] = []
                deadLine[tempMonth].append(tempDay)
            thisMonth = cal.monthdays2calendar(int(today["year"]), int(today["month"]))
            if today["month"] == 12:
                nextMonth = cal.monthdays2calendar(int(today["year"])+1, 1)
            else:
                nextMonth = cal.monthdays2calendar(int(today["year"]),int(today["month"])+1)
            startFlag = 0
            for week in thisMonth:
                for days in week:
                    if days[0]>=int(today["day"]):
                        if days[0] == int(today["day"]):
                            startFlag = 1
                            tempWeekDay = days[1]
                        if days[0] < int(today["day"]) + 7 and days[1]<tempWeekDay:
                            dates[days[1]] += "\n"
                            dates_colored[days[1]] += "\n"
                        dates[days[1]] = dates[days[1]] + str(days[0]) + "\n"
                        if days[0] in deadLine[int(today["month"])]:
                            dates_colored[days[1]] = dates_colored[days[1]] + str(days[0]) + "\n"
                        else:
                            dates_colored[days[1]]+="\n"

                    elif startFlag == 1: #当本月日期结束后退出
                        break
            monthNo = int(today["month"])+1
            if monthNo>12:
                monthNo = 1
            for week in nextMonth:
                for days in week:
                    if(days[0]!=0):
                        dates[days[1]] = dates[days[1]] + str(days[0]) + "\n"
                        if monthNo in deadLine and days[0] in deadLine[monthNo]:
                            dates_colored[days[1]] = dates_colored[days[1]] + str(days[0]) + "\n"
                        elif monthNo in deadLine:
                            dates_colored[days[1]]+="\n"
            print("Drawing Calendar...")
            offset1 = 0
            for col in dates:
                self.teImp.imageAddText(col,left+offset1,top,ttf ="ttf\SourceCodePro-Medium.ttf",text_size=text_size,pathLoad = pathSave,pathSave = pathSave,align = 'center')
                offset1 += offset
            offset1 = 0
            for col in dates_colored:
                self.teImp.imageAddText(col,left+offset1,top,ttf ="ttf\SourceCodePro-Medium.ttf", text_size=text_size,text_color=(255, 255, 0),pathLoad = pathSave,pathSave = pathSave,align = 'center')
                offset1 += offset
            offset1 = 0
            print("Drawing Calendar Done.")
            return pathSave
        except:
            print("Error: Drawing Calendar Failed.")
