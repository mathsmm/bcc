anos_cronologicos = float(input("Informe os anos cronológicos. Eles serão convertidos para anos caninos: "))

mensagem_resposta = ""
anos_caninos = 0

if anos_cronologicos < 0:
    mensagem_resposta = "O número informado deve ser maior ou igual a zero"
elif anos_cronologicos <= 2:
    anos_caninos = anos_cronologicos * 10.5
    mensagem_resposta = f"Idade canina: {anos_caninos}"
else:
    anos_caninos = 21 + ((anos_cronologicos - 2) * 4)
    mensagem_resposta = f"Idade canina: {anos_caninos}"

print(mensagem_resposta)