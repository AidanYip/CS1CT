import turtle

colours = ['red', 'orange', 'yellow', 'green',
           'blue', 'purple', 'pink', 'white']

turtle.speed(10)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.left(90)
radius = 200
startingpoint = 180

for i in colours:
    turtle.color(i)
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(startingpoint, 0)
    turtle.right(180)
    turtle.pendown()
    startingpoint -= 20
    radius -= 20
