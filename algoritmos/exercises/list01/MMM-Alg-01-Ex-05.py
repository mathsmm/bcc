qtd_vasilhame_menos_de_um_litro = int(input(
    "Informe a quantidade de vasilhames de menos de um litro: "
))

qtd_vasilhame_mais_de_um_litro = int(input(
    "Informe a quantidade de vasilhames de mais de um litro: "
))

credito_centavos = (qtd_vasilhame_menos_de_um_litro * 10) + (qtd_vasilhame_mais_de_um_litro * 25)

credito_reais = float(credito_centavos) / 100

print(f"Crédito total dos vasilhames: R${credito_reais:.2f}")