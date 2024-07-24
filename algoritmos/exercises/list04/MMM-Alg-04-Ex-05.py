valor_acumulado = 0
idade = str
while idade != "":
    idade = input("Informe sua idade (Enter para parar): ")
    if idade == "":
        continue
    idade = int(idade)

    if idade <= 2:
        valor_acumulado += 0
    elif idade >= 3 and idade <= 12:
        valor_acumulado += 14
    elif idade >= 65:
        valor_acumulado += 18
    else:
        valor_acumulado += 23
else:
    print(f"O valor total é de R${valor_acumulado:.02f}")