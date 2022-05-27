#funcion
def validacion_nota (nota:float):
    #validacion de parametros
    if nota < 0.0 or nota > 5.0:
        return "ingrese un numero valido entre 0.0 y 5.0"
    #proceso
    if nota < 3.0:
        mensaje = "insuficiente"
    elif nota <= 3.5:
        mensaje = "aceptable"
    elif nota <= 4.0:
        mensaje = "sobresaliente"
    elif nota <= 5.0:
        mensaje = "excelente"
    #salida
    return mensaje

#prueba
nota = float(input("ingrese su nota "))
print(validacion_nota(nota))
