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
