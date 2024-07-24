lado_1 = float(input("Informe o comprimento do primeiro lado do triângulo: "))
lado_2 = float(input("Informe o comprimento do segundo lado do triângulo: "))
lado_3 = float(input("Informe o comprimento do terceiro lado do triângulo: "))

mensagem_resposta = ""

if   lado_1 == lado_2 == lado_3:
    mensagem_resposta = "O triângulo é equilátero"
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    mensagem_resposta = "O triângulo é isósceles"
elif lado_1 != lado_2 != lado_3:
    mensagem_resposta = "O triângulo é escaleno"
else:
    mensagem_resposta = "Um ou mais lados informados são inválidos"

print(mensagem_resposta)