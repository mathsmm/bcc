import math

latitude1 = float(input("Digite a latitude do primeiro ponto: "))
longitude1 = float(input("Digite a longitude do primeiro ponto: "))
latitude2 = float(input("Digite a latitude do segundo ponto: "))
longitude2 = float(input("Digite a longitude do segundo ponto: "))

distancia = 6371.01 * math.acos(math.sin(math.radians(latitude1)) * math.sin(math.radians(latitude2)) + math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.cos(math.radians(longitude1 - longitude2)))

print("A distância entre os dois pontos é:", distancia, "km")