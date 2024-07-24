posicao = input("Informe uma posição do tabuleiro de xadrez: ")

coluna = posicao[:len(posicao)//2]
linha = posicao[len(posicao)//2:]

msg_retorno = ""

if coluna == "a":
    if int(linha) % 2 == 0:
        msg_retorno = "Brancas"
    else:
        msg_retorno = "Pretas"
elif coluna == "b":
    if int(linha) % 2 == 0:
        msg_retorno = "Pretas"
    else:
        msg_retorno = "Brancas"
elif coluna == "c":
    if int(linha) % 2 == 0:
        msg_retorno = "Brancas"
    else:
        msg_retorno = "Pretas"
elif coluna == "d":
    if int(linha) % 2 == 0:
        msg_retorno = "Pretas"
    else:
        msg_retorno = "Brancas"
elif coluna == "e":
    if int(linha) % 2 == 0:
        msg_retorno = "Brancas"
    else:
        msg_retorno = "Pretas"
elif coluna == "f":
    if int(linha) % 2 == 0:
        msg_retorno = "Pretas"
    else:
        msg_retorno = "Brancas"
elif coluna == "g":
    if int(linha) % 2 == 0:
        msg_retorno = "Brancas"
    else:
        msg_retorno = "Pretas"
elif coluna == "h":
    if int(linha) % 2 == 0:
        msg_retorno = "Pretas"
    else:
        msg_retorno = "Brancas"

print(msg_retorno)