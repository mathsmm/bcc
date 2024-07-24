import math


l = float(input("Digite o valor do lado: "))
n = float(input("Digite o valor do número de lados: "))

area_poligono_regular = (l ** 2 * n) / (4 * math.tan(math.pi / n))