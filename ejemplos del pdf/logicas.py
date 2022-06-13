fahr = input('ingrese la temperatura en grados fahrenheit: ')
#en el try se pone lo que deberia ir la formula
try:
    fahr = float(fahr)
    cel = (fahr - 32.0) * 5.0/9.0
    print(round (cel, 2))
#en except va si no se cumple vease, no se pone un numero
except:
    print('no ingreso ningun numero')

#normalmente se hace asi pero se puede usar evaluacion del guardia 
x = 6
y = 2
print(x>=2 and y !=0 and (x/y) > 2)

