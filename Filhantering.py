
def läsa_från_fil():
    try:
        uppgifter = []
        filnamn = "uppgifter.txt"
        fil = open(filnamn, "r")
        rader = fil.readlines()
        
        
        for rad in rader:
            delar = rad.split("|")
            ny_uppgift = {"id": int(delar[0]), "uppgift": (delar[1]), "prioritet": (delar[2].strip())}
            uppgifter.append(ny_uppgift)
        fil.close()
        return uppgifter
    except FileNotFoundError:
        return uppgifter


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
