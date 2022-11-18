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

def gotocircle():
    turtle.showturtle()
    turtle.penup()
    turtle.goto(20 * int(coords[0]), 20 * int(coords[1]))

def actiononcircle():
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

# random circle selected by computer
correct = [random.randint(0, 4), random.randint(0, 4)]

# guessing time
coords = input("Guess a circle(x,y): ").split(sep=",") # eg "2,2"
coords = [int(coords[0]), int(coords[1])]
tries = 1

# if wrong
while coords != correct:
    gotocircle()
    turtle.pencolor("white")
    turtle.fillcolor("white")
    actiononcircle()
    tries += 1
    coords = input("You guessed wrong! Guess another circle(x,y): ").split(sep=",") # eg "2,2"
    coords = [int(coords[0]), int(coords[1])]

# if correct
gotocircle()
turtle.pencolor("red")
turtle.fillcolor("red")
actiononcircle()
print("Game Over! Your number of tries was:", tries)
