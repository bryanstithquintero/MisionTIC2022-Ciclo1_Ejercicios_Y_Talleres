diccionario = {}
palabras = input("introduzca la lista de palabaras en formato palabra:traduccion separadas por coma: ")
for i in palabras.split(","):
    clave, valor = i.split(":")
    diccionario[clave] = valor
frase = input("introduzca una frase en espanol: ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")