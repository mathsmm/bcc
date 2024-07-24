# Converte uma string de número  com ponto racionário 
# para uma lista de números sem ponto racionário
def num_str_to_num_list(number: str):
    number_list = []

    for char in number:
        if char == '.' or char == ',':
            continue
        number_list.append(char)

    return number_list

# Retorna o índice do ponto decimal
def dot_index_of(number_seq: str):
    if '.' in number_seq:
        return number_seq.index('.')
    elif ',' in number_seq:
        return number_seq.index(',')
    else:
        return len(number_seq)

# Converte uma lista de caracteres que representam um número 
# de uma base entre 2 e 16 para um número de base 10
def convert_num_list_to_dec(number_list: list, base: int, dot_index: int):
    symbols = [
        '0', '1', '2', '3', 
        '4', '5', '6', '7', 
        '8', '9', 'A', 'B', 
        'C', 'D', 'E', 'F'
    ]

    result = 0

    len_number_list = len(number_list)
    i = 0
    while i < len_number_list:
        result += symbols.index(number_list[i]) * base ** (dot_index - i - 1)
        i += 1

    return result

# Conjunção das funções anteriores;
# Converte uma string de número de uma base 
# entre 2 e 16 para um número de base 10
def convert_to_dec(number: str, base: int):
    if base < 2 or base > 16:
        return None

    number = number.upper()

    number_list = num_str_to_num_list(number)

    dot_index = dot_index_of(number)

    return convert_num_list_to_dec(number_list, base, dot_index)


def convert_from_dec(number: int, base: int):
    if base < 2 or base > 16:
        return None

    symbols = [
        '0', '1', '2', '3', 
        '4', '5', '6', '7', 
        '8', '9', 'A', 'B', 
        'C', 'D', 'E', 'F'
    ]

    result = ""

    while number > 0:
        result = symbols[number % base] + result
        number //= base

    return result

def main():
    n_decimal = int(input("Digite um número de base 10 (inteiro): "))
    base_1 = int(input("Digite a base a qual o número será convertido: "))

    n_base_1 = convert_from_dec(int(n_decimal), base_1)
    print(f"O número {n_decimal} de base 10 em base {base_1} é {n_base_1}")

    n_base_qualquer = input("Digite um número de base qualquer (aceita-se número racional com ponto ou vírgula): ")
    base_2 = int(input("Digite a base do número informado: "))
    n_base_2 = convert_to_dec(n_base_qualquer, base_2)
    print(f"O número {n_base_qualquer} de base {base_2} em base 10 é {n_base_2}")

if __name__ == "__main__":
    main()