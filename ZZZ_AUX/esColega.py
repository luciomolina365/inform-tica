def esColega(n):
    n = str(n)
    for digito in n:
        aux = n.count(digito)
        if(aux>=2):
            return True
        else:
            return False