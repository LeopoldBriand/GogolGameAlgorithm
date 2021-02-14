import json
from utils.template import GogoleTemplate
from tkinter import *

def draw(card, template):
    cardToPrint = GogoleTemplate()
    cardToPrint.initCircles(card, template)
    Fenetre = Tk()
    canvas = Canvas(Fenetre, width=1000,height=1000, bg="white")
    canvas.pack()
    canvas.create_oval(0,0,1000,1000)
    for gogol in cardToPrint.circles:
        canvas.create_oval(gogol.returnCirclePositions())
        canvas.create_text(gogol.getPos(),text=str(gogol.num))
    Fenetre.mainloop()

