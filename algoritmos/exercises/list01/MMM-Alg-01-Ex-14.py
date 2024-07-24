lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

l = (lado1 + lado2 + lado3) / 2

area_triangulo = (l * (l - lado1) * (l - lado2) * (l - lado3)) ** 0.5

print("A área do triângulo é:", area_triangulo)