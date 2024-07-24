def return_list_of_dividers(number: int):
    dividers_list = []

    i = 1
    while i <= number:
        if number % i == 0:
            dividers_list.append(i)
        i += 1

    return dividers_list


def main():
    n = int(input("Informe um número. Este programa imprimirá seus divisores: "))
    dividers_list = return_list_of_dividers(n)
    print("Divisores:", dividers_list)

if __name__ == "__main__":
    main()