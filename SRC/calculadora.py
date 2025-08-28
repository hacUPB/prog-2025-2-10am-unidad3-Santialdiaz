#Calculadora



control = True

while control == True:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: ")) 
    print("S, Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion = input("Elija una opcion: ")
    match opcion:
        case 'S':
            print("Suma")
            Resultado = num1 + num2
        case 'R':
            print ("Resta")
            Resultado = num1 - num2 
        case 'M':
            print("Multiplicacion")
            Resultado = num1 * num2
        case 'D':
            print("Division")
            Resultado = num1 / num2
        case 'E': 
            control = False
        case _:
            print("Modo No Valido")
    print(f"Resultado = {Resultado}")

