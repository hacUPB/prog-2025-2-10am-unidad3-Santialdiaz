
#Ejercicio Condicional Simple
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.
numero = int(input("Ingrese un numero entero: "))
print(numero % 3)   
if numero % 3 == 0:
    print(f"El numero {numero} es divisible por 3")

#EJERCICIO CON MENU
print("=== MENÚ PRINCIPAL ===")
print("'A'. Ver datos de sensores")
print("'B'. Configurar parámetros")
print("'C'. Salir")

opcion = (input("Selecciona una opción: "))

match opcion:
    case 'A':
        print("Mostrando datos de sensores...")
    case 'B':
        print("Entrando a configuración...")
    case 'c':
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")
