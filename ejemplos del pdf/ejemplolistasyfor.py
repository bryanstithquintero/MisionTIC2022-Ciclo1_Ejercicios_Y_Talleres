nombres = []
edades = []
for x in range(2):
    nom = input("ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed = int(input("ingrese la edad de la persona: "))
    edades.append(ed)
print("nombre de las personas mayores de edad: ")
for x in range(2):
    if edades [x] >= 18:
        print(nombres[x])
        
lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista)
print(lista[0])
print(lista[0][0])
for x in range (len (lista [0])):
    print(lista[0][x], end=' ')
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x], end=' ')

lista2= [[1,2,3,4,5],[6,7,8,9,10]]
for k in range(len(lista2)):
    suma = 0
    for x in range(len(lista2[k])):
        suma = suma + lista2[k][x]
    print(suma)

lista3= [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
suma2 = 0
for k in range(len(lista3)):
    for x in range(len(lista3[k])):
        suma2 = suma2 + lista3 [k][x]
    print(suma2, end='-')

