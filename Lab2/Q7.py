file = open("readings.txt")

counter = 0

number = file.readline()

while number != "":
    number = int(number)
    if number > 0:
        counter += 1
    elif number <= 0:
        print("It has been above freezing", counter, "days in a row.")
        counter = 0
    number = file.readline()


