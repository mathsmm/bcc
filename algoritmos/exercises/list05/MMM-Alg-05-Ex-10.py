def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def main():
    n = int(input("Informe um número. Será verificado se ele é primo: "))
    if isPrime(n):
        print("O número {} é primo.".format(n))
    else:
        print("O número {} não é primo.".format(n))

if __name__ == "__main__":
    main()
