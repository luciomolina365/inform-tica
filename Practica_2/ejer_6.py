nro1=int(input("Ingrese el primer numero:  "))

nro2=int(input("Ingrese el segundo numero:  "))

opcion=int(input("Ingrese el 1 para sumar"+ "\n" + "Ingrese el 2 para restar" + "\n" +  "Ingrese el 3 para multiplicar" + "\n" +  "Ingrese el 4 para dividir" + "\n")) 

if opcion == 1:
    resultado = nro1 + nro2
elif opcion == 2:
    resultado = nro1 - nro2
elif opcion == 3:
    resultado = nro1 * nro2
elif opcion == 4:
    resultado = nro1 / nro2

print("El resultado es: " + str (resultado))