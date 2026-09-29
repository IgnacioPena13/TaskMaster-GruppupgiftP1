import Filhantering as fh

def uppdatera(data, uppgiftId):
    while True:
        try:
            for i in data: #checkar om det finns en upppgiftmed id man har skrivit
                if i["id"] == uppgiftId:
                    ny_namn = input("Uppgift: ")
                    ny_prio_nr = int(input("Prio (Hög(1), Medium(2) eller Låg(3)): "))
                    ny_prio = ""
                    if  ny_prio_nr== 1:
                        ny_prio = "Hög" 
                    elif ny_prio_nr == 2:
                        ny_prio = "Medium" 
                    elif ny_prio_nr == 3:
                        ny_prio = "Låg" 
                    else:
                        raise ValueError
                    i['uppgift'] = ny_namn
                    i['prioritet'] = ny_prio
                    print(f"Uppgiften nr {uppgiftId} - {i['uppgift']} uppdateras...")
            print('***UPPGIFTER:***')
            for j in data: #printas igen data utan den uppgift man ville ta bort
                print(f'{j["id"]} - {j["uppgift"]} ({j["prioritet"]})')
            fh.spara_till_fil(data)
            print()
            return(data)
        except ValueError:
            print("Ogiltig input, försök skriva med siffror 1-3")


        





