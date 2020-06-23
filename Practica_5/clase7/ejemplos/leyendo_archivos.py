def leo_caracteres():
    f = open("imagine.txt","r")
    for x in f.read():
        print(x)
        f.close()

def leo_lineas():
    f = open("imagine.txt","r")
    print(f.readlines())
    f.close()

def otra_forma():
    f = open("imagine.txt","r")
    for linea in f:
        print(linea)
    f.close()

def main():
    print('Leo caracteres')
    leo_caracteres()
    print('-' * 20)
    print('Leo lineas')
    leo_lineas()
    print('-' * 20)
    print('Otra forma')
    otra_forma()


if __name__ == "__main__":
    main()
