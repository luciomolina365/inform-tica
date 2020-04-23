import random

#Defino conjunto de palabras a trabajar por temas
palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}

#Defino estructura del ahorcado
ahorcado = ["O","/|\\" , "/ \\"] 

#Comienza el proceso del juego 

#Pido que el jugador elija un tema
tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))

#Selecciono la palabra a trabajar
pal = palabras[tema][random.randrange(len(palabras[tema]))]

print(pal)





