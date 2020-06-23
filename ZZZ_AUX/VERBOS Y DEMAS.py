from pattern.text.es import verbs, parse, split, conjugate, INFINITIVE
import json

def escribir_archivo(datos):
    with open('verbos.json', 'w') as archivo:
        json.dump(datos,archivo)
    archivo.close()

def leer_archivo():
    #try:
    #with open('texto.txt', 'r') as archivo:
        #datos = json.load(archivo)
    datos = open('texto.txt', 'r')
    return datos
    #except FileNotFoundError:
    #    print("El archivo no existe, crealo.")

def muestro_todos_los_verbos():
	for pal in verbs:
		print(pal)

verbos = []

def solo_los_verbos(frase):
    lectura = frase.read()
    s = parse(lectura).split()
    for cada in s:
        for c in cada:
            if c[1] == 'VB':
                verbos.append(c[0])
    return(verbos)

infinitivos = []

def verbos_a_infinitivos(verbos):
    for pal in verbos:
        nueva_pal = conjugate(pal,INFINITIVE)
        infinitivos.append(nueva_pal)
    return(infinitivos)


def main():
    arch = leer_archivo()
    print("-"*20)
    print(solo_los_verbos(arch))
    print("-"*20)
    infinit = solo_los_verbos(arch)
    print(verbos_a_infinitivos(infinit))
    
	
if __name__ == '__main__':
	main()