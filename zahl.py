import random

# Statistik-Zähler
gewonnen_gesamt = 0
verloren_gesamt = 0

weiterspielen = "ja"

while weiterspielen.lower() == "ja":
    zahl = random.randint(1, 20)
    tries = 0
    gewonnen = False

    print("\nNeues Spiel gestartet!")

    while tries < 5:
        try:
            answer = int(input("Rate eine Zahl zwischen 1 und 20: "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue

        if answer < zahl:
            print("Zu klein!")
        elif answer > zahl:
            print("Zu groß!")
        else:
            print("Glückwunsch! Du hast richtig geraten!")
            gewonnen = True
            gewonnen_gesamt += 1
            break

        tries += 1

    if not gewonnen:
        print(f"Keine Versuche mehr. Die richtige Zahl war: {zahl}")
        verloren_gesamt += 1

    weiterspielen = input("Möchtest du nochmal spielen? (ja/nein): ")

# Statistik anzeigen
print("\nSpielstatistik:")
print(f"Gewonnen: {gewonnen_gesamt} Mal")
print(f"Verloren: {verloren_gesamt} Mal")
print("Danke fürs Spielen!")
