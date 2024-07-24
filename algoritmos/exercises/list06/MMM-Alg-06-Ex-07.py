def return_list_of_dividers(number: int):
    dividers_list = []

    i = 1
    while i <= number:
        if number % i == 0:
            dividers_list.append(i)
        i += 1

    return dividers_list

def number_is_perfect(number: int):
    dividers_list = return_list_of_dividers(number)
    dividers_list.pop()

    sum = 0
    for n in dividers_list:
        sum += n

    if sum == number:
        return True

    return False


def main():
    for n in range(1, 10001):
        if number_is_perfect(n) == True:
            print(f"{n} é perfeito!")

if __name__ == "__main__":
    main()