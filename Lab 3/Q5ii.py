myList = [3, 7, -1, 2, -10, 6, 8]

newList = []

for i in range(len(myList)):
    if myList[i] >= 0:
        newList.append(myList[i])
    else:
        newList.append(0)

print(newList)
