'''
Q5i.
We need to extract the name from each line
'''

# Q5ii
file = open("chat.txt")
newline = file.readline()

while newline != "":
    newline = newline.split()
    print("{firstname} {lastname}".format(firstname = newline[2], lastname = newline[3]))
    newline = file.readline()
