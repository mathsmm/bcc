def hasOnlyDigitsOrSign(seq):
    for char in seq:
        ord_char = ord(char)
        if (ord_char < 48 or ord_char > 57) and (char != "+" and char != "-"):
            return False
    return True

def isInteger(string):
    stripped_str = string.strip()
    bool_hasOnlyDigitsOrSign = hasOnlyDigitsOrSign(stripped_str)

    if bool_hasOnlyDigitsOrSign == False:
        return False

    int_count_plus = stripped_str.count("+")
    int_count_minus = stripped_str.count("-")

    if (int_count_plus + int_count_minus) > 1:
        return False

    if int_count_plus == 1 or int_count_minus == 1:
        if len(stripped_str) < 2:
            return False
        elif stripped_str[0] != "+" and stripped_str[0] != "-":
            return False
        else:
            return True
    else:
        if len(stripped_str) < 1:
            return False
        else:
            return True

def main():
    n = input("Informe um número. Será verificado se ele é um inteiro: ")
    if isInteger(n) == True:
        print("É inteiro")
    else:
        print("Não é inteiro")

if __name__ == "__main__":
    main()
