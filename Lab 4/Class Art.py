import turtle

turtle.speed(10)
turtle.Screen().colormode(255)
turtle.Screen().bgcolor(160, 160, 160)
turtle.color("pink", "yellow")
turtle.begin_fill()

for i in range(36):
    turtle.forward(300)
    turtle.right(130)

turtle.end_fill()
turtle.hideturtle()
