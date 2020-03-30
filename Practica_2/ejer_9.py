#Utilizo una función que genera números aleatorios en un cierto rango
import random
numero_compu= random.randrange(0,51)
print(numero_compu)
#Inicializo la variable que cuenta la cantidad de oportunidades y comienzo
#con el juego
cont=0
while cont != 13 :
 if cont == 3 :
    if numero_compu % 2 == 0:
        print("__PISTA: Es par")
    else:
        print("__PISTA: Es impar")
 
 
 #Pido ingresar el número al usuario
 ingresa_numero= int(input('Ingresa el número que pensó la compu en un rango de 1 a 50. '))
 #Evalúo si es le número generado por la computadora
 if ingresa_numero == numero_compu:
    print ('Ganaste! y lo hiciste en', cont, 'intentos!')
    cont= 13
 else:
    print ('No.. ese número no es... Sigue pensando..')
    cont= cont + 1
#Consulto si uso todos los intentos..
if cont == 11:
 print ('\n Perdiste :(\n La compu pensó en el número:', numero_compu)