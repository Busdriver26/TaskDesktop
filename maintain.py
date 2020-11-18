from rw import readWriteJson as rwj
from draw import readJsonAndDraw as rjad
from setDesktop import setWallPaper as swp

class maintain:
    tempRW = rwj()
    tempRJAD = rjad()
    tempSWP = swp()
    def finishTask(self,task):
        if not self.tempRW.searchDat(task):
            print("Sorry, task not found.")
            return
        self.tempRW.deleteDat(task)
        self.tempRW.inputDat(task,path="dat/fin.json")
        return

    def update(self):
        self.tempRJAD.drawTask()
        self.tempRJAD.drawCalendar()
        self.tempSWP.changeWallPaper("pic/bckgrnd.png")
        return



