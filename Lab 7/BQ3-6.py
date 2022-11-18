f = open("glossaryTerms.txt")

terms = {}
changed = False

nextLine = f.readline()
while nextLine != "":
    bits = nextLine[:-1].split(":::")
    terms[bits[0]] = bits[1] 
    nextLine = f.readline()


nextInput = input("Enter (l)ookup, (p)retty print, (a)dd an entry, (s)ave, (sa)ve as, (d)elete an entry, (q)uit: ")

while nextInput != "q":
    if nextInput == "l":
        term = input("What are you looking for? ")
        if term in terms:
            print(terms[term])
        else:
            print("That is not in the glossary.")
            
    elif nextInput == "p":
        outF = open("prettyGlossary.html", "w")
        outF.write("<h1>Glossary</h1>")
        for term in terms:
            outF.write("<h3>{0}</h3>".format(term))
            outF.write("<p>{0}</p>".format(terms[term]))
        outF.close()
        
    elif nextInput == "a":
        term = input("Please enter a new term: ")
        explain = input("Please type the explantion of the new term: ")
        terms[term] = explain
        print("Updated glossary:", terms)
        changed = True

    elif nextInput == "s":
        if changed == True:
            w = open("glossaryTerms.txt", "w")
            for term in terms:
                newline = "{0}:::{1}\n".format(term, terms[term])
                w.write(newline)
            w.close()
            
    elif nextInput == "sa":
        filename = input("Create a name for the file (with .txt): ")
        w = open(filename, "w")
        for term in terms:
            newline = "{0}:::{1}\n".format(term, terms[term])
            w.write(newline)
        w.close()

    elif nextInput == "d":
        term = input("Enter a term you want to delete: ")
        if term in terms:
            terms.pop(term)
            print("{0} deleted successfully".format(term))
        else:
            print("That is not in the glossary.")
        
    else:
        print("Not implemented yet")
    nextInput = input("what next? ")
