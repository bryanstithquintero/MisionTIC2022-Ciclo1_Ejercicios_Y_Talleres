#prueba del ejercicio 1
import taller as t
nombre = str (input ("ingrese su nombre "))
print (t.ejercicio_1(nombre))
#prueba otra forma ejercicio 1
nombre = str("bryan")
print (t.ejercicio_1(nombre))

#prueba del ejercicio 2
numero = int (input ("ingrese un numero "))
print (t.ejercicio_2(numero))
#prueba otra forma ejercicio 2
numero = 32
print(t.ejercicio_2(numero))

#prueba del ejercicio 3
precio = int(input("ingrese el precio "))
iva = float(input("ingrese el iva "))
print (t.ejercicio_3(precio,iva))
#prueba otra forma del ejercicio 3
precio = 100
iva = 0.10
print (t.ejercicio_3(precio,iva))

#prueba ejercicio 4
r = 13
print  (t.ejercicio_4(r))
#prueba otra forma del ejercicio 4
r = int(input("ingrese el radio "))
print (t.ejercicio_4(r))

#prueba ejercicio 5
numero_entero = int(input("ingrese un numero entero "))
print (t.ejercicio_5(numero_entero))
#prueba otra forma ejercicio 5
numero_entero = 32
print (t.ejercicio_5(numero_entero))

#prueba ejercicio 5
peso = float(input ("ingrese su peso "))
estatura = float(input ("ingrese su estatura "))
print (t.ejercicio_6(peso, estatura))

#prueba ejercicio 7
muneca = 34
payaso = 78
print (t.ejercicio_7 (muneca, payaso))

#prueba ejercicio 8
barras_vendidas = 4
print (t.ejercicio_8 (barras_vendidas))

#prueba ejercicio 9
ahorros = float (input("ingrese el monto "))
print (t.ejercicio_9(ahorros))
#prueba otra forma ejercicio 9
ahorros = 1000000
print (t.ejercicio_9(ahorros))

#prueba ejercicio 10
tiempo_en_segundos = 300000
print (t.ejercicio_10  (tiempo_en_segundos))