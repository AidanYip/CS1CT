f = open( "pairs.txt" )

number = int( f.readline() )

for n in range( number ):
    n1 = int( f.readline() )
    n2 = int( f.readline() )
    n3 = n1 + n2
    print( n3 )

a=1
b=2
print(a)
print(b)
