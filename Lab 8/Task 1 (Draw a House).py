import math
import turtle

turtle.speed(5)

def house(sidelength):
    rooflength = math.sqrt(2) * sidelength/2
    turtle.begin_fill()
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.forward(sidelength)
    turtle.left(45)
    turtle.forward(rooflength)
    turtle.left(90)
    turtle.forward(rooflength)
    turtle.left(45)
    turtle.forward(sidelength)
    turtle.left(90)
    turtle.end_fill()


house(20)

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
house(50)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
house(70)

turtle.penup()
turtle.goto(200, 100)
turtle.pendown()
house(100)
