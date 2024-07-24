def input_to_int_list():
    int_list = []
    while True:
        int_input = int(input("Informe um número inteiro (zero para parar): "))
        if int_input == 0:
            break

        int_list.append(int_input)

    return int_list

# Bubble sort escrito (ordem decrescente):
def bubble_sort(array):
    tmp = int

    i = 0
    while i < len(array):
        j = len(array) - 1
        while j > 0:
            if array[j] > array[j - 1]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
            j -= 1
        i += 1


def main():
    int_list = input_to_int_list()
    bubble_sort(int_list)
    print("Números em ordem decrescente:")
    print(int_list)

if __name__ == "__main__":
    main()