qtd_lados = int(input("Informe a quantidade de lados do polígono regular: "))

mensagem_resposta = ""

if   qtd_lados == 3:
    mensagem_resposta = "O polígono é um triângulo"
elif qtd_lados == 4:
    mensagem_resposta = "O polígono é um quadrilátero"
elif qtd_lados == 5:
    mensagem_resposta = "O polígono é um pentágono"
elif qtd_lados == 6:
    mensagem_resposta = "O polígono é um hexágono"
elif qtd_lados == 7:
    mensagem_resposta = "O polígono é um heptágono"
elif qtd_lados == 8:
    mensagem_resposta = "O polígono é um octógono"
elif qtd_lados == 9:
    mensagem_resposta = "O polígono é um eneágono"
elif qtd_lados == 10:
    mensagem_resposta = "O polígono é um decágono"
else:
    mensagem_resposta = "A quantidade de lados deve estar entre 3 e 10, incluindo o 3 e o 10"

print(mensagem_resposta)