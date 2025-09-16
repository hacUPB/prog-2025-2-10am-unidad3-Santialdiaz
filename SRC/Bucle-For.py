'''
numero = int(input('Ingrese el numero entero: '))
while numero < 0:
    numero = int(input('Ingrese el numero entero positivo: '))
acum = 0
for cont in range(1,numero+1):
    if cont % 2 == 0:
        acum += cont
print(f"La suma de los pares es {acum}")
'''
'''
mensaje = "Universidad Pontifica Bolivariana"
numero = int(input('Ingrese el numero entero positivo: '))
for i in range (numero):
    print(mensaje)

#EN ESTE CASO LA i SE USA SOLO POR LA SINTAXIS
'''
# Conversor de Temperatura
'''
opcion = 'L'                     #Valor temporal
while opcion != 'Q':
    opcion = input("F, Fahrenheit a Celsius\nC. Celsius a Fahrenheit\nQ. Salir\n")
    opcion = opcion.upper()
    if opcion != 'Q':
        temperatura = float(input("Ingrese la temperatura a convertir: "))
        match opcion:
            case 'f':
                conversion = (temperatura - 32)*(5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case 'C':
                conversion = (temperatura * 9 / 5) + 32
                print (f"{temperatura}°C = {conversion}°F")
            case 'Q':
                print("Saliendo del programa . . .")
            case _:
                print("Opcion no valida")
    else:
        print("Saliendo del programa... ")
 '''     

#VERIFICADOR DE NUMEROS PRIMOS 

'''
Variable de entrada
numero    int

Variable de salida
divisores
'''
'''
numero = int(input("Ingrese un numero entero mayor que 1: "))
cont = 0
for i in range(1, numero + 1 ):
    if numero % i == 0:
        cont += 1

if cont == 2:
    print(f"{numero} es primo")
else:
    for i in range(1, numero + 1 ):
        if numero % i == 0:
            print(i)
'''

 
 