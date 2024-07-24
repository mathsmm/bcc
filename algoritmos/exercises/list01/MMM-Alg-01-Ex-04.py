# 1 Hectare == 10000m²

largura_terreno = float(input("Informe o comprimento da largura do terreno, em metros: "))
profundidade_terreno = float(input("Informe o comprimento da profundidade do terreno, em metros: "))

area_terreno_hectare = (largura_terreno * profundidade_terreno) / 10000

print(f"Área do terreno: {area_terreno_hectare}hm2 (em hectares)")