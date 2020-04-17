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


#Busco e imprimo al jugador con mayor puntaje
max=0
for jugador in diccionario:

    if diccionario[jugador]["PuntajeMAX"] > max:
        max = diccionario[jugador]["PuntajeMAX"]
        maxNom = jugador




print("Jugador con mayor puntaje: " + maxNom + "\n" + "-"*60)

#aux = sorted(diccionario, key=lambda C:  )
#print(aux)

print(diccionario)

# print('enter your name')
# name=input()
# print('your name is   ' + name)

# jugadores = {
#     'fede': {'nivel':3,'puntaje':4,'tiempo':200}, 
#     'belen': {'nivel':4,'puntaje':6,'tiempo':300}, 
#     'juan': {'nivel':5,'puntaje':7,'tiempo':400}
#     }

# # Imprimir los primeros 2 jugadores ordenados por puntaje
# # ('fede', {'nivel': 3, 'puntaje': 4, 'tiempo': 200})
# # Con reverse
# print(sorted(jugadores.items(), key = lambda jugador: jugador[1]['puntaje'], reverse=True)[:2])
# # Con slicing negativo
# print(sorted(jugadores.items(), key = lambda jugador: jugador[1]['puntaje'])[:-3:-1])

# # Imprimir los primeros 2 jugadores ordenados por nombre
# # ('fede', {'nivel': 3, 'puntaje': 4, 'tiempo': 200})
# a = lambda jugador: jugador[0]
# print(sorted(jugadores.items(), key = a))

# def fa(jugador): 
#    return jugador[0]

# print(sorted(jugadores.items(), key = fa))
