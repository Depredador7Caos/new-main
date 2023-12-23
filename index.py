figura = int(input("¿Que Figura necesita?\n1ºCuadrado \n2ºTriangulo \n3ºRectangulo \n"))

#Operaje de Cuadrado (Area y perimetro)
if figura == 1:
    print("Cuadrado")
    opc = int(input("¿Que calculo necesitas? \n1º Calcular Area \n2º Calcular perimetro \n"))

    print("Ingrese los datos siguientes...")
    lado_1 = int(input("Lado 1 = "))
    lado_2 = int(input("Lado 2 = "))

    if opc == 1:
        def calcular_area(l1, l2):
            resultado = l1 * l2
            print("Area =", resultado)
        calcular_area(lado_1, lado_2)
    elif opc == 2:
        def calcular_perimetro(l1, l2):
            resultado = (l1*2) + (l2*2)
            print("Perimetro =", resultado)
        calcular_perimetro(lado_1, lado_2)

#Operaje de Triangulo (Area y perimetro)
elif figura == 2:
    print("Triangulo")
    opc = int(input("¿Que calculo necesitas? \n1º Calcular Area \n2º Calcular perimetro"))

    print("Ingrese los datos siguientes...")
    lado_1 = int(input("Base = "))
    lado_2 = int(input("Altura = "))

    if opc == 1:
        def calcular_area(a, b):
            resultado = (b * a)/2
            print("Area = ", resultado)
        calcular_area(lado_1, lado_2)
    elif opc == 2:
        def calcular_perimetro(a, b):
            resultado = a + (b*2)
            print("Perimetro =", resultado)
        calcular_perimetro(lado_1, lado_2)

#Operaje de Rectangulo (Area y perimetro)
elif figura == 3:
    print("Rectangulo")
    opc = int(input("¿Que calculo necesitas? \n1º Calcular Area \n2º Calcular perimetro \n"))

    print("Ingrese los datso siguientes...")
    lado_1 = int(input("Lado 1 = "))
    lado_2 = int(input("Lado 2 = "))

    if opc == 1:
        def calcular_area(l1, l2):
            resultado = l1 * l2
            print("Area =", resultado)
        calcular_area(lado_1, lado_2)
    elif opc == 2:
        def calcular_perimetro(l1, l2):
            resultado = (l1*2) + (l2*2)
            print("Perimetro =", resultado)
        calcular_perimetro(lado_1, lado_2)
else:
    print("Option not found")
