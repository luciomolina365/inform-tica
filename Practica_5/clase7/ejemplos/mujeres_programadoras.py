import csv

archi = open("Todas_las_carreras.csv", "r")

csvreader = csv.reader(archi)

cont = 0
for fila in csvreader:

    if (fila[2]=="Universidad Nacional de La Plata"):
        cont = cont + (0 if fila[19]=='' else int(fila[19]))
        print('Año: {} Facultad: {} -- Egresadas: {}'.format(fila[0], fila[3], fila[19]))

print('\nTotal egresadas de la UNLP: {}'.format(cont))

