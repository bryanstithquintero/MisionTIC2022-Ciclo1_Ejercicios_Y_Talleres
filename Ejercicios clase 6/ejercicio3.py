#funcion
def validar_edad(edad:int):
    #validar parametros
    if edad == str or edad == float:
        return "escriba un numero entero"
    #proceso
    if edad >= 18:
        mensaje = "es mayor de edad"
    if edad < 18:
        mensaje = "es menor de edad"
    #salida
    return mensaje

#prueba
edad = int(input("ingrese su edad "))
print(validar_edad(edad))


