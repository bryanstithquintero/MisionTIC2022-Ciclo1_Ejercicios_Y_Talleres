num = int(input("ingrese un numero "))
if num <0:
    print("ingrse un numero valido")
while num > 0:
    print(num, end=",")
    num = num - 1
    if num == 0:
        print(num, end=" ")

#con funcion
def conteo (num:int):
    if num < 0:
        return "ingrese un numero valido"
    while num > 0:
        print(num, end=",")
        num = num - 1
        if num == 0:
            print(num, end=" ")
    return " "

num = int(input("ingrese un numero "))
print(conteo(num))