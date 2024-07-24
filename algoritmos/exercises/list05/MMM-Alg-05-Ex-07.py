def verificar_validade_triangulo(lado1, lado2, lado3):
    if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
        return False
    else:
        return True

def main():
    lado1 = float(input("Informe o comprimento do primeiro lado do triângulo: "))
    lado2 = float(input("Informe o comprimento do segundo lado do triângulo: "))
    lado3 = float(input("Informe o comprimento do terceiro lado do triângulo: "))
    if verificar_validade_triangulo(lado1, lado2, lado3):
        print("O triângulo é válido!")
    else:
        print("O triângulo é inválido!")

if __name__ == "__main__":
    main()