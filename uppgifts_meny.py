from radera_todo import radera
from uppdatera import uppdatera

# Visar menyn för den valda uppgiften
def uppgifts_meny(visa_alla, uppgifter, id_uppgift):
    while True:
        uppgiftsmeny = ['Uppdatera', 'Ta bort', 'Gå tillbaka']
        print("--- Uppgiftsmeny ---")

        # Skriver ut alla menyval med nummer
        for i, e in enumerate(uppgiftsmeny):
            print(f'{i+1} - {e}')

        # Användaren väljer ett alternativ
        try:
            val_uppgift = int(input("Välj ett alternativ 1-3: "))

            if val_uppgift < 1 or val_uppgift > 3:
                raise ValueError

            if val_uppgift == 1:
                print("Du har valt: Uppdatera uppgift.")
                uppdatera(uppgifter, id_uppgift)

            elif val_uppgift == 2:
                print("Du har valt: Radera Uppgift.")
                uppgifter = radera(uppgifter, id_uppgift)

            elif val_uppgift == 3:
                print("Du har valt: Gå tillbaka.")
                visa_alla(uppgifter)

        except ValueError:
            print("Ogiltigt val. Ange ett nummer mellan 1 - 3.")
