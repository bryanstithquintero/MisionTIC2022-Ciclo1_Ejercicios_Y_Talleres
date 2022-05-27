def validacion_nota(nota:float):
    # validar parametros
    if nota < 0.0 or nota > 5.0:
        return "ingrese un valor entre 0.0 y 5.0"
    # proceso
    mensaje = ""
    if nota >= 4.0:
            mensaje = "felicitaciones!"
    #salida    
    return f"su notas es {nota} {mensaje}"

nota = float(input("ingrese su nota "))
print(validacion_nota(nota))