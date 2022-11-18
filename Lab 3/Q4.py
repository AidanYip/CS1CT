myString = "Here is the data you need: 3, 4, 8, 1, 3\n"

numString = myString[-14:-1] #slicing

numList = numString.split(sep = ", ") #split

intnumList = [] #empty list

for i in range(5):
    intnumList.append(int(numList[i]))

print(intnumList)

for j in range(5):
    print(intnumList[j], type(intnumList[j]))
