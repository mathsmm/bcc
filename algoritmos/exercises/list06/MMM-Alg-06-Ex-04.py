def str_input_to_list_without_duplicates():
    list = []
    while True:
        str_input = input("Informe uma palavra: ")
        if str_input == "":
            break
        elif str_input in list:
            continue
        else:
            list.append(str_input)
    return list


def main():
    list = str_input_to_list_without_duplicates()
    print(list)

if __name__ == "__main__":
    main()