def convert_to_dec(number: str, base: int):
    if base < 2 or base > 16:
        return None

    number = number.upper()
    number_list = []

    for char in number:
        number_list.append(char)

    bef_dot_list = []
    aft_dot_list = []

    len_number_list = len(number_list)
    i = 0
    while i < len_number_list:
        if number_list[i] == '.' or number_list[i] == ',':
            break
        else:
            bef_dot_list.append(number_list[i])
        i += 1

    if i < len_number_list:
        i += 1
        while i < len_number_list:
            aft_dot_list.append(number_list[i])
            i += 1

    symbols = [
        '0', '1', '2', '3', 
        '4', '5', '6', '7', 
        '8', '9', 'A', 'B', 
        'C', 'D', 'E', 'F'
    ]

    result = 0

    len_bef_dot_list = len(bef_dot_list)
    i = 0
    while i < len_bef_dot_list:
        result += symbols.index(bef_dot_list[i]) * base ** (len_bef_dot_list - i - 1)
        i += 1


    len_aft_dot_list = len(aft_dot_list)
    i = 0
    while i < len_aft_dot_list:
        result += symbols.index(aft_dot_list[i]) * base ** (-i - 1)
        i += 1

    return result

print(convert_to_dec('1001.101', 2))
print(convert_to_dec('E2AC', 16))