def calculate_average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)

def ask_and_average():
    list = []
    while True:
        str_input = input("Informe um número. Será calculada a média dos números informados: ")
        if str_input == "":
            break
        float_input = float(str_input)
        list.append(float_input)
    return list, calculate_average(list)

def under_average(list, average):
    return_list = []
    for i in list:
        if i < average:
            return_list.append(i)
    return return_list

def in_average(list, average):
    return_list = []
    for i in list:
        if i == average:
            return_list.append(i)
    return return_list

def over_average(list, average):
    return_list = []
    for i in list:
        if i > average:
            return_list.append(i)
    return return_list


def main():
    list, average = ask_and_average()
    print("A média dos números informados é:", average)
    print("Números abaixo da média:", under_average(list, average))
    print("Números iguais à média:", in_average(list, average))
    print("Números acima da média:", over_average(list, average))

if __name__ == "__main__":
    main()