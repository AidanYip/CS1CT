file = open("readings.txt")

number = file.readline()

while number != "":
    number = int(number)
    if number >= 0:
        print(number)
    else:
        print("0")
    number = file.readline()
