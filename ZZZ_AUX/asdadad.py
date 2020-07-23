cadena= "RR6"

def formatear(cadena):

    aux = []
    for LETRA in cadena:
        if not LETRA.isdecimal():
            aux.append(LETRA)

    nueva_cadena = ""
    for letra in aux: 
        nueva_cadena = nueva_cadena + letra

    return nueva_cadena




texto = "(11, 356)"
print (type(eval(texto)))

