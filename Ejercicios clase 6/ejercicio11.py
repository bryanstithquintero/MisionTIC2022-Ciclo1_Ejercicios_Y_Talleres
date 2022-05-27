#funcion
def validacion (genero:str, estado_civil:str, estatura:float, edad:int):
    if estado_civil == "soltero":
        if genero == "mujer":
            if estatura > 1.60:
                if edad >= 20 and edad <= 25:
                    return "es apta"
                else:
                    return "no es apta por la edad"
            else:
                    return "no es apta por estatura"
        if genero == "hombre":
            if estatura > 1.65:
                if edad >= 18 and edad <= 24:
                    return "es apto"
                else:
                    return "no es apto por edad"
            else:
                return "no es apto por estatura"
    else:
        return "no es apto"
#prueba

genero = input("ingrese su genero ")
estado_civil = input("ingrese su estado civil ")
estatura = float(input("ingrese su estatura "))
edad = int(input("ingrese su edad "))
print(validacion(genero, estado_civil, estatura, edad))
