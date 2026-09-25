# TaskMaster-GruppupgiftP1

TaskMaster är ett terminalbaserat To-Do-system skapat som en gruppuppgift i kursen Programmering 1.

Programmet låter användaren skapa, visa och ta bort uppgifter. Uppgifterna sparas i en textfil så att de finns kvar även efter att programmet har stängts.

## Funktioner

TaskMaster ska kunna:

- Lägga till en ny uppgift
- Välja prioritet: Hög, Medium eller Låg
- Visa alla sparade uppgifter
- Ta bort en uppgift med ID eller namn
- Spara uppgifter i `uppgifter.txt`
- Läsa in tidigare uppgifter när programmet startas
- Hantera felaktig input utan att programmet kraschar

## Meny

När programmet startas visas följande meny:

1. Lägg till uppgift
2. Visa alla uppgifter
3. Ta bort uppgift
4. Avsluta

Programmet fortsätter köras tills användaren väljer att avsluta.

## Datastruktur

Uppgifterna lagras med hjälp av en lista av dictionaries.

Exempel:

```python
uppgifter = [
    {
        "id": 1,
        "uppgift": "Handla",
        "prioritet": "Hög"
    }
]
