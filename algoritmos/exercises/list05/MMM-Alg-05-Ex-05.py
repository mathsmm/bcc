def ordinal(inteiro):
    tupla_ordinais = (
        "Primeiro",
        "Segundo",
        "Terceiro",
        "Quarto",
        "Quinto",
        "Sexto",
        "Sétimo",
        "Oitavo",
        "Nono",
        "Décimo",
        "Décimo primeiro",
        "Décimo segundo"
    )
    return tupla_ordinais[inteiro - 1]


def main():
    i = 1
    while i <= 12:
        print(f"Ordinal do número {i}: {ordinal(i)}")
        i += 1


if __name__ == "__main__":
    main()
