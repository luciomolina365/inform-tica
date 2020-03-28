tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

nuevo = []

for i in tam:
    name, space, tuplaStr = i.partition(" ")

    arreglo=(  int(tuplaStr.split(",")[0])  ,  int(tuplaStr.split(",")[1])  )
    
    print(arreglo)

    nuevo.extend([arreglo])

nuevo.sort()
print(nuevo)