dic = {'A':{'cantidad':2,'valor':1} , 'B':{'cantidad':1,'valor':1}}


lista = []

for letra in dic:
    print(letra)
    for i in range(dic[letra]["cantidad"]):
        #UPDATE
        lista.append(letra)


print(lista)

lista_K = ["__BOTON 1__","__BOTON 2__","__BOTON 3__"]

diccc = {}

for i in range(len(lista_K)):
    diccc[lista_K[i]] = lista[i]

print("-.,-,.-.,"*12)
print(diccc)
print("-.,-,.-.,"*12)