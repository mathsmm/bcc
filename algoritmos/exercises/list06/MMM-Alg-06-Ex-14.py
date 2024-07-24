def precedence(operator: str):
    operator_list = ['+-', '*/', '^']

    for element in operator_list:
        for char in element:
            if operator == char:
                return operator_list.index(element) + 1

    return -1

def main():
    operator = input("Informe um operador (+, -, *, / ou ^): ")
    operator_list = ['+', '-', '*', '/', '^']

    if operator not in operator_list:
        print("ERRO: O operator informado não é válido.")
    else:
        print("Ordem de precedência:", precedence(operator))    

if __name__ == "__main__":
    main()