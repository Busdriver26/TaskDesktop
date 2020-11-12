import json
import os,sys
from timeM import timeMethods as tm

class readWriteJson:
    #这里返回的、录入的、删除的统一格式都是字典
    #插入的task:每天一个列表
    #插入时：字符串
    tempTimeClass = tm()

    def test(self,path = "dat/dat.json"):
        os.chdir(os.path.dirname(sys.argv[0]))
        os.getcwd()
        with open(path,'r',encoding='utf-8') as loadF:
            temp = loadF.read()
            if len(temp) == 0:
                return False
            else:
                return True

    def readDat(self,path="dat/dat.json",cond = 1):
        os.chdir(os.path.dirname(sys.argv[0]))
        os.getcwd()
        if self.test():
            with open(path,'r',encoding='utf-8') as loadF:
                loadDict = json.load(loadF)
                if cond == 1:
                    return loadDict["Tasks"]
                else:
                    return loadDict
        return 0

    #这里的task input为字符串
    def inputDat(self,task,path="dat/dat.json"):
        inputTime = task["Time"]
        job = task["Job"]
        dateFlag = 0
        os.chdir(os.path.dirname(sys.argv[0]))
        os.getcwd()
        with open(path,'r',encoding='utf-8') as loadF:
            if not self.test():
                loadDict = {"Tasks":[]}
            else:
                loadDict = json.load(loadF)
            jsTask = loadDict["Tasks"] #一个字典的列表
            for tsk in jsTask:
                if tsk["Time"]==inputTime:
                    dateFlag = 1
                    tsk["Job"].append(job)
            if dateFlag==0 :
                newDate = {"Time":inputTime,"Job":[job]}
                jsTask.append(newDate)
        with open(path,'w',encoding='utf-8') as loadF:
            json.dump(loadDict,loadF,ensure_ascii=False,indent=4)
        self.deleteRepeat(path)
        self.sortDat(path)
        return

    def sortDat(self,path = "dat/dat.json"):
        os.chdir(os.path.dirname(sys.argv[0]))
        os.getcwd()
        with open(path,'r',encoding='utf-8') as loadF:
            loadDict = json.load(loadF)
            jsTask = loadDict["Tasks"] #一个字典的列表
            jsTask = sorted(jsTask,key = self.tempTimeClass.timeKey)
            storeDict = {"Tasks":jsTask}
            print(storeDict)
        with open(path,'w',encoding='utf-8') as loadF:
            json.dump(storeDict,loadF,ensure_ascii=False,indent=4)
        return

    def deleteDat(self,task,path="dat/dat.json"):
        inputTime = task["Time"]
        job = task["Job"]
        os.chdir(os.path.dirname(sys.argv[0]))
        os.getcwd()
        with open(path,'r',encoding='utf-8') as loadF:
            loadDict = json.load(loadF)
            jsTask = loadDict["Tasks"]
            for tsk in jsTask:
                if tsk["Time"] == inputTime:
                    tsk["Job"].remove(job)
        with open(path,'w',encoding='utf-8') as loadF:
            json.dump(loadDict,loadF,ensure_ascii=False,indent=4)
        self.sortDat(path)
        return

    def deleteRepeat(self,path="dat/dat.json"):
        os.chdir(os.path.dirname(sys.argv[0]))
        os.getcwd()
        with open(path,'r',encoding='utf-8') as loadF:
            loadDict = json.load(loadF)
            jsTask = loadDict["Tasks"] #一个字典的列表
            for tsk in jsTask:
                tempJob = []
                for job in tsk["Job"]:
                    if job not in tempJob:
                        tempJob.append(job)
                tsk["Job"]=tempJob
        with open(path,'w',encoding='utf-8') as loadF:
            json.dump(loadDict,loadF,ensure_ascii=False,indent=4)
        return
