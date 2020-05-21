#!/usr/bin/python3

texto = '''colores:rojo naranja amarillo verde azul indigo violeta blanco negro marron, 
figuras: cuadrado triangulo rectangulo circulo elipse rombo trapezoide,
frutas: manzana naranja limon lima pera uva melon banana mango frutilla,
animales: murcielago oso gato perro mono pato aguila pez leon rata panda'''


texto = texto.strip().replace("\n", "").split(',')
palabras = {}
for palabra in texto:
    valor=palabra.split(":")
    palabras[valor[0]]=(valor[1]).split()

print(palabras)

def convertir(lista):
    return len(lista)


