# -*- coding: utf-8 -*-
import os
cwd=os.getcwd()

from swampy.Gui import *
from tkinter import PhotoImage

g = Gui()
for filename in os.listdir(cwd):
    try:
        photo = PhotoImage(file=filename)
        g.bu(image=photo)
        
        canvas = g.ca(width=300)
        canvas.image([0,0], image=photo)
    except:
        continue
#from PIL import ImageTk, Image
#
#image = Image.open('allen.png')
#photo2 = ImageTk.PhotoImage(image)
#g.la(image=photo2)

g.mainloop()

 