numero = 12
numero= [int(a) for a in str(numero)]
print(numero)
def validar_numero (numero:list):
    if numero[1] % 2 == 0 and numero[0] % 2 == 0:
        return "los dos digitos son pares"
    elif numero[0] % 2 == 0:
        return "el primer digito es par"
    elif numero[1] % 2 == 0:
        return "el segundo digito es par"
    else:
        return "el segundo digito es impar"

print(validar_numero(numero))