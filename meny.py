import webbrowser
from lagga_till import lagga_till
from visa_alla import visa_alla
from Filhantering import läsa_från_fil
from Filhantering import spara_till_fil


# Meny 1
def visa_meny():
    print("--- To do List Program ---")
    print("1. Lägg till uppgift")
    print("2. Visa alla uppgifter")
    print("3. Avsluta")

uppgifter = läsa_från_fil()

while True:
    visa_meny()
    val = input("Välj ett alternativ 1-3: ")
    if val == "1":
        print("Du har valt: Lägga till uppgift.")
        uppgifter = lagga_till(uppgifter)
        spara_till_fil(uppgifter)
    elif val == "2":
        print("Du har valt: Visa alla uppgifter.")
        visa_alla(uppgifter)
    elif val == "3":
        print("Taskmaster Avslutas.")
        break
    elif val.upper() == "SECRET":
        print("Du hittade den hemliga alternativet")
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
        break
    else:
        print("Ogiltigt val")
