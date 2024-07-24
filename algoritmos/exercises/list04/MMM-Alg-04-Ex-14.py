n_binario = input("Digite um número binário: ")
n_decimal = 0
for i in range(len(n_binario)):
    n_decimal += int(n_binario[i]) * 2 ** (len(n_binario) - i - 1)
print(n_decimal)