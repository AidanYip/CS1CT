import turtle

drawing = []
option = input("Do you want to (a)dd lines for your drawing or (r)ead in a drawing from a file? ")

if option == "a":
    nextinput = "y"
    while nextinput != "n":
        shape = input("Do you want to add a (l)ine or a (c)ircle? ")
        if shape == "l":
            newLine = input("Type in the four numbers for the added line and a colour of your choice(optional), separated by spaces ")
            bits = newLine.split()
            if len(bits) > 4:
                newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": bits[4]}
            else:
                newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": "black"}
            drawing.append(newPart)
        elif shape == "c":
            newLine = input("Type in the four numbers for the added circle and a colour of your choice(optional), separated by spaces ")
            bits = newLine.split()
            if len(bits) > 4:
                newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "radius": int(bits[3]), "colour": bits[4]}
            else:
                newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "radius": int(bits[3]), "colour": "black"}
            drawing.append(newPart)
        else:
            print("input not understood")
        nextinput = input("Do you want to add another line or circle?(y/n) ")
elif option == "r":
    file_choice = input("Choose the file you want to read in: ")
    f = open(file_choice)
    nextLine = f.readline()
    while nextLine != "":
        bits = nextLine[:-1].split(",")
        if len(bits) > 4:
            newLine = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": bits[4]}
        else:
            newLine = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": "black"}
        drawing.append(newLine)
        nextLine = f.readline()

nextInput = input("Enter (d)raw, (l)ist lines/circles, (c)hange a line, (a)dd a line, (s)ave file, (q)uit: ")

while nextInput != "q":
    if nextInput == "d":
        shape = input("Do you want to draw a (l)ine or a (c)ircle? ")
        for aardvark in drawing:
            if shape == "l":
                if "len" in aardvark:
                    turtle.penup()
                    turtle.goto(aardvark["x"], aardvark["y"])
                    turtle.pendown()
                    turtle.setheading(aardvark["direction"])
                    turtle.pencolor(aardvark["colour"])
                    turtle.forward(aardvark["len"])
            if shape == "c":
                if "radius" in aardvark:
                    turtle.penup()
                    turtle.goto(aardvark["x"], aardvark["y"])
                    turtle.pendown()
                    turtle.setheading(aardvark["direction"])
                    turtle.pencolor(aardvark["colour"])
                    turtle.circle(aardvark["radius"])
        turtle.exitonclick()
    elif nextInput == "l":
        pos = 0
        for line in drawing:
            if "len" in line:
                print("{0}. ({1},{2}), direction {3}, length {4}, colour {5}".format(pos, line["x"], line["y"], line["direction"], line["len"], line["colour"]))
            elif "radius" in line:
                print("{0}. ({1},{2}), direction {3}, length {4}, colour {5}".format(pos, line["x"], line["y"], line["direction"], line["radius"], line["colour"]))
            pos += 1
    elif nextInput == "c":
        lineNum = int(input("Which line? start from zero "))
        newLine = input("Type in the four numbers for the changed line and a colour of your choice(optional), separated by spaces ")
        bits = newLine.split()
        if len(bits) > 4:
            newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": bits[4]}
        else:
            newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": "black"}
        drawing[lineNum] = newPart
    elif nextInput == "a":
        newLine = input( "Type in the four numbers for the added line and a colour of your choice(optional), separated by spaces ")
        bits = newLine.split()
        if len(bits) > 4:
            newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": bits[4]}
        else:
            newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3]), "colour": "black"}
        drawing.append(newPart)
    elif nextInput == "s":
        saveoption = int(input("Do you want to save in the same file(1) or in a new file(2)? "))
        if saveoption == 1:
            w = open("drawing.txt", "w")
            for line in drawing:
                newline = "{0},{1},{2},{3},{4}\n".format(line["x"], line["y"], line["direction"], line["len"], line["colour"])
                w.write(newline)
            w.close()
        elif saveoption == 2:
            newname = input("Enter the name of the new file(with .txt at the end): ")
            w = open(newname, "w")
            for line in drawing:
                newline = "{0},{1},{2},{3},{4}\n".format(line["x"], line["y"], line["direction"], line["len"], line["colour"])
                w.write(newline)
            w.close()
    else:
        print("input not understood")
    nextInput = input("What now? ")
