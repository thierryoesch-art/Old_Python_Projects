a = float(input("Die erste Zahl:   "))
b = float(input("Die zweite Zahl:   "))
op = input("Rechenart (+, -, *, /):   ")


if op == "+":
    ergebnis = a + b
elif op == "-":
    ergebnis = a - b
elif op == "*":
    ergebnis = a * b
elif op == "/":
    ergebnis = a / b
else:
    print("Bitte eine Valide Rechenart eingeben!")
    ergebnis = None


if ergebnis is not None:
    print("Resultat = " , ergebnis)
