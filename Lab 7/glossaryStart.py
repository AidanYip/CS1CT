f = open( "glossaryTerms.txt" )

terms = {}

nextLine = f.readline()
while nextLine != "":
    bits = nextLine[ :-1 ].split( ":::" )
    terms[ bits[ 0 ] ] = bits[ 1 ] 
    nextLine = f.readline()


nextInput = input( "Enter (l)ookup, (p)retty print, (q)uit: " )

while nextInput != "q":
    if nextInput == "l":
        term = input( "What are you looking for? " )
        if term in terms:
            print( terms[ term ] )
        else:
            print( "That is not in the glossary." )
        
    elif nextInput == "p":
        outF = open( "prettyGlossary.html", "w" )
        outF.write( "<h1>Glossary</h1>" )
        for term in terms:
            outF.write( "<h3>{0}</h3>".format( term ) )
            outF.write( "<p>{0}</p>".format( terms[ term ] ) )
        outF.close()
    else:
        print( "Not implemented yet" )
    nextInput = input( "what next? " )
