#txt = "h3110 23 cat 444.4 rabbit 11 2 dog"
#l = []
#l = [int(s) for s in txt.split() if s.isdigit()]
#print(l)


def esColega(n):
    n = str(n)
    for digito in n:
        aux = n.count(digito)
        if(aux>=2):
            return True
        else:
            return False

print(esColega(3378))

def esCapicua(n):
    n = str(n)
    n1 = n[::-1]
    if(n==n1):
        return True
    else:
        return False

esCapicua(45654)

def esPrimo(n):
    n = int(n)
    if n < 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

print(esPrimo(17))

def suma_es_primo(n):
    n = int(n)
    suma=0
    while n != 0:
        dig = n % 10
        n = n//10
        suma = suma + dig
    return suma

print(suma_es_primo(17))

def gen_informacion(info):
    dic={}
    lis=info.split(" ")
    for i in lis:
       if(esColega(i)==True):
            dic[i]={}
            dic[i]["esCapicua"]=esCapicua(i)
            suma = suma_es_primo(i)
            dic[i]["suma_es_primo"]=esPrimo(suma)
    return dic

info ="222 13 33 111 7 9659"
print(gen_informacion(info))