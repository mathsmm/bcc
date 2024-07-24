def expression_to_token_list(expression: str):
    expression = expression.replace(' ', '')
    token_list = []
    additive_operator_list = ['+', '-']

    token = expression[0]

    i = 1
    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            token += char
        elif char in additive_operator_list:
            previous_char = expression[i - 1]
            if previous_char == ')' or previous_char.isdigit() or previous_char == '':
                token_list.append(token) if token != '' else None
                token = ''
                token += char
            else:
                token_list.append(token) if token != '' else None
                token = ''
                token_list.append(char)
        else:
            token_list.append(token) if token != '' else None
            token = ''
            token_list.append(char)

        i += 1
    else:
        token_list.append(token) if token != '' else None


    return token_list

def main():
    expression = '1 + 2 * 3 - 4 ^ (4 * (x - 2))'
    token_list = expression_to_token_list(expression)
    print(token_list)

if __name__ == "__main__":
    main()