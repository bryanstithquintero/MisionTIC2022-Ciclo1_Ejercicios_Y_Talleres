# Valores dados 
x = 3
y = 9
#el contrario de un exponenete es el logaritmo natural por lo que ese inmporta biblioteca
import math as m
exponente = m.log(y, x)
print(round (exponente, 2))

#solucion normal ahora hacer funcion
def potencia (x:int, y:int):
    try:
        import math
        exponente = int (math.log(y, x))
        return f' la potencia con el que {x} de como resultado {y} es {exponente}'
    except:
        if y <= 1:
            return False

x = int(input("ingrese primer numero: "))
y = int(input("ingrese segundo numero: "))
print(potencia(x, y))