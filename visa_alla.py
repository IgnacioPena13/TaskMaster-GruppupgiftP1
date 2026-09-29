from uppgifts_meny import uppgifts_meny

def visa_alla(listan):
    print()
    print('***UPPGIFTER:***')
    for task in listan:
        print(f'{task["id"]} - {task["uppgift"]} ({task["prioritet"]})')
    print()
    val = int(input('Välj en uppgift nummer eller tryck 0 för att gå tillbaka: '))
    print(f'Du har valt: {val}')

    if val == 0:
        print()
    else:
        # FELHANTERING - if val is valid id
        uppgifts_meny(visa_alla, listan)
    # return(val)
