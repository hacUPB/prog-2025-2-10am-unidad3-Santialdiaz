def menu():
    print("1.Entradas\n2. Platos Fuertes\n3.Bebidas\n4.Postres\n5.Salir")
    opcion = int(input("Elija una opcion "))
    return opcion 
def entradas():
    print('1. Pan de bono\t\t$3000')
    print('2. Empanada\t\t$3500')
    print('3. Patacones\t\t$7500')
    print('4. Nuggets de Pollo\t\t$10000')
def fuertes():
    print('1. Churrasco\t\t$30000')
    print('2. Salmon\t\t$35000')
    print('3. Hamburguesa\t\t$45000')
    print('4. Ensalada Cesar\t\t$38000')
    print('5. Pasta de Vegetales\t\t$35000')
    print('6. Pasta de Carnes\t\t$45000')
    print('7. Pechuga\t\t$38000')
def bebidas():
    print('1. Limonada Natura\t\t$10000')
    print('2. Limonada Hierbabuena\t\t$10000')
    print('3. Naranjada\t\t$10000')
    print('4. Cerezada\t\t$8000')
    print('5. Cerveza\t\t$5000')
    print('6. Gaseosa\t\t$5000')
    print('7. Agua\t\t$3000')
def postres():
    print('1. Torta Red Velvet\t\t$10000')
    print('2. Torta de Chocolate\t\t$10000')
    print('3. Postre de Limon\t\t$9000')
    print('4. Postre de Maracuya\t\t$9000')
    print('5. Postre Napolitano\t\t$9000')
    print('6. Copa de Helado\t\t$15000')
    print('7. Waffles\t\t$30000')
# Funcion Principal
eleccion = menu()
print(eleccion)

match(eleccion):
    case 1:
        entradas()
    case 2:
        fuertes()
    case 3:
        bebidas()
    case 4:
        postres()
    case _:
        print("Opcion no valida")

#Metodos son funciones asociadas a un objeto, para poder usarlo debo usarlo sobre el objeto.


# Aqui se llama la funcion principal
if __name__ == "__main__":
    main()

