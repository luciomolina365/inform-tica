def leer(auxDatos):
    auxDatos.clear()
    auxDatos.append(input("Ingrese el nombre del jugador:  "))
    
    if auxDatos[0] != "ZZZ":
        auxDatos.append(int(input("Ingrese el nivel del jugador:  ")))
        auxDatos.append(int(input("Ingrese el puntaje max del jugador:  ")))
        auxDatos.append(input("Ingrese tiempo de juego:  "))
    
   


diccionario={}
auxDatos=[]

leer(auxDatos)
while auxDatos[0] != "ZZZ":
    
    nom = auxDatos[0]
    auxDatos.remove(nom)
    diccionario[nom] = auxDatos[:] 

    leer(auxDatos)

auxDatos.clear()

print(diccionario)



lista_diccionario=(sorted(diccionario , key=lambda usuario : diccionario[usuario][1]))

lista_diccionario_INVERTIDA = (list(reversed(lista_diccionario)))


print("TOP " + str(len(diccionario)) + "\n" +"="*40)
i=1
for NOM in lista_diccionario_INVERTIDA:
    print( str(i) + "_ " + NOM + " ---> " + str(diccionario[NOM][1]) + "pts" )
    i+=1
print("="*40)