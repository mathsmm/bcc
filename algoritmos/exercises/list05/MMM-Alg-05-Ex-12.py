def is_good_password(password):
    if len(password) < 8:
        return False

    upper_flag = False
    numeric_flag = False

    for char in password:
        if char.isupper():
            upper_flag = True
        
        if char.isnumeric():
            numeric_flag = True

    if upper_flag and numeric_flag:
        return True
    else:
        return False

def main():
    password = input("Informe uma senha: ")
    if is_good_password(password):
        print("Senha válida")
    else:
        print("Senha inválida")


if __name__ == "__main__":
    main()



