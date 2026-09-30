from uppgifts_meny import uppgifts_meny

def visa_alla(listan):
    while True:
        print()
        print('***UPPGIFTER:***')
        
        # Visar alla uppgifter i listan med ID, namn och prioritet
        for task in listan:
            print(f'{task["id"]} - {task["uppgift"]} ({task["prioritet"]})')
        print()

        # Användaren väljer en uppgift genom att ange dess ID eller skriver 0 för att gå tillbaka till huvudmenyn
        try:
            val = int(input('Välj en uppgift nummer eller tryck 0 för att gå tillbaka: '))
            print(f'Du har valt: {val}')
            if val == 0:
                print()
                return
            elif val < 1 or val > len(listan):
                print(f"Ogiltigt nummer. Ange ett nummer mellan 1 - {len(listan)}, eller 0 för att gå tillbaka.")
            else:
                uppgifts_meny(visa_alla, listan, val)

        except ValueError:
            print(f"Ogiltigt val. Ange ett nummer mellan 1 - {len(listan)}, eller 0 för att gå tillbaka.")
