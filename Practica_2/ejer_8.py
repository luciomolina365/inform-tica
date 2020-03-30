cadena = input("Ingrese una cadena : ")

lista = []

cadena = cadena.replace(" ", "")

for letra in cadena:

    n = cadena.count(letra)
    
    cantDivisiones=0

    aux=1
    while (aux <= n) and (cantDivisiones < 4 ):
        
        if n % aux == 0:
            cantDivisiones=cantDivisiones+1
        
        aux=aux + 1

    if cantDivisiones == 2:
        lista.append(letra)
    
    cadena= cadena.replace(letra, "")
    print("La letra " + str(letra) + " aparece: "+ str(n) +" veces") 
    print(cadena)

print("")
print(lista)


