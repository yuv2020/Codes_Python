import turtle
import random
import math
turtle.speed(11)
turtle.color("Black")
turtle.up()

phi=(1+math.sqrt(5))/2
i=360/math.pi*(phi)
t=turtle
t.down()
for t in range(1):
    t.right(i)
    u=i
    t.forward(400)
