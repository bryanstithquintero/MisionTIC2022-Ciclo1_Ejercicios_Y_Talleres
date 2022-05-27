lineas = []
print (input("escriba algunas lineas "))
while True:
    save = input ()
    if save:
        lineas.append(save.upper())
    else:
        break
for a in lineas:
    print(a)