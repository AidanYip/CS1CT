import random

numHeads = 0
numTails = 0

for i in range(1000):
    x = random.randint(0, 1)
    
    if x == 0:
        numHeads += 1
        print("heads")
    else:
        numTails += 1
        print("tails")
        
print("heads: %d tails: %d"%(numHeads, numTails))
