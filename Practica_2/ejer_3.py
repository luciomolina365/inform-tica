lista = ['Auto', '123', 'Viaje', '50', '120']

lista2=[]

for i in lista:
    if i.isdecimal() == True:
        lista2.append(int (i))


lista2.sort()
print(lista2)