myList = [3, 7, -1, 2, -10, 6, 8]

newList = []

for i, number in enumerate(myList):
    if number < 0:
        newList.append(0)
    else:
        newList.append(myList[i])

print(newList)
