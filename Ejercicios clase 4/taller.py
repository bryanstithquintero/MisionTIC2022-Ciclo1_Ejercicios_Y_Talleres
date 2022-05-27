def ejercicio_1 (nombre:str):
    return f"hola {nombre}"

def ejercicio_2 (numero:int):
    return float(numero)

def ejercicio_3 (precio:int, iva = "0.19"):
    precio_total = precio + (precio * iva)
    return precio_total + iva

import math as m
def ejercicio_4 (r):
    area = m.pi * (r**2)
    return round (area, 2)

def ejercicio_5 (numero_entero:int):
    suma = (numero_entero * (numero_entero + 1))/2
    return int (suma)

def ejercicio_6 (peso:float, estatura:float):
    imc = round (float (peso / (estatura **2)), 2)
    return f"tu indice de masa corporal es {imc}"

def ejercicio_7 (muneca:int, payaso:int):
    peso_payaso = float (payaso * 112)
    peso_muneca = float (muneca * 75)
    peso_total = peso_payaso + peso_muneca
    return int(peso_total)

def ejercicio_8 (barras_vendidas:int):
    precio_barra = 3.49
    descuento = 0.6
    precio_con_descuento = (precio_barra)-(precio_barra * descuento)
    precio_total_barras = round (float(barras_vendidas * precio_con_descuento), 2)
    return f"el precio habitual de una barra de pan es {precio_barra} se hace descuento de {descuento} por ser de ayer por lo que el coste total es {precio_total_barras}"

def ejercicio_9 (ahorros:float):
    intereses = 0.04
    ahorros_primer_ano = round (ahorros + (ahorros * intereses), 2)
    ahorros_segundo_ano = round (ahorros_primer_ano + (ahorros_primer_ano * intereses),2 )
    ahorros_tercer_ano = round (ahorros_segundo_ano + (ahorros_segundo_ano * intereses), 2)
    return f"{ahorros_primer_ano}, {ahorros_segundo_ano}, {ahorros_tercer_ano}"

def ejercicio_10 (tiempo_en_segundos:int):
    tiempo_dias = tiempo_en_segundos // (24 * 60 * 60)
    tiempo_en_segundos = tiempo_en_segundos % (24 * 60 * 60)
    tiempo_horas = tiempo_en_segundos // (60 * 60)
    tiempo_en_segundos = tiempo_en_segundos % (60 * 60)
    tiempo_en_minutos = tiempo_en_segundos // 60
    tiempo_en_segundos= tiempo_en_segundos % 60
    return f"dias {tiempo_dias} horas {tiempo_horas} minutos {tiempo_en_minutos} segundos {tiempo_en_segundos}"

