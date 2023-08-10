binario = []
decimal = 0

print(
    """
Esta es una calculadora para convertir numeros del sistema binarios al sistema decimal.
Asi es como funciona este programa:

1) Para poder ingresar el número decimal que deseas convertir deber ingresar
digito por digito.
2) Si te equivocaste puedes escribir borrar para despues corregir.
3) Si cuando ayas terminado de digitar el número binario presiona '.' para convertir el número.
4) Cuando quieras finalicar escribe: 'salir' para finalizar el programa
      
La belleza no se alcanza con dinero, sino con riqueza."""
)
while True:
    nuevo = str(input("introduza el nuevo elemento: "))

    if nuevo == "1" or nuevo == "0":
        binario.append(nuevo)
        print(binario)

    elif nuevo.lower() == "borrar":
        print(nuevo)
        eliminar = len(binario) - 1
        del binario[eliminar]
        print(binario)

    elif nuevo == ".":
        str_binario = "".join(binario)
        str_binario = str_binario.replace(" ", "")
        print(f"El numero introducido es: {str_binario}(2)")
        str_binario_invertido = ""
        for i in range(len(str_binario) - 1, -1, -1):
            str_binario_invertido += str_binario[i]
        for indice, x in enumerate(str_binario_invertido):
            x = int(x)
            decimal += x * (2**indice)
        print(f"Su equivalente es = {decimal}(10)")

    elif nuevo.lower() == "salir":
        print("Espero verte pronto :)")
        break
    else:
        print("Caractér no válido")
