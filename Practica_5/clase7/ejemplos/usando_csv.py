import csv

archi = open("datos.csv", "r")
csvreader = csv.reader(archi)
for fila in csvreader:
	if (fila[6]=="reducido"):
		print(fila[0])


