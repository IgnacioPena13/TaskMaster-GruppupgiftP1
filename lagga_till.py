# def lagga_till(uppgifter):
#     print("--- Lägg till Uppgift ---")

#     uppg_namn = input("Skriv in uppgiftens namn: ")

#     uppg_prioritet = input("Skriv in uppgiftens prioritet (Hög, Medium eller Låg): ")

#     id = len(uppgifter) + 1

#     ny_uppgift = {
#         "id": id,
#         "uppgift": uppg_namn,
#         "prioritet": uppg_prioritet

#     }

#     uppgifter.append(ny_uppgift)

#     print("Uppgiften :)", ny_uppgift)

#     return uppgifter

def lagga_till(uppgifter):
    while True:
        try:
            print("--- Lägg till Uppgift ---")

            uppg_namn = input("Skriv in uppgiftens namn: ")
            uppg_prioritet= ""

            i_prioritet = int(input("Uppgiftens prioritet (Hög(1), Medium(2) eller Låg(3)): "))
            if  i_prioritet== 1:
                uppg_prioritet = "Hög" 
            elif i_prioritet == 2:
                uppg_prioritet = "Medium" 
            elif i_prioritet == 3:
                uppg_prioritet = "Låg" 
            else:
                raise ValueError
            id = len(uppgifter) + 1

            ny_uppgift = {
                "id": id,
                "uppgift": uppg_namn,
                "prioritet": uppg_prioritet

            }

            uppgifter.append(ny_uppgift)

            print("Uppgiften :)", ny_uppgift)

            return uppgifter
        except ValueError:
            print("Ogiltig input, försök skriva med siffror 1-3")