from pattern.text.es import verbs, parse, split, conjugate, INFINITIVE
import json

def lista_de_verbos_en_texto(texto):

    listaDePalabras=[]
    conjunto = parse(texto).split()
    for palabra in conjunto:
        for pal in palabra:
            if pal[1]=="VB":
                listaDePalabras.append(pal[0])

    return listaDePalabras


def lista_de_verbos_en_infinitivo(lista):
    resultado = []
    for elemento in lista:
        resultado.append(conjugate(elemento,INFINITIVE))

    return resultado

def procesar (listaEnInfinitivo):
    
    diccionario = {}

    for palabra in listaEnInfinitivo:
        if palabra not in diccionario.keys():
            diccionario[palabra] = listaEnInfinitivo.count(palabra)
    
    return diccionario

def crearArchivo(datos):

    with open('verbos.json', 'w') as archivo:
        json.dump(datos, archivo)        


def hacer(archivo):
    lista = lista_de_verbos_en_texto(archivo)
    listaEnInfinitivo = lista_de_verbos_en_infinitivo(lista)
    datos = procesar(listaEnInfinitivo)
    return datos


#===========================================================================================================


archivo = open("texto.txt", "r")
archivo = archivo.read()
print(archivo)

datos = hacer(archivo)

crearArchivo(datos)



