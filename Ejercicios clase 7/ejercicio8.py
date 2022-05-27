valor=int(input("ingrese su valor "))
if valor >= 0 and valor <= 100000:
    print("descuento del 0%")
elif valor > 100000 and valor <= 225000:
    print("descuento del 1.5%")
elif valor > 225000 and valor <= 375000:
    print("descuento del 3.8%")
elif valor > 375000:
    print("descuento del 1.5%")

