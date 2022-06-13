fruta = 'banana'
#entre [] y un numero para la posicion, empieza siempre en cero 0
letra = fruta[0]
print(letra)
#la longitud de una cadena se usa con len
print(len(fruta))
#se puede imprimir parte de las cadenas especificando asi
print(fruta[:3])
print(fruta[3:])
#operador in, si algo esta en la segunda
var1= 'na'
var2 = 'banana'
print(var1 in var2)
#se puede hacer comparaciones y diferencias
palabra = 'banana'
if palabra == 'banana':
    print('esta bien')
else:
    print('no esta bien')
#otro ejemplo
palabra = 'pera'
if palabra < 'banana':
    print(f'tu palabra {palabra} viene antes de banana')
elif palabra > 'banana':
    print(f'tu palabra {palabra} viene despues de banana')
else:
    print('esta bien su palabra es banana')
# se puede buscar un booleano con startswith, donde se busca si la cadena empieza por un valor especifico
linea = 'que tengas un buen dia'
print(linea.startswith('q'))

#ejemplo con mas 
data = 'De stephen.marquard@uct.ac.za sat jan 5 09:14:16 2008'
encontrar = data.find('@')
print(encontrar)
espacio = data.find(' ',encontrar)
print(espacio)
host = data[encontrar + 1:espacio]
print(host)