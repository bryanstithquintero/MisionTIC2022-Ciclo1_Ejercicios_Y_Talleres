saldo = 0
print("escriba la bitacora de operaciones: ")
while True:
    s = input()
    if not s:
        break
    datos = s.split(" ")
    operacion = datos [0]
    monto = int(datos[1])
    if operacion == "D":
        saldo += monto
    elif operacion == "R":
        saldo -= monto
    else:
        pass
print(saldo)