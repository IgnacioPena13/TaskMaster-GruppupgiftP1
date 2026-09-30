#leta efter en specifik todo för att ta bort denn och printa både DONE och listan kvar
import Filhantering as fh

def radera(data, uppgiftId):
    while True:     
        try:
            print('VILL DU RADERA DE HÄR UPPGIFTER? (j/n)')
            radera_id = input('> ').lower()
            if radera_id == "j":
                for i in data: #checkar om det finns en upppgiftmed id man har skrivit
                    if i["id"] == uppgiftId:
                        data.pop(uppgiftId-1)
                        print(f"Uppgiften nr {uppgiftId} - {i['uppgift']} raderas...")
                        for index, uppgift in enumerate(data):
                            uppgift["id"] = index + 1
                print('***UPPGIFTER:***')
                for j in data: #printas igen data utan den uppgift man ville ta bort
                    print(f'{j["id"]} - {j["uppgift"]} ({j["prioritet"]})')
                fh.spara_till_fil(data)
            elif radera_id =='n':
                print(f"Uppgiften nr {uppgiftId} ska inte raderas")
            else:
                raise ValueError
            return(data)
        except ValueError:
            print("du måste skriva 'j' eller 'n'")