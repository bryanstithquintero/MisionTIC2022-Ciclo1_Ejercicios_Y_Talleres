numero = int(input("Digite un numero entero "))
if numero >0:
    if numero >=10 and numero <= 99:
        print("el numero es positivo y tiene dos digitos")
    else:
        print("el numero es positivo y no tiene dos digitos")
else:
    if numero >= -999 and numero <= -100:
        print("el numero es negativo y tiene tres digitos")
    else:
        print("el numero es negativo y no tiene tres digitos")