
def uppgifts_meny():
    uppgiftsmeny = ['Uppdatera', 'Ta bort', 'Gå tillbaka']
    print("--- Uppgiftsmeny ---")
    for i, e in enumerate(uppgiftsmeny):
        print(f'{i+1} - {e}')

    val_uppgift = input("Välj ett alternativ 1-3: ")

    if val_uppgift == "1":
        print("Du har valt: Uppdatera uppgift.")

    elif val_uppgift == "2":
        print("Du har valt: Radera Uppgift.")

    elif val_uppgift == "3":
        print("Du har valt: Gå tillbaka.")
        # break
    else:
        print("Ogiltigt val")


