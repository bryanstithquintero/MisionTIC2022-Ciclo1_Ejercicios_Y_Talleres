#no funcion
mayor = -1
numero = int(input("ingrese un numero positivo: "))
if numero < 0:
    print("ingrese un numero valido ")
while numero > 0:
    if numero > mayor:
        mayor = numero
    numero = int(input("ingrese un numero positivo: "))
print("mayor numero ingresado", mayor)

#funcion
def mayor (numero:int):
    if numero < 0:
        return "ingrese un numero valido"
    mayor = -1
    while numero > 0:
        if numero > mayor:
            mayor = numero
        numero = int(input("ingrese un numero positivo: "))
    return f"mayor numero ingresado {mayor} "

numero = int(input("ingrese un numero positivo: "))
print(mayor(numero))
