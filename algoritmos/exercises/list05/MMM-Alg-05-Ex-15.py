def hex2int(hexadecimal_char):
    hexadecimal_char = hexadecimal_char.upper()

    if hexadecimal_char == 'A':
        return 10
    elif hexadecimal_char == 'B':
        return 11
    elif hexadecimal_char == 'C':
        return 12
    elif hexadecimal_char == 'D':
        return 13
    elif hexadecimal_char == 'E':
        return 14
    elif hexadecimal_char == 'F':
        return 15
    else:
        return int(hexadecimal_char)

def int2hex(decimal_char):
    if decimal_char == 10:
        return 'A'
    elif decimal_char == 11:
        return 'B'
    elif decimal_char == 12:
        return 'C'
    elif decimal_char == 13:
        return 'D'
    elif decimal_char == 14:
        return 'E'
    elif decimal_char == 15:
        return 'F'
    else:
        return str(decimal_char)