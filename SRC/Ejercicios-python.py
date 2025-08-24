nombre = input("Ingresa tu nombre y apellido")
#Opcion 2
print ("Bienvenido: ", nombre)
#Calcular el IMC de la persona
#Leer peso, altura
peso = input("Ingresa tu peso en kg: ")
peso= float(peso)
altura = input("Ingresa tu talla en metros: ")
altura= float(altura)
#Calculos
imc = peso/altura**2
#Mostrar IMC
print("Tu IMC = ", imc)
if imc < 18.5:
    print("Bajo peso")
if imc >= 18.5 and imc < 25:
    print("Peso normal")
if imc >= 25 and imc < 30:
    print("Sobrepeso")
if imc >= 30:
    print("Obesidad")
if imc >= 40:
    print("Obesidad morbida")
if imc >= 50:
    print("Obesidad extrema")