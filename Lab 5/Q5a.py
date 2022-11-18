import random
import turtle

turtle.speed(0)
turtle.right(90)
turtle.pencolor("gray")
turtle.fillcolor("gray")

for row in range(5):
    for column in range(5):
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.circle(10, 180)
        turtle.right(180)
        turtle.pendown()   
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()

turtle.hideturtle()
turtle.done()
