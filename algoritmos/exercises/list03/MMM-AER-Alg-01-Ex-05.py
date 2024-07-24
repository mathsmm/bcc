mes = input("Informe o nome de um mês: ").upper()

mensagem_resposta = ""

if mes == "FEVEREIRO": 
    mensagem_resposta = "O mês possui 28 ou 29 dias"
elif mes == "ABRIL" or mes == "JUNHO" or mes == "SETEMBRO" or mes == "NOVEMBRO":
    mensagem_resposta = "O mês possui 30 dias"
else:
    mensagem_resposta = "O mês possui 31 dias"

print(mensagem_resposta)