message = input("Informe a mensagem a ser operada pela cifra de César: ")
displacement = int(input("Informe o deslocamento da cifra: "))

accumulated_str = ""
for char in message:
    ord_char = ord(char)
    if ord_char >= 97 and ord_char <= 122:
        if ord_char + displacement > 122:
            displaced_char = chr((ord_char + displacement) - 26)
        elif ord_char + displacement < 97:
            displaced_char = chr((ord_char + displacement) + 26)
        else:
            displaced_char = chr(ord_char + displacement)
    elif ord_char >= 65 and ord_char <= 90:
        if ord_char + displacement > 90:
            displaced_char = chr((ord_char + displacement) - 26)
        elif ord_char + displacement < 65:
            displaced_char = chr((ord_char + displacement) + 26)
        else:
            displaced_char = chr(ord_char + displacement)
    else:
        displaced_char = char

    accumulated_str += displaced_char


print(accumulated_str)

"""
caracteres_minúsculos = {"a": 97, "z": 122}
caracteres_maiúsculos = {"A": 65, "Z": 90}
"""