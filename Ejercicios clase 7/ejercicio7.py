#forma 1
def validacion_nota (nota1:float, nota2:float, nota3:float ):
    if nota1 < 0.0 or nota1 > 5.0 or nota2 < 0.0 or nota2 > 5.0 or nota3 < 0.0 or nota3 > 5.0:
        return "ingrese un numero valido"
    promedio = (nota1 + nota2 + nota3)/ 3
    if promedio < 3.0:
        return "no aprobo el curso"
    else:
        return "su nota es {} aprobo el curso".format(promedio)
nota1 = 5.0
nota2 = 2.2
nota3 = 4.5
print(validacion_nota(nota1, nota2, nota3))

#forma 2
def validacion_nota2 (nota:dict):
    if nota["nota1"] < 0.0 or nota["nota1"] > 5.0 or nota["nota2"] < 0.0 or nota["nota2"] > 5.0 or nota["nota3"] < 0.0 or nota["nota3"] > 5.0:
        return "ingrese un numero valido"
    promedio = (nota["nota1"] + nota["nota2"] + nota["nota3"])/ 3
    if promedio < 3.0:
        return "no aprobo el curso"
    else:
        return "su nota es {} aprobo el curso".format(promedio)
nota ={"nota1" : 5.0, "nota2" : 2.2, "nota3" : 1.5}
print(validacion_nota2(nota))