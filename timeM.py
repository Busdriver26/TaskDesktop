import re

class timeMethods:
    #注意这里的输入都是"YYYY-MM-DD"
    def getTime(self,time):
        pattern = re.compile("(^(?P<year>(19|20)\d\d)-(?P<month>0?[1-9]|1[012])-(?P<day>0?[1-9]|[12][0-9]|3[01])$)")        
        try:
            matc = pattern.match(time)
            res = {}
            res["year"] = matc.group('year')
            res["month"] = matc.group('month')
            res["day"] = matc.group('day')
            return res
        except:
            return {"year":-1,"month":-1,"day":-1}

    #只需要检查闰年与大小月
    def checkTime(self,time):
        days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        rec = self.getTime(time)
        if(rec["year"]==-1):
            return False
        y = int(rec["year"])
        m = int(rec["month"])
        d = int(rec["day"])
        if (y%4==0 and y%100!=0) or (y%400 == 0):
            days[2] = 29
        if days[m]<d or d<=0:
            return False
        return True

    def timeKey(self, task):
        time1 = self.getTime(task["Time"])
        return int(time1["year"])*10000+int(time1["month"])*100+int(time1["day"])

    #输入是一个字典，<:-1,=:0,>:1
    def compare(self,task1,task2):
        time1 = self.getTime(task1["Time"])
        time2 = self.getTime(task2["Time"])
        if time1["year"]>time2["year"]:
            return 1
        if time1["month"]>time2["month"]:
            return 1
        if time1["day"]>time2["day"]:
            return 1
        if time1["day"] == time2["day"]:
            return 0
        return -1
