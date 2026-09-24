#leta efter en specifik todo för att ta bort denn och printa både DONE och listan kvar
import json

def radera():
    with open("dummy.txt","r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)
        print('id på uppgiften du vill ta bort?')
        id_radera = int(input('> '))
        print("uppgiften raderas...")
        for i in data:
            if i["id"] == id_radera:
                data.pop(id_radera-1)
        for j in data:
            print(f'Uppgift: {j["uppgift"]}:\nPrioritet: {j["prioritet"]}')