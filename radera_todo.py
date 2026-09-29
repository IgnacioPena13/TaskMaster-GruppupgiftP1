#leta efter en specifik todo för att ta bort denn och printa både DONE och listan kvar
import Filhantering as fh
#Behöver lite ändringar än
def radera(uppgiftId):
    try:
            data = fh.läsa_från_fil()
            print("uppgiften raderas...")
            for i in data: #checkar om det finns en upppgiftmed id man har skrivit
                if i["id"] == uppgiftId:
                    data.pop(uppgiftId-1)
            for j in data: #printas igen data utan den uppgift man ville ta bort
                print(f'{j}', end='\n')
            print('VILL DU SPARA DE HÄR UPPGIFTER? (j/n)')
            spara = input('> ').lower()
            if spara == "j":
                print('Data sparas...')
                fh.spara_till_fil(data)
            elif spara =='n':
                print("Data ska inte sparas")
    except:
        print("Något gick fel")