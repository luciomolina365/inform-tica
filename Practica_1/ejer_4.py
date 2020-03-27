frase ="""Solo por las calles del olvido debo andar medio perdido 
pero no me sé buscar desearía tanto que me encuentres Caminabas sola por la vida 
vos llegabas, yo me iba no te dejo de mirar desearía tanto que me mires 
Quiero escapar, quiero dejarte mi pasado la ciudad no me permite ver el sol"""

# palabra a buscar
busqueda = input("Ingrese una palabra: ")

# pasamos el string a minusculas
busqueda = busqueda.lower()

# dividimos la frase en minuscilas
palabras_frase = frase.replace("\n", "").lower().split(" ")

# buscamos la palabra
palabras_busqueda = [s for s in palabras_frase if busqueda in s]

# imprimimos en pantalla, la palabra ingresada y la cantidad de veces que aparece
print(palabras_busqueda, len(palabras_busqueda))

print(" ".join(palabras_frase))