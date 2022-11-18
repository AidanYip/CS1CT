age = int(input("Age: "))

file = open("nameage.txt")

name = file.readline()

while name != "":
    theage = int(file.readline())
    if theage == age:
        print(name)
    name = file.readline()
