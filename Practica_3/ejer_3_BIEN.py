def leer(Datos):
    nombre = input("Ingrese el nombre del jugador:  ")
    
    if nombre != "ZZZ":
        Datos[nombre]={}
        Datos[nombre]["Nivel"] = (int(input("Ingrese el nivel del jugador:  ")))
        Datos[nombre]["PuntajeMAX"] = (int(input("Ingrese el puntaje max del jugador:  ")))
        Datos[nombre]["Tiempo"] = (input("Ingrese tiempo de juego:  "))

    return nombre



#Lleno la estrutura de datos
diccionario={}
nombre = leer(diccionario)
while nombre != "ZZZ":

    nombre = leer(diccionario)


#Imprimo todos los jugadores
print( "-" *25 + "Jugadores" + "-" *26 + "\n" + str(diccionario.keys()).replace("dict_keys","") + "\n" + "-"*60)

# Imprimir los primeros 2 jugadores ordenados por puntaje 
print("Imprimir los primeros 2 jugadores ordenados por puntaje (CON REVERSE)"+ "\n")
# Con reverse
print(sorted(diccionario.items(), key = lambda jugador: jugador[1]['PuntajeMAX'], reverse=True)[:2])

print("-"*60 + "\n")
print("Imprimir los primeros 2 jugadores ordenados por puntaje (CON SLICING NEGATIVO)"+ "\n")
# Con slicing negativo
print(sorted(diccionario.items(), key = lambda jugador: jugador[1]['PuntajeMAX'])[:-3:-1])
print("-"*60 + "\n")


# Imprimir los primeros 2 jugadores ordenados por nombre
 
a = lambda jugador: jugador[0]
print(sorted(diccionario.items(), key = a)[:2])

def fa(jugador): 
   return jugador[0]

print(sorted(diccionario.items(), key = fa)[:2])