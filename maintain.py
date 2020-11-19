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

    def update(self,img):
        tempPic = self.tempRJAD.drawTask(pathLoad=img)
        tempPic = self.tempRJAD.drawCalendar(pathLoad=tempPic)
        self.tempSWP.changeWallPaper(tempPic)
        return
        