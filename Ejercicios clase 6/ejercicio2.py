#funcion
def validacion_nota (nota:float):
    #validar parametros
    if nota < 0.0 or nota > 5.0:
        return "ingrese un numero entre 0.0 y 5.0"
    #proceso
    if nota >= 3.0:
        mensaje = "gano el curso"
    if nota < 3.0:
        mensaje = "perdio el curso"
    #salida
    return f"{nota} el estudiante {mensaje}"

#prueba
nota = float(input("ingrese su nota "))
print(validacion_nota(nota))