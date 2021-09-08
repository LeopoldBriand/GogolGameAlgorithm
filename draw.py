import json
import io
import os
from tkinter import Canvas, NW
from utils.template import GogoleTemplate
from PIL import Image, ImageTk
import random

filelist=os.listdir('images')
# for fichier in filelist[:]: 
#     if not(fichier.endswith(".png") or not(fichier.endswith(".PNG"))):
#         filelist.remove(fichier)
print(len(filelist))

def whiteToTransparent(image):
    img = image.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    return img
    


def draw(card, template, i, canvas):
    cardToPrint = GogoleTemplate(i)
    cardToPrint.initCircles(card, template)
    background = ImageTk.PhotoImage(Image.open('./cercle.PNG'))
    canvas.create_image(0,0,anchor = NW, image=background)
    #canvas.create_oval(0,0,1000,1000)
    images = []
    for gogol in cardToPrint.circles:
        print(gogol.num)
        rotation = random.randint(0,360)
        transformedImage = Image.open('./images/' + filelist[gogol.num])
        #transformedImage = whiteToTransparent(Image.open('./images/' + filelist[gogol.num]))
        resizedImage = transformedImage.resize((gogol.radius*2, gogol.radius*2), Image.ANTIALIAS).rotate(rotation, Image.NEAREST)
        images.append(ImageTk.PhotoImage(resizedImage))
        canvas.create_image(gogol.getPos(), anchor = NW, image=images[-1])
        # canvas.create_oval(gogol.returnCirclePositions())
        # canvas.create_text(gogol.getPos(),text=str(gogol.num))

    save(canvas, cardToPrint.name)

def save(canvas, name):
    ps = canvas.postscript(colormode='color')
    print(Image)
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('./cards/'+ str(name) +'.jpg')