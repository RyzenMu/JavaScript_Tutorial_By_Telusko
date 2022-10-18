# import os

# list_dir = os.listdir()

# for filename in list_dir:
#     if 'mp4' in filename:
#         print(filename)

from turtle import *
import turtle
from tkinter import *
from PIL import *
import PIL.Image
from PIL import Image

turtle.color('deep pink')
turtle.write('0-introduction', font=('verdana', 100, 'normal'), align='center')

ts = turtle.getscreen()
ts.getcanvas().postscript(file="0-intoduction.eps")
# turtle.Screen().exitonclick()

image = Image.open('0-intoduction.eps')
# image.show()

rgb_image = image.convert('RGB')

rgb_image.save('0-intoduction.png')




