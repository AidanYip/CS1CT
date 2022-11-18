File = open("numbers.txt")

runtotal = 0
walktotal = 0

for i in range(10):
    run = int(File.readline())
    walk = int(File.readline())
    runtotal = runtotal + run
    walktotal = walktotal + walk

print("Total time ran: ",runtotal)
print("Total time walked: ",walktotal)
