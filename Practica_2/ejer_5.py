lista=[]

opcion=int(input("Ingrese una opcion del 1 al 6:  "))
while opcion != 0:
    
    if opcion==1:
        nro=input("Ingrese un nro:  ")
        lista.append(int(nro))
        print("NUMERO AGREGADO")
    elif opcion == 2:

        if len(lista) != 0:
            lista.sort()
            print("LISTA ORDENADA")
        else:
            print("__LISTA VACIA__")

    elif opcion == 3:
        
        if len(lista) != 0:
            print("MAXIMO: "+ str(max(lista)))
        else:
            print("__LISTA VACIA__")

    elif opcion == 4:
        
        if len(lista) != 0:
            print("MINIMO: "+ str(min(lista)))
        else:
            print("__LISTA VACIA__")  

    elif opcion == 5:

        if len(lista) != 0:
            print("PROMEDIO: "+ str(sum(lista)/len(lista)))
        else:
            print("__LISTA VACIA__")

    elif opcion == 6:
        
        if len(lista) != 0:
            print("----------------------------------------------------------------------------------------------------------------------------")
            print(lista)
            print("----------------------------------------------------------------------------------------------------------------------------")
        else:
            print("__LISTA VACIA__")
    
    opcion=int(input("Ingrese una opcion del 1 al 5:  "))
    

print("LISTA RESULTADO============================================================================================================")
print(lista)