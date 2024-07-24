def int_input_to_sum_of_lists():
    negative_numbers = []
    zeros = []
    positive_numbers = []

    while True:
        str_input = input("Informe um número inteiro (Enter para parar): ")
        if str_input == "":
            break

        int_input = int(str_input)

        if int_input < 0:
            negative_numbers.append(int_input)
        elif int_input > 0:
            positive_numbers.append(int_input)
        else:
            zeros.append(int_input)

    return negative_numbers + zeros + positive_numbers


def main():
    num_list = int_input_to_sum_of_lists()
    for n in num_list:
        print(n)

if __name__ == "__main__":
    main()