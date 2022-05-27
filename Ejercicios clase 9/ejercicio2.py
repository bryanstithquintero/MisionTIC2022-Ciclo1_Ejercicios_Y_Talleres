def imprimir_triangulo (altura:int):
    valor_actual = 1
    while valor_actual <= altura:
        print("*" * valor_actual)
        #for x in range(valor_actual):
            #print("*", end="")
        #print()
        valor_actual += 1
altura= int(input("ingrese la altura del triangulo: "))
imprimir_triangulo(altura)