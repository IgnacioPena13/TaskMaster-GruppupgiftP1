import Filhantering as fh

# Uppdaterar en befintlig uppgift med nytt namn och ny prioritet
def uppdatera(data, uppgiftId):
    while True:
        try:
            #Checkar om det finns en upppgift med id man har skrivit
            for i in data: 
                if i["id"] == uppgiftId:
                    # Användaren skriver in det nya namnet och prioriteten med en siffra
                    ny_namn = input("Skriv in den nya uppgiften: ")
                    ny_prio_nr = int(input("Prio (Hög(1), Medium(2) eller Låg(3)): "))
                    # Översätter siffran till rätt prioritet
                    ny_prio = ""
                    if  ny_prio_nr== 1:
                        ny_prio = "Hög" 
                    elif ny_prio_nr == 2:
                        ny_prio = "Medium" 
                    elif ny_prio_nr == 3:
                        ny_prio = "Låg" 
                    else:
                        raise ValueError
                    # Uppdaterar uppgiftens namn och prioritet
                    i['uppgift'] = ny_namn
                    i['prioritet'] = ny_prio
                    # Bekräftar att uppgiften har uppdaterats
                    print(f"Uppgiften nr {uppgiftId} - {i['uppgift']} uppdateras...")
            
            # Printas igen data utan den uppgift man ville ta bort
            print('***UPPGIFTER:***')
            for j in data: 
                print(f'{j["id"]} - {j["uppgift"]} ({j["prioritet"]})')
            # Sparar den uppdaterade listan till filen
            fh.spara_till_fil(data)
            print()
            return(data)
        
        except ValueError:
            print("Ogiltig input, försök skriva med siffror 1-3")


        





