import random
import turtle

# draw 5x5 grey circles
def drawcircle():
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.circle(10, 180)
    turtle.right(180)
    turtle.pendown()

def removecircle():
    coords = input("Select a circle(x,y): ") # eg "2,2"
    coords = coords.split(sep=",")
    turtle.showturtle()
    turtle.penup()
    turtle.goto(20 * int(coords[0]), 20 * int(coords[1]))
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.hideturtle()
    
turtle.speed(0)
turtle.right(90)
turtle.pencolor("gray")
turtle.fillcolor("gray")

for row in range(5):
    for column in range(5):
        drawcircle()   
    turtle.penup()
    turtle.goto(0, (row + 1) * 20)
    turtle.pendown()

# removing target circle
removecircle()
nextcircle = input("Do you want to remove another circle? ").lower()
while nextcircle == "y" or nextcircle == "yes":
    removecircle()
    nextcircle = input("Do you want to remove another circle? ").lower()

