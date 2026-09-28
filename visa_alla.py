def visa_alla(listan):
    print()
    print('***UPPGIFTER:***')
    for task in listan:
        print(f'{task["id"]} - {task["uppgift"]} ({task["prioritet"]})')
    val = int(input('Välj en uppgift nummer eller tryck 0 för att gå tillbaka: '))
    return(val)
