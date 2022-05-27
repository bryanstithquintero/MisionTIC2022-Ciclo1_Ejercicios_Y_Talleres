#funcion
def liquidacion_facturas (estrato:int, cantidad_consumida:int):
    #validacion parametros
    #proceso
    if estrato == 1 :
        valor_factura = 2500 + (cantidad_consumida * 2200) + 5500
    elif estrato ==2 :
        valor_factura = 2800 + (cantidad_consumida * 2350) + 6200
    elif estrato == 3:
        valor_factura = 3000 + (cantidad_consumida * 2600) + 7400
    elif estrato == 4:
        valor_factura = 3300 + (cantidad_consumida * 3400) + 8600
    elif estrato == 5:
        valor_factura = 3700 + (cantidad_consumida * 3900) + 9700
    elif estrato == 6:
        valor_factura = 4400 + (cantidad_consumida * 4800) + 11000
    #salida
    return f"el valor de la factura para el estrato {estrato} es de {valor_factura}"
#prueba
estrato = 4
cantidad_consumida = 11
print(liquidacion_facturas(estrato, cantidad_consumida))