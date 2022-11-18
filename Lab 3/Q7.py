# open data.txt
oldfile = open("data.txt")
# open a new file and set the mode to write
newfile = open("dataWithAverages.txt", "w") 

# copy first line to new file
nextLine = oldfile.readline() 
newfile.write(nextLine)

# change some parts of the second line and write it to the new file
nextLine = oldfile.readline() 
heading = nextLine[:19]
newheading = heading + "name, average score, individual scores"
newfile.write(newheading)
newfile.write("\n")

nextLine = oldfile.readline()


while nextLine != "":
    # use slice and split to prepare for calculation
    nextLineNL = nextLine[:-1]
    anotherList = nextLineNL.split()
    nextList = nextLineNL.split(sep = ", ")

    # ignore any names with no marks and skip them, calculate average with those that do have marks
    if len(nextList) > 2:
        total = 0
        average = 0
        for i in range(len(nextList) - 2):
            score = int(nextList[i+2])
            total = total + score
        average = total / (len(nextList) - 2)

        # combine the pieces together and write the entire line to the new .txt file
        finalString = anotherList[0] + " " + anotherList[1] + " " + str(average) + ", "
        for j in range(len(nextList) - 2):
            finalString += anotherList[j+2] + " "
        newfile.write(finalString)
        newfile.write("\n")

    # read new line before exiting loop
    nextLine = oldfile.readline()

# close the file at the end!
newfile.close()
