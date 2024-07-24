n = int(input("Informe um número inteiro maior ou igual a 2: "))
if n < 2:
    print("O número informado é menor que 2.")
fator = 2
while fator <= n:
    if n % fator == 0:
        print(fator)
        n = n // fator
    else:
        fator += 1