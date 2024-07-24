def calcular_tarifa(distancia_percorrida):
    valor_inicial = 4
    taxa_140metros = 0.25
    return valor_inicial + taxa_140metros * (distancia_percorrida * 1000 / 140)

def main():
    distancia = float(input("Informe a distância, em quilômetros, que o táxi percorreu: "))
    print(f"O valor da tarifa será de: R${calcular_tarifa(distancia):.02f}")

if __name__ == "__main__":
    main()