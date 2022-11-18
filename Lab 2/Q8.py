total = int(input("Enter a number: "))

counter = 1

number = 0

while total <= 100:
    number = int(input("Enter another number: "))
    total = total + number
    counter += 1

print("Sum:", total)
print(counter, "number(s) was/were read in")
