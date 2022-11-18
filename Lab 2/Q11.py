length = int(input("Enter a number: "))

if length == 1:
    print("□")
else:
    for i in range(length):
        for j in range(length):
            if i == 0 and j == 0:
                print("\u250C", end="")
            elif i == 0 and j == (length - 1):
                print("\u2510", end="")
            elif i == (length - 1) and j == 0:
                print("\u2514", end="")
            elif i == (length - 1) and j == (length - 1):
                print("\u2518", end="")
            elif i == 0 or i == (length - 1) and j > 0 and j < (length - 1):
                print("\u2500", end="")
            elif i > 0 and i < (length - 1) and j == 0 or j == (length - 1):
                print("\u2502", end="")
            else:
                print(" ", end="")
        print(" ")

for i in range(length):
    if i == 0:
        print("\u250C", "\u2500" * (length - 2), "\u2510")
    elif i == (length - 1):
        print("\u2514", "\u2500" * (length - 2), "\u2518")
    else:
        print("\u2502 " + " " * (length - 2) + " \u2502")
