def has_unique_chars(str: str):
    list = []
    aux_set = set(list)

    for char in str:
        if char in aux_set:
            return False
        else:
            aux_set.add(char)

    return True


def main():
    str1 = 'abcdefghijklmnopqrstuvwxyz1234'
    str2 = 'ferramenta'
    print(has_unique_chars(str1))
    print(has_unique_chars(str2))

if __name__ == "__main__":
    main()