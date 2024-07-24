nt_completa = input("Informe o nome de uma nota musical: ").upper()

nota =       nt_completa[:len(nt_completa)//2]
oitava = int(nt_completa[len(nt_completa)//2:])

msg_retorno = ""

if   nota == "C":
    msg_retorno = f"A frequência é {32.70375 * 2 ** (oitava - 1)} Hz"
elif nota == "D":
    msg_retorno = f"A frequência é {36.7075  * 2 ** (oitava - 1)} Hz"
elif nota == "E":
    msg_retorno = f"A frequência é {41.20375 * 2 ** (oitava - 1)} Hz"
elif nota == "F":
    msg_retorno = f"A frequência é {43.65375 * 2 ** (oitava - 1)} Hz"
elif nota == "G":
    msg_retorno = f"A frequência é {49       * 2 ** (oitava - 1)} Hz"
elif nota == "A":
    msg_retorno = f"A frequência é {55       * 2 ** (oitava - 1)} Hz"
elif nota == "B":
    msg_retorno = f"A frequência é {61.735   * 2 ** (oitava - 1)} Hz"
else:
    msg_retorno = "A nota informada é inválida"

print(msg_retorno)