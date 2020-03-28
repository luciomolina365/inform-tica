from random import choice

preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]

puntaje=0

while len(preguntas) != 0:
    
    pregunta_aleatoria= choice(preguntas)
    print(pregunta_aleatoria[0])
    
    respuesta= input("Ingrese SI o NO:  ")
    respuesta.lower
    
    if respuesta == pregunta_aleatoria[1]:
        puntaje+=1
        print("Correcto")
    else:
        print("Incorrecto")
    
    preguntas.remove(pregunta_aleatoria)

print("Tu puntaje es : "+ str(puntaje))