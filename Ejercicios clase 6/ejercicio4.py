#funcion
def validar_numero (numero:int):
    #validar parametros
    #proceso
    if numero % 2 == 0:
        mensaje = "el numero es par"
    else:
        mensaje = "el numero es impar"
    #salida
    return mensaje

numero = int(input("escriba un numero "))
print(validar_numero(numero))


