ano = int(input("Digite um ano: "))

msg_retorno = ""

if ano % 400 == 0:
    msg_retorno = "O ano é bissexto"
elif ano % 100 == 0:
    msg_retorno = "O ano não é bissexto"
elif ano % 4 == 0:
    msg_retorno = "O ano é bissexto"
else:
    msg_retorno = "O ano não é bissexto"

print(msg_retorno)