#funcion no se porque rango dice con enteros y aqui estan con floats
def validar_numero (numero:float):
    #validar parametros
    if numero < 0:
        return "numero negativo"
    #proceso
    if numero >= 3.5 and numero <= 7.8:
        mensaje = "el numero se encuentra en el rango"
    else:
        mensaje = "el numero no se encuentra en el rango"
    #salida
    return mensaje

numero = -4.3
print(validar_numero(numero))