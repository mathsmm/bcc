def mediana(n1, n2, n3):
    maximo = max(n1, n2, n3)
    minimo = min(n1, n2, n3)
    return n1 + n2 + n3 - maximo - minimo

def main():
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    n3 = int(input("Informe o terceiro número: "))
    print("A mediana dos três números é:", mediana(n1, n2, n3))

if __name__ == "__main__":
    main()