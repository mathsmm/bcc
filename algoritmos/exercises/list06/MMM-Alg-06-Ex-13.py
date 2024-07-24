def countRange(list, min_value, max_value):
    result = 0

    i = 0
    while i < len(list):
        if list[i] >= min_value and list[i] < max_value:
            result += 1

        i += 1

    return result

def main():
    list = [1, 1, 2, 3, 5, 7, 8, 9, 25, 30, 35]
    print(countRange(list, 5, 31))

if __name__ == "__main__":
    main()