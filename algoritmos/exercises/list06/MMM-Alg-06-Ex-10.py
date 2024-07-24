def format_list(list):
    result_str = ""
    i = 0
    len_list = len(list)
    while i < len_list:
        if len_list == 1:
            result_str = str(list[i])
            return result_str
        elif i == 0:
            result_str = str(list[i])
        elif i == len_list - 1:
            result_str += " e " + str(list[i])
        else:
            result_str += ", " + str(list[i])

        i += 1
    return result_str


def main():
    list = ['maçãs', 'bananas', 'laranjas', 'melancias']
    print(format_list(list))

if __name__ == "__main__":
    main()