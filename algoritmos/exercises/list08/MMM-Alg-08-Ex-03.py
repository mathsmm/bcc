def recursive_is_palindrome(string: str):
    up_string = string.upper()
    new_string = ""

    for char in up_string:
        if ord(char) >= 65 and ord(char) <= 90:
            new_string += char

    def rec_is_palindrome(str: str):
        if len(str) <= 1:
            return True
        return str[0] == str[-1] and rec_is_palindrome(str[1:-1])

    return rec_is_palindrome(new_string)


def main():
    print("'Hannah!?' é um palíndromo? ", recursive_is_palindrome("Hannah"))
    print("'Ovo' é um palíndromo? ", recursive_is_palindrome("Ovo"))
    print("'Socorram-me, subi no onibus em marrocos' é um palíndromo? ", recursive_is_palindrome("Socorram-me, subi no onibus em marrocos"))
    print("'Meu camarada Thomas!' é um palíndromo? ", recursive_is_palindrome("Meu camarada Thomas!"))

if __name__ == "__main__":
    main()