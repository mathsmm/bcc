contador_vertice = 1
perimetro_acumulado = 0
while True:
    str_x_novo = input(f"Digite o valor da coordenada X do vértice {contador_vertice} (Enter para parar): ")
    if str_x_novo == "":
        perimetro_acumulado += ((x_novo - x_primeiro_vertice) ** 2 + (y_novo - y_primeiro_vertice) ** 2) ** 0.5
        break
    x_novo = float(str_x_novo)

    str_y_novo = input(f"Digite o valor da coordenada Y do vértice {contador_vertice} (Enter para parar): ")
    if str_y_novo == "":
        perimetro_acumulado += ((x_novo - x_primeiro_vertice) ** 2 + (y_novo - y_primeiro_vertice) ** 2) ** 0.5
        break
    y_novo = float(str_y_novo)

    if contador_vertice == 1:
        x_primeiro_vertice = x_novo
        y_primeiro_vertice = y_novo
        x_antigo = x_novo
        y_antigo = y_novo
    else:
        perimetro_acumulado += ((x_novo - x_antigo) ** 2 + (y_novo - y_antigo) ** 2) ** 0.5
        x_antigo = x_novo
        y_antigo = y_novo

    contador_vertice += 1

print(f"O perímetro do polígono é: {perimetro_acumulado}")