imagenes=['im1','im2','im3']

copy = imagenes[:]


for i in  range(0,len(imagenes)):
    nro1 = int(input("Ingrese coor X:  "))
    nro2 = int(input("Ingrese coor Y:  "))
    while nro2 == nro1:
        nro2 = int(input("Ingrese coor Y:  "))

    copy[i]=copy[i] + " " + str(nro1) + " " + str(nro2)

    copy[i]= copy[i].split(" ")

print(copy)




