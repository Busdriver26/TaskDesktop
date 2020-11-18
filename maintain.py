from rw import readWriteJson as rwj

class maintain:
    tempRW = rwj()
    def finishTask(self,task):
        if not self.tempRW.searchDat(task):
            print("Sorry, task not found.")
            return
        self.tempRW.deleteDat(task)
        self.tempRW.inputDat(task,path="dat/fin.json")
        return


