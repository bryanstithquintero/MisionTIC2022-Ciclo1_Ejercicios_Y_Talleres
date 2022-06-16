padres = [] #se empieza con lista vacia pues ahi se agrega info
hijos = []
for k in range(3): #el range 3 es para la cantidad de valores que se agregaran o preguntaran
    pa = input("ingrese el nombre del padre: ")
    ma = input('ingrese el nombre de la madre: ')
    padres.append([pa, ma]) #asi se agrega lo que se escriba
    cant = int(input('cuantos hijos tiene esta familia: '))
    hijos.append([])
    for x in range(cant):
        nom = input('ingrese el nombre del hijo: ')
        hijos[k].append(nom)
print('listado del padre madre y sus hijos')
for k in range(3):
    print('padre:', padres[k][0])
    print('madre:', padres[k][1])
    for x in range(len(hijos[k])): #len es para saber cuantos se agregaron 
        print('hijos:', hijos[k][x])
print('listado del padre y cantidad hijos tiene')
for x in range(3):
    print('padre:', padres[x][0])
    print('cantidad de hijos:', len(hijos[x]))