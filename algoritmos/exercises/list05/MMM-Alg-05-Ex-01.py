def calcular_hipotenusa(cateto1, cateto2):
    return (cateto1 ** 2 + cateto2 ** 2) ** 0.5

def main():
    cateto1 = float(input("Informe o primeiro cateto do triângulo retângulo: "))
    cateto2 = float(input("Informe o segundo cateto do triângulo retângulo: "))
    print("O comprimento da hipotenusa é:", calcular_hipotenusa(cateto1, cateto2))

if __name__ == "__main__":
    main()
