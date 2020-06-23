import csv

archivo = open("mujeresEnCarrera.csv", "r")

csvreader = csv.reader(archivo)


try:
    lista = []
    for linea in csvreader:
        print("---" *50)
        print(linea[0])   
        print(linea[2]) 
        print(linea[4])   
        print(linea[10])

        if linea[2] == "Universidad Nacional de La Plata":
            elemento =[ linea[0] , linea[2] , linea[4] , linea[10] ]
            lista.append(elemento)

except UnicodeDecodeError:
    print("SALTO EL ERROR PERRO" + "//////" * 20)

finally:

    for persona in lista:
        print(persona)
        print("-.,-.,"* 20)
    



    
# Año, 0
# Tipo de Institución, 1
# Institución, 2 
# Unidad Académica, 3 
# Carrera, 4 
# Título, 5 
# Gestión, 6
# Nivel de la Oferta, 7 
# Total de Estudiantes, 8
# Estudiantes Varones, 9 
# Estudiantes Mujeres, 10
# Total de Nuevos Inscriptos, 11
# Nuevos Inscriptos Varones, 12
# Nuevas Inscriptas Mujeres, 13
# Total de Reinscriptos, 14
# Reinscriptos Varones, 15
# Reinscriptos Mujeres, 16
# Total de Egresados, 17
# Egresados Varones, 18
# Egresados Mujeres, 19