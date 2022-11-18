length = int(input("Enter a number: "))

#square
for i in range(length):
    print("*" * length)

#empty square
for i in range(length):
    for j in range(length):
        print("*" if i in (0, length - 1) or j in (0, length - 1) else " ", end=" ")
    print(" ")

#empty square2
for i in range(length):
    for j in range(length):
        if i == 0 and j == 0:
            print("*", end=" ")
        elif i == 0 and j == (length - 1):
            print("*", end=" ")
        elif i == (length - 1) and j == 0:
            print("*", end=" ")
        elif i == (length - 1) and j == (length - 1):
            print("*", end=" ")
        elif i == 0 or i == (length - 1) and j < (length - 1) and j > 0:
            print("*", end=" ")
        elif i > 0 and i < (length - 1) and j == 0 or j == (length - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")

#empty square3
for i in range(length):
    if i == 0 or i == (length - 1):
        print("* " * length)
    else:
        print("* " + "  " * (length - 2) + "*")
