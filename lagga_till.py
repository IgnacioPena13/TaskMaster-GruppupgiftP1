def lagga_till(uppgifter):
    while True:
        try:
            print("--- Lägg till Uppgift ---")

            # Användaren skriver in namnet och prioritet med en siffra på den nya uppgiften
            uppg_namn = input("Skriv in uppgiftens namn: ")
            uppg_prioritet= ""

            i_prioritet = int(input("Uppgiftens prioritet (Hög(1), Medium(2) eller Låg(3)): "))
            # Översätter siffran till rätt prioritet
            if  i_prioritet== 1:
                uppg_prioritet = "Hög" 
            elif i_prioritet == 2:
                uppg_prioritet = "Medium" 
            elif i_prioritet == 3:
                uppg_prioritet = "Låg" 
            else:
                raise ValueError
            # Skapar ett nytt ID för uppgiften
            id = len(uppgifter) + 1
                    
            # Skapar en dictionary med uppgiftens ID, namn och prioritet
            ny_uppgift = {
                "id": id,
                "uppgift": uppg_namn,
                "prioritet": uppg_prioritet
            }
            
            # Lägger till den nya uppgiften i listan
            uppgifter.append(ny_uppgift)

            print("Uppgiften :)", ny_uppgift)

            return uppgifter
        
        except ValueError:
            print("Ogiltig input, försök skriva med siffror 1-3")