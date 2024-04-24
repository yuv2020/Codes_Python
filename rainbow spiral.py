import turtle
from turtle import *

turtle.title("rainbow spiral")
speed(5)
bgcolor("black")
red,green,blue=(255,0,0)

for i in range(255*2):
    colormode(255)
    if i<255//3:
        green+=3
    elif i<255*2//3:
        red-=3
    elif i<255:
        blue+=3
    elif i<255*4//3:
        green-=3
    elif i<255*5//3:
        red+=3
    else:
        blue-=3

    fd(50+i)
    rt(91)
