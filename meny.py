import webbrowser
# import radera_todo
# from lagga_till import lagga_till
from visa_alla import visa_alla

# Fejkdata för testning, kommer att ersättas med filhantering.
uppgifter = [
    {"id": 1, "uppgift": "Vattna blommorna", "prioritet": "Medium"},
    {"id": 2, "uppgift": "Handla mat", "prioritet": "Hög"},
    {"id": 3, "uppgift": "Laga lunch", "prioritet": "Hög"},
    {"id": 4, "uppgift": "Diska", "prioritet": "Låg"},
    {"id": 5, "uppgift": "Städa vardagsrummet", "prioritet": "Medium"},
    {"id": 6, "uppgift": "Tvätta kläder", "prioritet": "Låg"},
    {"id": 7, "uppgift": "Betala räkningar", "prioritet": "Hög"},
    {"id": 8, "uppgift": "Träna", "prioritet": "Medium"},
    {"id": 9, "uppgift": "Läsa 20 sidor", "prioritet": "Låg"},
    {"id": 10, "uppgift": "Boka tandläkartid", "prioritet": "Medium"},
]

# Meny 1
def visa_meny():
    print("--- To do List Program ---")
    print("1. Lägg till uppgift")
    print("2. Visa alla uppgifter")
    print("3. Avsluta")

# Meny 2
# def uppgifts_meny():

#     while True:
#         print("--- Uppgiftsmeny ---")
#         print("1. Uppdatera uppgift")
#         print("2. Radera Uppgift")
#         print("3. Gå tillbaka")
#         val_uppgift = input("Välj ett alternativ 1-3: ")
#         if val_uppgift == "1":
#             print("Du har valt: Uppdatera uppgift.")

#         elif val_uppgift == "2":
#             print("Du har valt: Radera Uppgift.")


#         elif val_uppgift == "3":
#             print("Du har valt: Gå tillbaka.")
#             break
#         else:
#             print("Ogiltigt val")

while True:
    visa_meny()
    val = input("Välj ett alternativ 1-3: ")
    if val == "1":
        print("Du har valt: Lägga till uppgift.")
        uppgifter = lagga_till(uppgifter)
    elif val == "2":
        print("Du har valt: Visa alla uppgifter.")
        visa_alla(uppgifter)
        # Här ska Student 1 visa_alla_uppgifter() köras
    elif val == "3":
        print("Taskmaster Avslutas.")
        break
    elif val == "secret":
        print("Du hittade den hemliga alternativet")
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
        break
    else:
        print("Ogiltigt val")








    # while True:

    # huvudmeny_val = huvudmeny(huvudmeny_lista)

    # if huvudmeny_val == 1:
    #     listan_val = visa_alla(uppgifter)
    #     if listan_val == 0:
    #             continue
    #     else:
    #         uppgift(listan_val)
    # elif huvudmeny_val == 2:
    #     lagga_till()
    # elif huvudmeny_val == 3:
    #     avsluta()
