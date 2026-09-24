def lagga_till(uppgifter):
    print("--- Lägg till Uppgift ---")

    uppg_namn = input("Skriv in uppgiftens namn: ")

    uppg_prioritet = input("Skriv in uppgiftens prioritet (Hög, Medium eller Låg): ")

    id = len(uppgifter) + 1

    ny_uppgift = {
        "id": id,
        "uppgift": uppg_namn,
        "prioritet": uppg_prioritet

    }

    uppgifter.append(ny_uppgift)

    print("Uppgiften :)", ny_uppgift)

    return uppgifter