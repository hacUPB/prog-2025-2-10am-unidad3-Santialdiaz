#Calculadora
#control = True #la variable de control fue eliminada, en el caso E se elimino

while True: #bucle infinito, siempre sera verdadero
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: ")) 
    print("S, Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion = input("Elija una opcion: ")
    opcion = opcion.upper()  #Para que lo que ingrese el usuario este en mayuscula
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
            break
        case 'P':
            print("Potenciacion")
            Resultado = num1 ** num2 
        case _:
            print("Modo No Valido")
    print(f"Resultado = {Resultado}")

