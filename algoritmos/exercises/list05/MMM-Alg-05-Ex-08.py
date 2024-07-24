def corrigir_string(string):
    result = string[0].upper()
    string_mod = string[1:]

    i = 0
    while i < len(string_mod):
        if string_mod[i] == "." or string_mod[i] == "!" or string_mod[i] == "?":
            j = i + 1
            while ord(string_mod[j]) == 32:
                j += 1
            result += string_mod[i] + " " + string_mod[j].upper()
            i = j + 1
        else:
            result += string_mod[i]
            i += 1

    return result


def main():
    string_informada = input(
        "Informe uma string. Será atribuída a ela a correção de letras maiúsculas: ")
    print(f"String original:  {string_informada}")
    print(f"String corrigida: {corrigir_string(string_informada)}")


if __name__ == "__main__":
    main()
