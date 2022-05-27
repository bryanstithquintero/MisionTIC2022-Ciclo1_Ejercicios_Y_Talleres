#funcion
def validacion_numeros (numero_1:int, numero_2:int, numero_3:int, numero_4:int):
    #validar parametros
    if numero_1 and numero_2 and numero_3 and numero_4 == str:
        return "ingrese un numero"
    #proceso
    resultado = max(numero_1, numero_2, numero_3, numero_4)
    #salida
    return resultado
#prueba
numero_1, numero_2, numero_3, numero_4 = int(input("ingrese numero1 ")), int(input("ingrese numero2 ")), int(input("ingrese numero3 ")), int(input("ingrese numero4 "))
print(validacion_numeros(numero_1, numero_2, numero_3, numero_4))