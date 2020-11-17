from PIL import Image, ImageDraw, ImageFont
import numpy as np
class imgManipulate:
    def imageAddText(self,textToDraw, left, top,align = 'left' ,text_color=(255, 255, 255), text_size=70, pathLoad="pic/black.png", save=True, pathSave="pic/bckgrnd.png",ttf="ttf/Deng.ttf"):
        img = Image.open(pathLoad)
        draw = ImageDraw.Draw(img)
        fontStyle = ImageFont.truetype(ttf, text_size, encoding="utf-8")
        draw.multiline_text((left, top), textToDraw, text_color, font=fontStyle,spacing = 20,align = align)
        if save:
            img.save(pathSave)
        return img
#