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

mensaje = "Universidad Pontifica Bolivariana"
numero = int(input('Ingrese el numero entero positivo: '))
for i in range (numero):
    print(mensaje)

#EN ESTE CASO LA i SE USA SOLO POR LA SINTAXIS
