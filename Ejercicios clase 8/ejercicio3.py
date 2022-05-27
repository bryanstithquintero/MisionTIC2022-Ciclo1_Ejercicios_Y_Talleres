mensaje = "ingrese un numero entero (0 para salir): "
numero = int(input(mensaje))
sumatoria = 0
while numero != 0:
    sumatoria += numero
    numero = int(input(mensaje))
print(f"la sumatoria de los numeros ingresados es {sumatoria}")