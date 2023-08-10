sistema_decimal = "0123456789"
sistema_octal = "01234567"
sistema_hexadecimal = "0123456789abcdef"
sistema_binario = "01"
valor_de_pertenencia = True  # este valor lo utilizo para verificar si el númeor ingresado pertenece a sistema_numerico_input
resultado = 0

numero = str(input("Ingrese su numero que quiere convertir: "))
sistema_numerico_input = int(
    input(
        "ingresa la base del sistema numerico en el que está el numero que quieres convertir: "
    )
)
sistema_numerico_output = int(
    input("ingresa el sistema numerico al cual lo quieres convertir: ")
)

# asignación de los sistemas numericos
if sistema_numerico_input == 10:
    sistema_numerico_input = sistema_decimal
elif sistema_numerico_input == 16:
    sistema_numerico_input = sistema_hexadecimal
elif sistema_numerico_input == 8:
    sistema_numerico_input = sistema_octal
elif sistema_numerico_input == 2:
    sistema_numerico_input = sistema_binario
else:
    print("no tengo ese sistema númerico")


for x in numero:
    if valor_de_pertenencia == True:
        for y in str(sistema_numerico_input):
            if y == x:
                valor_de_pertenencia = True
                break
            else:
                valor_de_pertenencia = False
    else:
        break


# se van a convertir todos los valores a decimal y despues al sistema numerico requerido
if valor_de_pertenencia == True:
    numero_invertido = ""
    # binario - decimal
    if sistema_numerico_input == sistema_binario:
        # voy a invertir el string para que el indice coincida con el exponente cuando se multiplique
        for i in range(len(numero) - 1, -1, -1):
            numero_invertido += numero[i]

        # ahora se va a muntiplicar el numero por 2 elevado al indice correspondiente
        for indice, x in enumerate(numero_invertido):
            x = int(x)
            resultado += x * (2**indice)
        print(f"el resultado es {resultado} (10)")

    # octal - decimal
    if sistema_numerico_input == sistema_octal:
        # voy a invertir el string para que el indice coincida con el exponente cuando se multiplique
        for i in range(len(numero) - 1, -1, -1):
            numero_invertido += numero[i]

        # ahora se va a muntiplicar el numero por 2 elevado al indice correspondiente
        for indice, x in enumerate(numero_invertido):
            x = int(x)
            resultado += x * (8**indice)
        print(f"el resultado es {resultado} (10)")

    # hexadecimal - decimal
    if sistema_numerico_input == sistema_hexadecimal:
        # se hacen lista para poder separar cada termino, esto debido que por ejemplo a = 10
        # y ese 10 debe tener un índice para ese termino lo que es imposible hacerlo en un string
        numero_invertido = []
        auxiliar = []
        # se remplazan los valores alfabeticos por sus respectivos numericos
        for x in numero.lower():
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

            auxiliar.append(int(x))
        # se inierte el numero para que su indice coincida con la potencia que le debería corresponder
        for x in range(len(auxiliar) - 1, -1, -1):
            numero_invertido.append(auxiliar[x])
        # se hace las operaciones sumandolas a la varialbe resultado
        for indice, i in enumerate(numero_invertido):
            resultado += i * (16**indice)

        print(f"el resultado es {resultado} (10)")

else:
    print("el valor ingresado no pertenece a al sistema numerico")
