#reto 1
def CDT (usuario:str, capital:int, tiempo:int):
    """CDT
    :parametros: usuario (str): alfanumerico que identifica el usuario
    capital (int): monto a ingresar
    tiempo (int): tiempo del CDT
    """
    if tiempo > 2:
        valor_intereses = (capital * 0.03 * tiempo) / 12
        valor_total = int (valor_intereses + capital)
    else:
        valor_perdida = capital * 0.02
        valor_total = int (capital - valor_perdida)
    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial es {capital} para un tiempo de {tiempo} meses es: {valor_total}"

usuario = str(input("ingrese su usario"))
capital = int(input("ingrese el monto"))
tiempo = int(input("ingrese el tiempo"))
print(CDT(usuario, capital, tiempo))

