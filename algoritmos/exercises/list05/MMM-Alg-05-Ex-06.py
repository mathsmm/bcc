def centralizar_str(string, largura_termimal):
    metade_len_str = len(string) // 2
    metade_larg_terminal = largura_termimal // 2
    result = ""

    i = 1
    while i <= metade_larg_terminal:
        result += " "
        i += 1
    
    j = 1
    while j <= metade_len_str:
        result = result[:-1]
        j += 1

    return result + string

def main():
    str_informada = input("Informe uma string qualquer: ")
    larg_terminal = int(input("Informe a largura do terminal: "))
    print(centralizar_str(str_informada, larg_terminal))

if __name__ == "__main__":
    main()