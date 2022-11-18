file = open("chat.txt")
newline = file.readline()

chat = {}

while newline != "":
    nameline = newline.split()
    chatline = newline.split(sep = ":")
    name = nameline[2] + " " + nameline[3]
    message = chatline[3][1:-1] # .strip() method also works
    if name not in chat:
        chat[name] = [message]
    else:
        chat[name].append(message)
    newline = file.readline()

print(chat)

namesearch = input("Enter a name: ")

if namesearch in chat:
    for c in chat[namesearch]:
        print(c)
else:
    print("There aren't any posts from {name}.".format(name=namesearch))
