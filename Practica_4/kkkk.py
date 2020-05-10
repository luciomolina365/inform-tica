import json
import time
archivo = open("superHeroesEnJSON.txt", "w")
datos = [{'nombre': 'Tony Stark', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())} ,
 {'nombre': 'Bruce Wayne', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())}]
json.dump(datos, archivo)
archivo.close()





lista = ["hola", "hola"]

cant = lista.count("hola")

print(cant)