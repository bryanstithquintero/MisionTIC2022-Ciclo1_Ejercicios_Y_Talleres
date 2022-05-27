#funcion
def validar_precio (camisas:int, precio_camisas:dict):
    if camisas >= 3:
        descuento = (precio_camisas["camisa1"]+precio_camisas["camisa2"]+precio_camisas["camisa3"])*0.20
        precio_total = (precio_camisas["camisa1"]+precio_camisas["camisa2"]+precio_camisas["camisa3"])-descuento 
    else:
        descuento = (precio_camisas["camisa1"]+precio_camisas["camisa2"])*0.10
        precio_total = (precio_camisas["camisa1"]+precio_camisas["camisa2"])-descuento 
    return int(precio_total)
#prueba
camisas= 2
precio_camisas={"camisa1":20000,"camisa2":13000}
print(validar_precio(camisas, precio_camisas))