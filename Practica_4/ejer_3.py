
import json
import pattern
import pattern.text.es as ptt
from pattern.text.es import conjugate , INFINITIVE


def leerTxt():
    try:
        with open('texto.txt', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('texto.txt', 'w') as archivo:
            datos="Queen es una banda británica de rock formada en 1970 en Londres por el cantante Freddie Mercury, el guitarrista Brian May, el baterista Roger Taylor y el bajista John Deacon. Si bien el grupo ha presentado bajas de dos de sus miembros (Mercury, fallecido en 1991, y Deacon, retirado en 1997), los integrantes restantes, May y Taylor, continúan trabajando bajo el nombre Queen, por lo que la banda aún se considera activa."
            json.dump(datos, archivo)        
        return datos   


def txt_a_lista():
    texto = leerTxt()
    resultado = texto.split()
    return resultado

def esVerbo(palabra):
    palabra = conjugate(palabra, INFINITIVE)
    encuentro = False
    if palabra in ptt.verbs.keys():
        encuentro = True

    if encuentro:
        return palabra
    else:
        return ""

def crearListaDeVerbos(lista):
    listaResultado=[]
    for palabra in lista:        
        palabra = esVerbo(palabra)
        if palabra != "":
            listaResultado.append(palabra)
    
    
    return listaResultado


def txt_a_lista_de_verbos():
    lista = txt_a_lista()
    return crearListaDeVerbos(lista)



def crearJson(lista):
    datos={}

    for verbo in lista:
        
        if verbo not in datos:
            datos[verbo]= lista.count(verbo)

    with open('verbos.json' , 'w') as archivo:
        json.dump(datos,archivo)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



resultado = txt_a_lista_de_verbos()

print(resultado)

crearJson(resultado)