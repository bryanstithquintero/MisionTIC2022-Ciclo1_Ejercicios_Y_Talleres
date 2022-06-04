def ordenes (rutinaContable):
    #importar reduce
    from functools import reduce
    #orden minima de 600000 si es menor sumar un incremento de 25000
    ordenMinima = 600000
    incremento = 25000
    #sumar el total de cada tupla de cada lista
    ordenTotal = list(map(lambda x: [x[0]] + list(map (lambda y: y[1]*y[2], x[1:])), rutinaContable))
    #sumar los totales de todas las tuplas de toda la lista
    ordenTotal = list(map(lambda x: [x[0]] + [reduce(lambda a, b: round(a + b, 2), x[1:])], ordenTotal))
    #sumar el incremento si no se llega a 600000
    ordenTotal = list(map(lambda x: x if x[1]>= ordenMinima else (x[0], x[1] + incremento), ordenTotal))
    #print
    print('------------------------ Inicio Registro diario ---------------------------------')
    for x in range(len(ordenTotal)):
        print(f'La factura {ordenTotal [x][0]} tiene un total en pesos de {ordenTotal [x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')
rutinaContable = [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] ]
ordenes(rutinaContable)