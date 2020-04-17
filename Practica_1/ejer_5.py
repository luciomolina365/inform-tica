#ejercicio 1
#frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple."

#lista =frase.split(" ")

#print(lista)

#ejercicio2
"""
texto = input()
busqueda = input()

if texto.islower():
    busqueda=busqueda.lower()
else:
    busqueda=busqueda.upper()

palabras_texto = texto.split(' ')


print(palabras_texto)
palabras_busqueda = [s for s in palabras_texto  if busqueda in s]  # recorre mi frase y pregunta si busqueda pertenece a s

print(len(palabras_busqueda))
print(palabras_busqueda)
"""
#ejercicio 3
"""
frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple."
lista1 = frase.split(" ")
frase2= " ".join(e for e in lista1)
lista2 =frase2.upper().split(" ")

print(frase2)
"""

#ejercicio 4
"""
texto = input()
busqueda = input()

if texto.islower():
    busqueda=busqueda.lower()
else:
    busqueda=busqueda.upper()

palabras_texto = texto.split(' ')


#print(palabras_texto)
palabras_busqueda = [s for s in palabras_texto  if busqueda in s]  # recorre mi frase y pregunta si busqueda pertenece a s

string=" ".join(palabras_busqueda)
print(string)
"""
#ejercicio 5


frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple."

lista= frase.split(" ")
lista2= [ ]
for i in lista:
    if lista.count(i) == 1:
        lista2.append(i)

    if lista2.count(i) == 0:
        lista2.append(i)

        

# sin_repetidos_string=" ".join(lista2)
# act= sin_repetidos_string.lower()

print(lista2)