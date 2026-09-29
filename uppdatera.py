import Filhantering as fh

def uppdatera(data, uppgiftId):
    # try:
        for i in data: #checkar om det finns en upppgiftmed id man har skrivit
            if i["id"] == uppgiftId:
                ny_namn = input("Uppgift: ")
                ny_prio = input("Prio: ")
                i['uppgift'] = ny_namn
                i['prioritet'] = ny_prio
                print(f"Uppgiften nr {uppgiftId} - {i['uppgift']} uppdateras...")
        print('***UPPGIFTER:***')
        for j in data: #printas igen data utan den uppgift man ville ta bort
            print(f'{j["id"]} - {j["uppgift"]} ({j["prioritet"]})')
        fh.spara_till_fil(data)
        print()
        return(data)
    # except:
    #     print("Något gick fel")




