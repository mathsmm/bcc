def recursive_total_sum():
    sum = 0
    n = input("Digite um número: ")
    if n != "":
        sum += float(n) + recursive_total_sum()
    return sum


def main():
    print(recursive_total_sum())

if __name__ == "__main__":
    main()