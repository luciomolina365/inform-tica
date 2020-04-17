import random

colores=['azul','amarillo','rojo','verde']
coordenadas=[(1,2),(3,4),(5,6),(7,8)]

dic_sin_repeticiones = {}

tam_colores= len(colores)
for coor in coordenadas:
    # seleccionar un numero aleatorio de color
    numCol = random.randrange(0, tam_colores)

    # asignar al diccionario
    dic_sin_repeticiones[coor] = colores[numCol]

    # elmimino los elementos seleccionados para evitar repeticiones
    colores.remove(colores[numCol])

    # reduzco la longitud de la lista
    tam_colores= tam_colores- 1

print(dic_sin_repeticiones)



def imprimirA():
    N1 = random.randrange(50)
    N2 = random.randrange(50)
    resultado = N1 + N2
    teclado=int(input(f"Cuanto es: {N1} + {N2} = "))

    if teclado == resultado:
        print("Correcto")
    else:
        print(f"Incorrecto el resultado es: {resultado} ")



palabras = [('grave',['molesto']) , ('aguda',['ratón']) , ('esdrujula',['murciélago'])]
    
def imprimirB():
    pos = random.randrange(0, len(palabras))
    cadena = palabras[pos][1]
    tipo = palabras[pos][0]
    
    respuesta_teclado = input(f"La palabra {cadena} es: ") 

    if respuesta_teclado == tipo :
        print("Correcto, fuiste al colegio!")
    else:
        print(f"Incorrecto, la palabra es: {tipo}")


funciones = {'azul': imprimirA, 'amarillo': imprimirB, 'rojo': imprimirA, 'verde': imprimirB}

while True:
    # col = input('decime un color: ')
    coor = input('decime una coordenada separada por comas (por ej 5,6): ')
    x, y = coor.split(',')
    funciones[dic_sin_repeticiones[(int(x),int(y))]]()
