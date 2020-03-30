cadena = input("Ingrese una cadena : ")

lista = []

cadena = cadena.replace(" ", "")

i=0
while cadena != "":
    
    letra=cadena[i]
    n = cadena.count(letra)

    print("La letra " + str(letra) + " aparece: "+ str(n) +" veces") 
    cantDivisiones=0

    aux=1
    while (aux <= n) and (cantDivisiones < 4 ):
        
        if n % aux == 0:
            cantDivisiones=cantDivisiones+1
        
        aux=aux + 1

    if cantDivisiones == 2:
        lista.append(letra)

    cadena=cadena.replace(letra,"")


print("Por lo tanto las letras " + str(lista) + " son letras que aparecen un número primo de veces.")

