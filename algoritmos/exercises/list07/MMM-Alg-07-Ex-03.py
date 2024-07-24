def reverse_search(dict: dict, value):
    result_list = []

    for key in dict:
        if dict[key] == value:
            result_list.append(key)

    return result_list

def main():
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 3, 'f': 2, 'g': 1}
    value = 3
    print(reverse_search(dict, value))

    value = 2
    print(reverse_search(dict, value))

if __name__ == "__main__":
    main()