import turtle

turtle.speed(0)
turtle.Screen().colormode(255)
turtle.Screen().bgcolor(60, 60, 60)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()

for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                # even number
                turtle.pendown()
                turtle.color(232, 235, 239)
                turtle.begin_fill()
                for k in range(4):
                    turtle.forward(70)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(70)
            else:
                # odd number
                turtle.pendown()
                turtle.color(125, 135, 150)
                turtle.begin_fill()
                for k in range(4):
                    turtle.forward(70)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(70)
    else:
        for j in range(8):
            if j % 2 == 1:
                # even number
                turtle.pendown()
                turtle.color(232, 235, 239)
                turtle.begin_fill()
                for k in range(4):
                    turtle.forward(70)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(70)
            else:
                # odd number
                turtle.pendown()
                turtle.color(125, 135, 150)
                turtle.begin_fill()
                for k in range(4):
                    turtle.forward(70)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(70)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(560)
    turtle.right(180)

turtle.hideturtle()
turtle.done()
