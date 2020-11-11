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

    def compare(self,task1,task2):
        time1 = self.getTime(task1["Time"])
        time2 = self.getTime(task2["Time"])

a = timeMethods()
print(a.checkTime("2020-11-1"))