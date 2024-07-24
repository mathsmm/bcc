while True:
    bits = input("Informe uma sequência de 8 bits (Deixe em branco para parar): ")
    _continue = False

    if bits == "":
        break
    elif len(bits) != 8:
        print("ERRO: Você deve fornecer uma sequência de 8 (oito) bits.")
        _continue = True

    mostrar_terceiro_erro = False
    for bit in bits:
        if bit != "1" and bit != "0":
            mostrar_erro = True
            _continue = True
            break

    if mostrar_terceiro_erro:
        print("ERRO: Você deve digitar somente 0s ou 1s.")
    if _continue:
        continue

    qtd_1s = bits.count("1")
    bit_paridade = str
    if (qtd_1s % 2) == 0:
        bit_paridade = "0"
    else:
        bit_paridade = "1"

    print(f"Para paridade par, o bit de paridade de {bits} deve ser: {bit_paridade}")