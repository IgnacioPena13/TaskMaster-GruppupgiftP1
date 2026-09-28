import webbrowser
import radera_todo
from lagga_till import lagga_till

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
            print("Du har valt: Radera Uppgift.")


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
        break
    else:
        print("Ogiltigt val")

