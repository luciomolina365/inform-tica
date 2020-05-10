from pattern.text.es import conjugate,INFINITIVE
import json
from pattern.text.es import verbs
from pattern.text.es import parse, split

def muestro_todos():
    for pal in verbs:
        print(pal)

def leerArchivo():
        with open('texto_ALTERNATIVE.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos
def escribirArchivo(datos):
    with open("texto_ALTERNATIVE.json" , 'w') as archivo:
        json.dump(datos,archivo)


def solo_los_verbos(frase):
    s = parse(frase).split()
    dic={}
    lista=[]
    for cada in s:
        for c in cada:
            if c[1] == 'VB':
                lista.append(c[0])
    for i in lista:
        if i not in dic.keys():
            dic[i]=lista.count(i)
    return dic

def contar(pal,frase):
    s = parse(frase).split()
    cont=0
    for palabra in s:
        if palabra[1] == pal:
            cont=cont+1
    return cont
#muestro_todos()
print("-"*20)
frase = "En muestra muestra muestra una nueva publicacion se muestra como se graban las escenas bajo el agua de la pelicula. Destaca un truco ya conocido por los mas interesados en el cine de Cameron, que es el uso de pelotas flotantes que evitan que la luz interfiera con el ambiente que se quiere conseguir en una determinada escena bajo el agua. Se dejan flotando en la superficie y permiten a los actores salir del agua comodamente."
nuevo=solo_los_verbos(frase)
print(nuevo)
escribirArchivo(nuevo)
