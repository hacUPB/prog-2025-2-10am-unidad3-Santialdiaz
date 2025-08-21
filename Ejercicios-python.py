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
