soma = 0
cont = 0
num = 1

while num != 0:
    num = float(input("Digite um número (0 para parar o cálculo da média): "))
    if num == 0 and cont == 0:
        print("Nenhum número foi digitado.")
        break
    elif num == 0:
        continue
    else:
        soma += num
        cont += 1
else:
    print(f"A soma dos números é {soma}")
    print(f"A média dos números é {soma / cont}")