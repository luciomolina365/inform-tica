def leer(Datos):
    nombre = input("Ingrese el nombre del jugador:  ")
    
    if nombre != "ZZZ":
        
        Datos[nombre]={}
        Datos[nombre]["Apellido"] = str(input("Ingrese su apellido:  ")) 
        Datos[nombre]["Nivel"] = (int(input("Ingrese el nivel del jugador:  ")))
        Datos[nombre]["PuntajeMAX"] = (int(input("Ingrese el puntaje max del jugador:  ")))
        Datos[nombre]["Tiempo"] = (str(input("Ingrese tiempo de juego en horas:  "))+ " Horas")

    return nombre



#Lleno la estrutura de datos
diccionario={}
nombre = leer(diccionario)
while nombre != "ZZZ":

    nombre = leer(diccionario)


#Imprimo todos los jugadores
print( "-" *25 + "Jugadores" + "-" *26 + "\n" + str(diccionario.keys()).replace("dict_keys","") + "\n" + "-"*60)


print("Imprimir los primeros 10 jugadores ordenados por puntaje (CON REVERSE)"+ "\n")
print(sorted(diccionario.items(), key = lambda jugador: jugador[1]['PuntajeMAX'], reverse=True)[:10])
print("-"*60 + "\n")



# Imprimir los jugadores ordenados por apellido
print(sorted(diccionario.items(), key = lambda jugador: jugador[1]["Apellido"]))


# Imprimir los jugadores ordenados por nivel
def nivel(jugador): 
   return jugador[1]["Nivel"]

print(sorted(diccionario.items(), key = nivel , reverse=True))