#funcion
def salario_trabajador (horas_trabajadas:int, salario_hora:int):
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        salario_extra = ((salario_hora * 0.50) + salario_hora) * horas_extras 
        salario_total = salario_hora * horas_trabajadas + salario_extra
    else:
        salario_total = salario_hora * horas_trabajadas
    return salario_total

#prueba
salario_hora = 5000
horas_trabajadas = 40
print(salario_trabajador(horas_trabajadas, salario_hora))