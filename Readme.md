### TaskDesktop.py

### 模块

#### 图像处理 ：输出图片、在图片上输出文字

pic.py -- class imgManipulate

```python
def imageAddText(self,
                 text, 
                 left, top, text_color=(255, 255, 255), text_size=70, 		
                 pathLoad="pic/black.png", save=True, 
                 pathSave="pic/bckgrnd.png",ttf="ttf/Deng.ttf"):
```

#### Json数据读写

rw.py -- class readWriteJson

```python
def test(self,path = "dat/dat.json"):
def readDat(self,path="dat/dat.json",cond = 1):
def inputDat(self,task,path="dat/dat.json"):
def deleteDat(self,task,path="dat/dat.json"):
def deleteRepeat(self,path="dat/dat.json"):
```

图像大小：4000*2250（目前必须是）

外部库依赖：
import datetime
import calendar
from PIL import Image, ImageDraw, ImageFont
import re
import ctypes
import struct
import os
import json
import sys
