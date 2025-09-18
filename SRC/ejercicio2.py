
#Determinar si un numero es par o impar
numero = int(input("Ingrese un numero entero: "))
residuo = numero % 2
#Si el residuo es 0, el numero es par
if residuo == 0:
    print(numero, "es par")
# Si el residuo no es 0, el numero es impar
else:
    print(numero, "es impar")