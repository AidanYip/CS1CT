import random

numHeads = 0
numTails = 0

for i in range(100):
    x = random.randint(0, 2)
    
    if x == 0 or x == 1:
        numHeads += 1
        print("heads")
    else:
        numTails += 1
        print("tails")
        
print("heads: %d tails: %d"%(numHeads, numTails))
