from functools import reduce 

def funcion(operador, *numeros, **datosPersonales):
    
    print(operador)
    print(numeros)
    print("-"*20)
    
    if operador == '+':
        resultado = reduce((lambda a,b: a+b), numeros[0])
    elif operador == '*':
        resultado = reduce((lambda a,b: a*b), numeros[0])

    print('resultado', resultado)
    print("-"*20)

    for clave,valor in datosPersonales.items():
        print(clave,valor)


lista = [2,2,2,2,2,2,2]
dic = {'Nombres':'Lack','Apellido':'Molina','Direccion':'calle queti gato'}

funcion('*',lista,dic)