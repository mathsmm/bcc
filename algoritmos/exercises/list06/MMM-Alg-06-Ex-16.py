def str_is_integer(str: str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def precedence(operator: str):
    operator_list = ['+-', '*/', '^']

    for element in operator_list:
        for char in element:
            if operator == char:
                return operator_list.index(element) + 1

    return -1

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

def infix_to_postfix(infix_array):
    operators = []
    postfix_array = []

    for token in infix_array:
        if str_is_integer(token):
            postfix_array.append(token)
        elif token in operators:
            while len(operators) > 0 and operators[-1] != '(' and precedence(token) <= precedence(operators[-1]):
                postfix_array.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                postfix_array.append(operators.pop())
            operators.pop()

    while len(operators) > 0:
        postfix_array.append(operators.pop())

    return postfix_array


def main():
    expression = '1 * 2'
    token_list = expression_to_token_list(expression)
    print(token_list)
    postfix_list = infix_to_postfix(token_list)
    print(postfix_list)

if __name__ == "__main__":
    main()