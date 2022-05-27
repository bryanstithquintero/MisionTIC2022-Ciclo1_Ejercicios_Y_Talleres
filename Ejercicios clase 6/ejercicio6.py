#funcion no se porque rango dice con enteros y aqui estan con floats
def validar_numero (numero:float):
    #validar parametros
    if numero < 0:
        return "numero negativo"
    #proceso
    if (numero >= 3.5 and numero <= 7.8) or (numero <= 9.3 and numero >=4.5) or (numero >= 23.4 and numero <= 45.3):
        mensaje = "el numero se encuentra en el rango"
    else:
        mensaje = "el numero no se encuentra en el rango"
    #salida
    return mensaje

numero = 7
print (validar_numero(numero))