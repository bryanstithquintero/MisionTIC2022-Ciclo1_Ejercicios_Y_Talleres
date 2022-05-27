expresion = 6/2 * (1+2)
print("el resultado correcto es", expresion)
print("la otra calculadora ejecuta las instrucciones de derecha a izquierda")

expresion_2 = (1000*5.95)/100
print("el precio del productor por kilo es", expresion_2)


peso_producto_gramos = 100
precio_producto = 5.95
peso_kilo_gramos = 1000
precio_por_gramo = precio_producto / peso_producto_gramos
precio_por_kilo = precio_por_gramo * peso_kilo_gramos
precio_por_kilo = round(precio_por_kilo, 2)

print(precio_por_kilo)

numero_de_peces_rojos = 284
numero_de_peces_azules = 163
numero_total_de_peces = numero_de_peces_rojos + numero_de_peces_azules
print("el numero total de peces son",numero_total_de_peces)

dinero_al_salir = 23
dinero_al_llegar = 12.75
dinero_gasto = dinero_al_salir - dinero_al_llegar
print("el dinero que carmen gasto en el cine fueron",dinero_gasto, "euros")

precio_pc_con_todos_los_accesorios = 660
descuento_por_pronto_pago = 0.90
precio_final = precio_pc_con_todos_los_accesorios * descuento_por_pronto_pago
print("tienes que pagar en total por el pc con todos los accesorios",precio_final)

descuento = 1.15
pago_por_pantalones = 34
precio_pantalones_sin_descuento = pago_por_pantalones * descuento
precio_pantalones_sin_descuento = round(precio_pantalones_sin_descuento,1)
print("el precio sin descuento es", precio_pantalones_sin_descuento)