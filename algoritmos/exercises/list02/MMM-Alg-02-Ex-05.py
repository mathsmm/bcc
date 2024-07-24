import math

quantidadeCentavos = int(input("Digite a quantidade de centavos, de 0 a 99: "))
moeda50 = quantidadeCentavos // 50
quantidadeCentavos = quantidadeCentavos % 50
moeda25 = quantidadeCentavos // 25
quantidadeCentavos = quantidadeCentavos % 25
moeda10 = quantidadeCentavos // 10
quantidadeCentavos = quantidadeCentavos % 10
moeda5 = quantidadeCentavos // 5
quantidadeCentavos = quantidadeCentavos % 5
moeda1 = quantidadeCentavos // 1

print(f"O troco é: {moeda50} moeda(s) de 50 centavos, {moeda25} moeda(s) de 25 centavos, {moeda10} moeda(s) de 10 centavos, {moeda5} moeda(s) de 5 centavos e {moeda1} moeda(s) de 1 centavo.")