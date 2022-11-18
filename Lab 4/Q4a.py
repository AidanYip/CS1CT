import turtle

turtle.pensize(10)
directions = 'rrrruuuuuuuuulllrrrrrr'

for i in range(len(directions)):
    if directions[i] == 'r':
        turtle.setheading(0)
        turtle.forward(20)
    elif directions[i] == 'u':
        turtle.setheading(90)
        turtle.forward(20)
    else:
        turtle.setheading(180)
        turtle.forward(20)
