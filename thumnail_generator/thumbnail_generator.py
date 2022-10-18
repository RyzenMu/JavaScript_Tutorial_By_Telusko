import os
from turtle import *
import turtle
from tkinter import *
from PIL import *
import PIL.Image
from PIL import Image

list_dir = os.listdir()

for filename in list_dir:
    if 'mp4' in filename:
        print(filename)
        turtle.color('black')
        turtle.write(filename, font=('verdana', 100, 'normal'), align='center')

        ts = turtle.getscreen()
        # ts.getcanvas().postscript(file="0-intoduction.eps")
        ts.getcanvas().postscript(file=filename)
        # turtle.Screen().exitonclick()

        image = Image.open(filename)
        # image.show()

        rgb_image = image.convert('RGB')

        rgb_image.save(filename+'.png')




