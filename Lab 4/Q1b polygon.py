import turtle

sides = int(input("Number of sides of your polygon: "))

for i in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)

turtle.done()