#Solución de la Tarea Serie de Fibonacci, Santiago Díaz S.

num = int(input("Ingrese la cantidad de números de la serie de Fibonacci que desea imprimir: "))

if num <= 0:
    print("Por favor, ingrese un número entero positivo.")
elif num == 1:
    print("Serie de Fibonacci:")
    print(0)
else:
    a, b = 0, 1
    contador = 2  # Iniciamos en 2 porque ya vamos a imprimir los dos primeros términos
    
    # Imprimir los primeros dos términos
    print("Serie de Fibonacci:")
    print(a)
    print(b)
    
    while contador < num:
        siguiente = a + b
        print(siguiente)
        a, b = b, siguiente
        contador += 1
