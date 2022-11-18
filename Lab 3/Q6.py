oldfile = open("people.txt")
newfile = open("olderPeople.txt", "w")

person = oldfile.readline()

while person != "":
    person = person[:-1].split(sep = ", ")
    age = int(person[1])
    if age >= 65:
        newfile.write(person[0] + "\n")
    person = oldfile.readline()

newfile.close()
