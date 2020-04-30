def funcionA(*args):
    print("-"*20)
    resultado = list(enumerate(args))
    for i,nombre in resultado:
        print(f"{i}. {nombre}")
    print("-"*20)

funcionA("Lack","Blackmight","Zeekx", "RusitoLp")

