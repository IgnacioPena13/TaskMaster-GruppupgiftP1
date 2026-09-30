#leta efter en specifik todo för att ta bort denn och printa både DONE och listan kvar
import Filhantering as fh

# Tar bort en vald uppgift från listan
def radera(data, uppgiftId):
    while True:     
        try:
            # Checkar om det finns en upppgiftmed id man har skrivit
            print('VILL DU RADERA DE HÄR UPPGIFTER? (j/n)')
            radera_id = input('> ').lower()
            if radera_id == "j":
                for i in data: 
                    if i["id"] == uppgiftId:
                        data.pop(uppgiftId-1)
                        print(f"Uppgiften nr {uppgiftId} - {i['uppgift']} raderas...")
                        # Uppdaterar ID för uppgifterna efter den raderade uppgiften
                        for index, uppgift in enumerate(data):
                            uppgift["id"] = index + 1
                # Printas igen data utan den uppgift man ville ta bort
                print('***UPPGIFTER:***')
                for j in data: 
                    print(f'{j["id"]} - {j["uppgift"]} ({j["prioritet"]})')
                # Sparar den uppdaterade listan till filen
                fh.spara_till_fil(data)

            elif radera_id =='n':
                print(f"Uppgiften nr {uppgiftId} ska inte raderas")
            else:
                raise ValueError
            return(data)
        
        except ValueError:
            print("du måste skriva 'j' eller 'n'")