#   Ejercicio de tabla de multiplicar
numero = int(input("Ingrese un numero entero"))
print(f"Tabla de multiplicar del {numero}: ") 
i = 1
while i <= 15:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
    