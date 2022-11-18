import random

x = random.randint(1, 100)
answer = 0
tries = 0

while answer != x:
    answer = int(input("Guess a number between 1-100: "))
    if answer > x:
        print("The number is lower")
    elif answer < x:
        print("The number is higher")
    tries += 1

print("You guessed right! Your number of tries was:", tries)
