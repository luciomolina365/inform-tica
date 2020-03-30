palabra=input("Ingrese una palabra:  ")

invertida= palabra [::-1]

AUX1= palabra.lower()
AUX2=invertida.lower()

if AUX1 == AUX2:
    print("_______________Es PALINDROMO_______________")

print("Palabra original: " + palabra)
print("Palabra invertida: " + invertida)
