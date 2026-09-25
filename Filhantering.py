

def spara_till_fil(uppgifter):
    filnamn = "uppgifter.txt"
    fil = open(filnamn, "w")
    
    
    for uppgift in uppgifter:
        fil.write(str(uppgift["id"]))
        fil.write("|")
        fil.write(uppgift["uppgift"])
        fil.write("|")
        fil.write(uppgift["prioritet"])
        fil.write("\n")
    fil.close()


def läsa_från_fil():
