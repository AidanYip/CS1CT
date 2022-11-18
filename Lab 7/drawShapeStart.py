import turtle

f = open( "drawing.txt" )

drawing = []

nextLine = f.readline()
while nextLine != "":
    bits = nextLine[ : - 1 ].split( "," )

    newLine = { "x": int( bits[ 0 ] ), "y": int( bits[ 1 ] ), "direction": int( bits[ 2 ] ), "len": int( bits[ 3 ] ) }
    drawing.append( newLine )
    
    nextLine = f.readline()

nextInput = input( "Enter (d)raw, (l)ist lines, (c)hange a line, (q)uit: " )

while nextInput != "q":
    if nextInput == "d":
        for aardvark in drawing:
            turtle.penup()
            turtle.goto( aardvark[ "x" ], aardvark[ "y" ] )
            turtle.pendown()
            turtle.setheading( aardvark[ "direction" ] )
            turtle.forward( aardvark[ "len" ] )
        turtle.exitonclick()
    elif nextInput == "l":
        pos = 0
        for line in drawing:
            print("({0},{1}), direction {2}, length {3}".format( line["x"],line["y"],line["direction"],line["len"] ) )
            pos += 1
    elif nextInput == "c":
        lineNum = int( input( "Which line? start from zero" ) )
        newLine = input( "Type in the four numbers for the changed line, separated by spaces" )
        bits = newLine.split()
        newPart = { "x": int( bits[ 0 ] ), "y": int( bits[ 1 ] ), "direction": int( bits[ 2 ] ), "len": int( bits[ 3 ] ) }
        drawing[ lineNum ] = newPart
    else:
        print( "input not understood" )
    nextInput = input( "What now? " )
