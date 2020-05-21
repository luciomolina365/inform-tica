def esCapicua(n):
    n = str(n)
    n1 = n[::-1]
    if(n==n1):
        print("ES CAPICUA")
    else:
        print("NO ES CAPICUA")

num = 6996

esCapicua(num)