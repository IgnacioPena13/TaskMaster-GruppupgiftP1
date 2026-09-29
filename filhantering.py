
# Läser in alla sparade uppgifter från textfilen
def läsa_från_fil():
    try:
        
        # Skapar en tom lista där uppgifterna ska sparas
        uppgifter = []
        
        # Namnet på filen som ska läsas
        filnamn = "uppgifter.txt"
        
        # Öppnar filen i läsläge ("r")
        fil = open(filnamn, "r")
       
        # Läser in alla rader från filen
        rader = fil.readlines()
        
        # Går igenom en rad i taget
        for rad in rader:
            
            # Delar upp raden vid | i tre delar
            delar = rad.split("|")
            
            # Skapar en dictionary av informationen från raden
            # ID omvandlas till int och strip() tar bort t.ex. \n
            ny_uppgift = {"id": int(delar[0]), "uppgift": (delar[1]), "prioritet": (delar[2].strip())}
           
            # Lägger till uppgiften i listan
            uppgifter.append(ny_uppgift)
        
        # Stänger filen efter att den har lästs    
        fil.close()
        
        # Skickar tillbaka listan med alla uppgifter
        return uppgifter
    
    # Om filen inte finns ska programmet inte krascha
    except FileNotFoundError:
        return uppgifter

# Sparar alla uppgifter från listan till textfilen
def spara_till_fil(uppgifter):
    
    # Namnet på filen som uppgifterna ska sparas i
    filnamn = "uppgifter.txt"
    
    # Öppnar filen i skrivläge ("w")
    fil = open(filnamn, "w")
    
    # Går igenom varje uppgift i listan
    for uppgift in uppgifter:
        
        # Skriver id, uppgift och prioritet separerade med |
        fil.write(str(uppgift["id"]))
        fil.write("|")
        fil.write(uppgift["uppgift"])
        fil.write("|")
        fil.write(uppgift["prioritet"])
        
        # Gör en ny rad inför nästa uppgift
        fil.write("\n")
    
    # Stänger filen när allt har sparats
    fil.close()
