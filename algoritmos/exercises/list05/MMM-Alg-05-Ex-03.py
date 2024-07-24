def calcular_taxa_envio(qtd_itens):
    return 10.95 + 2.95 * (qtd_itens - 1)

def main():
    qtd_itens = int(input("Informe a quantidade de itens: "))
    print(f"O valor da taxa de envio será de: R${calcular_taxa_envio(qtd_itens):.02f}")

if __name__ == "__main__":
    main()