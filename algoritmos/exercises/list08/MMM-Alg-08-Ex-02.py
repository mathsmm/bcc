pre_calculated = {0: 1, 1: 1}
def recursive_fibonacci(n):
    if n in pre_calculated:
        return pre_calculated[n]
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def main():
    print("Fibonacci de 5:", recursive_fibonacci(5))
    print("Fibonacci de 10:", recursive_fibonacci(10))
    print("Fibonacci de 20:", recursive_fibonacci(20))

if __name__ == "__main__":
    main()