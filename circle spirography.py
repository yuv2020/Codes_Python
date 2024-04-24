# Program to make circle  spirography.
import turtle

turtle.bgcolor("Black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["Red", "Yellow", "white", "Blue", "Green", "Magenta"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()


    
