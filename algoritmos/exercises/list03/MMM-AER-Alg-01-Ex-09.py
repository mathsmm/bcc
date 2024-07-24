dia = int(input("Informe um dia de um mês, em número: "))
mes = int(input("Informe o mês do dia, em número: "))

msg_retorno = ""

if   dia == 1 and mes == 1:
    msg_retorno = "O feriado é: Confraternização universal"
elif dia == 21 and mes == 4:
    msg_retorno = "O feriado é: Tiradentes"
elif dia == 1 and mes == 5:
    msg_retorno = "O feriado é: Dia do trabalho"
elif dia == 7 and mes == 9:
    msg_retorno = "O feriado é: Independência do Brasil"
elif dia == 12 and mes == 10:
    msg_retorno = "O feriado é: Nossa Senhora Aparecida"
elif dia == 2 and mes == 11:
    msg_retorno = "O feriado é: Finados"
elif dia == 15 and mes == 11:
    msg_retorno = "O feriado é: Proclamação da República"
elif dia == 25 and mes == 12:
    msg_retorno = "O feriado é: Natal"
else:
    msg_retorno = "O dia e o mês informados não correspondem a um feriado nacional"

print(msg_retorno)