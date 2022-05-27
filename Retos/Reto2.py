#funcion
def cliente (informacion:dict):
    if informacion ["edad"]>18:
        atraccion = "X-Treme"
        apto = True
        if informacion ["primer_ingreso"] == True:
            total_boleta = (20000-(20000*0.05))
        else:
            total_boleta = (20000)
    if informacion ["edad"] >= 15 and informacion ["edad"] <= 18:
        atraccion = "Carros chocones"
        apto = True
        if informacion ["primer_ingreso"] == True:
            total_boleta = (5000-(5000*0.07))
        else:
            total_boleta = 5000
    if informacion ["edad"] >= 7 and informacion["edad"] <15:
        atraccion = "Sillas voladoras"
        apto = True
        if informacion ["primer_ingreso"] == True:
            total_boleta =(10000-(10000*0.05))
        else:
            total_boleta = 10000
    if informacion ["edad"] < 7:
        apto = False
        atraccion = "N/A"
        total_boleta = "N/A"
    resultado = {"nombre": informacion["nombre"], "edad": informacion["edad"], "atraccion":atraccion, "apto":apto, "primer_ingreso": informacion["primer_ingreso"], "total_boleta": total_boleta}
    return resultado
#prueba
informacion = {"id_cliente": 1,"nombre": "Johana Fernandez","edad": 20,"primer_ingreso": True}
informacion2 = {'id_cliente' : 1, 'nombre' : "Johana Fernandez", 'edad': 20, 'primer_ingreso': False }
informacion3 = {'id_cliente' : 1, 'nombre' : "Gloria Suarez", 'edad': 3, 'primer_ingreso': True }
informacion4 = {'id_cliente' : 1, 'nombre' : "Tatiana Suarez", 'edad': 17, 'primer_ingreso': True }
informacion5 = {'id_cliente' : 1, 'nombre' : "Tatiana Suarez", 'edad': 17, 'primer_ingreso': False }
informacion6 = {'id_cliente' : 1, 'nombre' : "Tatiana Ruiz", 'edad': 8, 'primer_ingreso': True }
informacion7 = {'id_cliente' : 1, 'nombre' : "Tatiana Ruiz", 'edad': 8, 'primer_ingreso': False }
print(cliente(informacion7))