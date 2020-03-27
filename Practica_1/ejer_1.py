frase = """"Si trabajas mucho con computadoras, 
eventualmente encontraras que te gustaria automatizar alguna tarea. Por ejemplo, 
podrias desear realizar una busqueda y reemplazo en un gran numero de archivo de texto, 
o renombrar y reorganizar un monton de archivos con fotos de una manera compleja. 
Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicacion especializada 
con interfaz grafica, o un juego simple."""

lista= frase.upper().replace("\n","").replace(",","").split(" ")

print(lista)


