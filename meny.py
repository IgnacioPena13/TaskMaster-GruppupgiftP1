import webbrowser
import radera_todo
from lagga_till import lagga_till

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
        uppgifter = lagga_till(uppgifter)
    elif val == "2":
        print("Du har valt: Visa alla uppgifter.")
        # Här ska Student 1 visa_alla_uppgifter() köras
    elif val == "3":
        print("Du har valt: Ta bort uppgift.")
        radera_todo.radera()
    elif val == "4":
        print("Taskmaster Avslutas.")
        break
    elif val == "secret":
        print("Du hittade den hemliga alternativet")
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
        break
    else:
        print("Ogiltigt val")
