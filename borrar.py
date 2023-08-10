ingreso = str(input("ingresa el numero hexadecimal"))
salida = 0
alternativo = []
inverso = []
for x in ingreso.lower():
    if x == "a":
        x = 10
    elif x == "b":
        x = 11
    elif x == "c":
        x = 12
    elif x == "d":
        x = 13
    elif x == "e":
        x = 14
    elif x == "f":
        x = 15

    alternativo.append(int(x))
    print(alternativo)

# invertir la lista
for x in range(len(alternativo) - 1, -1, -1):
    inverso.append(alternativo[x])
    print(inverso)

# hacer la operación
for indice, x in enumerate(inverso):
    salida += x * (16**indice)

print(salida, "(10)")
