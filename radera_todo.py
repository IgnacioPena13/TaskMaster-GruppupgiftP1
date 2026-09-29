#leta efter en specifik todo för att ta bort denn och printa både DONE och listan kvar
import Filhantering as fh

def radera(data, uppgiftId):
    try:
        print('VILL DU RADERA DE HÄR UPPGIFTER? (j/n)')
        radera_id = input('> ').lower()
        if radera_id == "j":
            for i in data: #checkar om det finns en upppgiftmed id man har skrivit
                if i["id"] == uppgiftId:
                    data.pop(uppgiftId-1)
                    for index, uppgift in enumerate(data):
                        uppgift["id"] = index + 1
            for j in data: #printas igen data utan den uppgift man ville ta bort
                print(f'{j}')
            print("Uppgiften raderas...")
            fh.spara_till_fil(data)
        elif radera_id =='n':
            print("Uppgiften ska inte raderas")
        return(data)
    except:
        print("Något gick fel")