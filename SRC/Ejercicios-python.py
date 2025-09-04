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
    mensaje = "Bajo peso"
elif imc >= 18.5 and imc < 25:
    mensaje = "Peso normal"
elif imc >= 25 and imc < 30:
    mensaje ="Sobrepeso"
elif imc >= 30:
     mensaje ="Obesidad"
elif imc >= 40:
    mensaje = "Obesidad morbida"
elif imc >= 50:
    mensaje = "Obesidad extrema"

print(f"Paciente: {nombre}, tiene un IMC de: {imc:0.2f} y su estado es: {mensaje}")

  


