vlr_inicial = float(input("Informe o valor inicial depositado na conta, em reais: "))

montante_um_ano = vlr_inicial * ((1 + 0.12) ** 1)
montante_dois_anos = vlr_inicial * ((1 + 0.12) ** 2)
montante_tres_anos = vlr_inicial * ((1 + 0.12) ** 3)

print("O saldo de sua conta, com taxa de 12% ao ano, será: ")
print(f"Em um ano, R${montante_um_ano:.2f}")
print(f"Em dois anos, R${montante_dois_anos:.2f}")
print(f"Em três anos, R${montante_tres_anos:.2f}")