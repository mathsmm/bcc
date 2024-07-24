def input_to_int_list():
    int_list = []
    while True:
        int_input = int(input("Informe um número inteiro (zero para parar): "))
        if int_input == 0:
            break

        int_list.append(int_input)

    return int_list

def bubble_sort(array):
    tmp = int

    i = 0
    while i < len(array):
        j = len(array) - 1
        while j > 0:
            if array[j] < array[j - 1]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
            j -= 1
        i += 1

def remove_n_extreme_values(array, n):
    if n < 0:
        return None

    new_list = []
    i = n
    while i < len(array) - n:
        new_list.append(array[i])
        i += 1

    return new_list


def main():
    original_list = input_to_int_list()
    n = int(input("Informe o número de elementos a serem retirados dos extremos: "))

    if len(original_list) < (n + n):
        print("Erro: o número de elementos deve ser maior que o dobro do valor especificado anteriormente.")
        return None

    list = original_list

    bubble_sort(list)
    new_list = remove_n_extreme_values(list, n)

    print()
    print("Lista modificada:")
    print(new_list)
    print()
    print("Lista original:")
    print(original_list)

if __name__ == "__main__":
    main()