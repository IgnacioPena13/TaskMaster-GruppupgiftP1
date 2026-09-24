from lagga_till import lagga_till

def huvudmeny():
    print("--- To do List Program ---")
    print("1. Lägg till")
    print("2. Visa alla uppgifter")
    print("3. Ta bort \n")
    print("0. Avsluta")

    val = int(input("Välj ett av alternativen: "))
    return val

uppgifter = [] # Lista som ska innehålla alla uppgifter

while True:
    val = huvudmeny()

    if val == 1:
        uppgifter = lagga_till(uppgifter)
    elif val == 2:
        pass
    elif val == 3:
        pass
    elif val == 0:
        print("Programmet Avslutas...")
        exit()
    else:
        print("Ogiltig inmatning! ")