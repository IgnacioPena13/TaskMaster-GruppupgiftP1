import webbrowser
import radera_todo
from lagga_till import lagga_till
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





# Meny 1 
def visa_meny():
    print("--- To do List Program ---")
    print("1. Lägg till uppgift")
    print("2. Visa alla uppgifter")
    print("3. Avsluta")

# Meny 2
def uppgifts_meny():

    while True:
        print("--- Uppgiftsmeny ---")
        print("1. Uppdatera uppgift")
        print("2. Radera Uppgift")
        print("3. Gå tillbaka")
        val_uppgift = input("Välj ett alternativ 1-3: ")
        if val_uppgift == "1":
            print("Du har valt: Uppdatera uppgift.")
        elif val_uppgift == "2":
            while True:
                try:
                    print("Du har valt: Radera Uppgift.")
                    läsa_från_fil()
                    uppgiftId = int(input("Id på uppgift du vill ta bort?"))
                    if uppgiftId <= 0:
                        raise ValueError
                    radera_todo.radera(int(uppgiftId))
                    break
                except ValueError:
                    print("Ogiltig Id")
        elif val_uppgift == "3":
            print("Du har valt: Gå tillbaka.")
            break
        else:
            print("Ogiltigt val")
        
while True:
    visa_meny()
    val = input("Välj ett alternativ 1-3: ")
    if val == "1":
        print("Du har valt: Lägga till uppgift.")
        uppgifter = lagga_till(uppgifter)
    elif val == "2":
        print("Du har valt: Visa alla uppgifter.")
        uppgifts_meny()
        # Här ska Student 1 visa_alla_uppgifter() köras
    elif val == "3":
        print("Taskmaster Avslutas.")
        break
    elif val == "secret":
        print("Du hittade den hemliga alternativet")
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
        break
    else:
        print("Ogiltigt val")