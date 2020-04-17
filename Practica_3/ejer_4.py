
anim={'Gato Montes':2,'Yacare overo':4,'Boa acuática':5} 

pal_separada=[]

codigo=list(anim.values())[0]
for j in range(len(anim)):
    pal=list(anim.keys())[j]
    codigo=list(anim.values())[j]
    cont=0
    for i in pal:
        if(cont==codigo):
            pal_separada.append(i)
        else:
            pal_separada.append("_")
        cont=cont+1
    
    print(" ".join(pal_separada))
    pal_separada.clear()




