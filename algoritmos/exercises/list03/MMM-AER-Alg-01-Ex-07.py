nv_volume = float(input("Informe o nível de volume em decibéis de um som: "))

mensagem_resposta = ""

if   nv_volume == 40:
    mensagem_resposta = "O volume é equivalente ao de uma sala silenciosa"
elif nv_volume > 40 and nv_volume < 70:
    mensagem_resposta = "O volume está entre o de uma sala silenciosa e um despertador"
elif nv_volume == 70:
    mensagem_resposta = "O volume é equivalente ao de um despertador"
elif nv_volume > 70 and nv_volume < 106:
    mensagem_resposta = "O volume está entre o de um despertador e um cortador de grama"
elif nv_volume == 106:
    mensagem_resposta = "O volume é equivalente ao de um cortador de grama"
elif nv_volume > 106 and nv_volume < 130:
    mensagem_resposta = "O volume está entre o de um cortador de grama e uma britadeira"
elif nv_volume == 130:
    mensagem_resposta = "O volume é equivalente ao de uma britadeira"
else:
    mensagem_resposta = "O volume informado é inválido"

print(mensagem_resposta)