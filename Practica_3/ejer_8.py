def funcionA(*args):
    print("-"*10)
    resultado = sum(args[:10])
    return resultado

print(funcionA(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37))


def funcionB(**kwargs):
    for clave, valor in kwargs.items():
        print("El valor de {} es {}".format(clave, valor))


funcionB(Emilio = 34, Carlos = 56 , Dario = "GATITO33" , LUCIO = "KPO") 