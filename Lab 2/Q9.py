file = open("felixexercisetimes.txt")

for i in range(10):
    weeklytotal = 0
    for j in range(7):
        weeklytotal = weeklytotal + int(file.readline())
    print("Week", str(i+1) + ":", weeklytotal, "hours")
