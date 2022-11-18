file = open("chat.txt")
newline = file.readline()

chat = {}

while newline != "":
    newline = newline.split()
    name = newline[2] + " " + newline[3]
    if name not in chat:
        chat[name] = 1
    else:
        chat[name] += 1
    newline = file.readline()

print(chat)
