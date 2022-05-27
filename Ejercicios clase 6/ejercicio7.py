#funcion
def validar_mensaje (mensaje:str):
    #validar parametros
    #proceso
    if mensaje == "a" or mensaje == "A":
        impresion = "android"
    elif mensaje == "i" or mensaje == "I":
        impresion = "ios"
    else:
        impresion = "opcion invalida"
    #salida
    return impresion

#prueba
mensaje = str(input("escriba la letra "))
print(validar_mensaje(mensaje))
