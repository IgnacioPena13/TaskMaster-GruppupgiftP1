import webbrowser

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


def visa_meny():
    print("--- To do List Program ---")
    print("1. Lägg till uppgift")
    print("2. Visa alla uppgifter")
    print("3. Ta bort uppgift")
    print("4. Avsluta")
while True:
    visa_meny()
    val = input("Välj ett alternativ 1-4: ")
    if val == "1":
        print("Du har valt: Lägga till uppgift.")
        # Här ska Student 1 lägg_till_uppgift() köras
    elif val == "2":
        print("Du har valt: Visa alla uppgifter.")
        # Här ska Student 1 visa_alla_uppgifter() köras
    elif val == "3":
        print("Du har valt: Ta bort uppgift.")
        # Här ska Student 1 ta_bort_uppgift() köras
    elif val == "4":
        print("Taskmaster Avslutas.")
        break
    elif val == "secret":
        print("Du hittade den hemliga alternativet")
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
        break
    else:
        print("Ogiltigt val")