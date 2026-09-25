#leta efter en specifik todo för att ta bort denn och printa både DONE och listan kvar
import json

def radera():
    with open("dummy.txt","r", encoding="utf-8") as f:
        data = json.load(f) #ska vara en lista med dictionaries
        for j in data:
            print(f'{j}', end='\n')
        print('id på uppgiften du vill ta bort?')
        id_radera = int(input('> '))
        print("uppgiften raderas...")
        for i in data: #checkar om det finns en upppgiftmed id man har skrivit
            if i["id"] == id_radera:
                data.pop(id_radera-1)
        for j in data: #printas igen data utan den uppgift man ville ta bort
            print(f'{j}', end='\n')
        print('VILL DU SPARA DE HÄR UPPGIFTER? J/N')
        spara = input('> ')
        #koden/funktionen till filhantering