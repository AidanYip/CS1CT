import math
import turtle

turtle.speed(0)

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
    turtle.forward(sidelength)

def row(n, size):
    for i in range(n):
        house(size)


row(8, 50)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
row(20, 20)
