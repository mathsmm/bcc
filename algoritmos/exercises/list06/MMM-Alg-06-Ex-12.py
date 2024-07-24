# Verifica se está em ordem crescente
# Ocorre verificando os elementos de um em um
# def is_ordered(list):
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             return False
#     return True

def input_to_int_list():
    int_list = []
    while True:
        str_input = input("Informe um número inteiro (Enter para parar): ")
        if str_input == "":
            break

        int_input = int(str_input)

        int_list.append(int_input)

    return int_list

def is_ordered(list):
    if len(list) == 0 or len(list) == 1:
        return True

    sorted_aux_list = sorted(list)
    sorted_reverse_aux_list = sorted(list, reverse=True)

    if list == sorted_aux_list or list == sorted_reverse_aux_list:
        return True
    return False

def main():
    list = input_to_int_list()
    if is_ordered(list):
        print("A lista está ordenada")
    else:
        print("A lista não está ordenada")
        
if __name__ == "__main__":
    main()