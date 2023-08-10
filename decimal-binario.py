while True:
    decimal = int(input("ingresa un decimal: "))
    div_binario = 0  # división entera
    binario = ""
    binario_reves = ""

    while div_binario != 1:
        binario_reves += str(decimal % 2)
        div_binario = decimal // 2
        decimal = div_binario

    binario_reves = binario_reves + "1"

    for x in range(len(binario_reves) - 1, -1, -1):
        binario += binario_reves[x]

    print(f"Su equivalente binario es = {binario}(2)")
