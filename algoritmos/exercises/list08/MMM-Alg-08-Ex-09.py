# x = float(input("Informe o valor de x: "))
# raiz = x / 2

# while ((raiz * raiz) - x) > (10**-12) or ((raiz * raiz) - x) < -(10**-12):
#     raiz = (raiz + (x / raiz)) / 2

# print("A raiz de x é aproximadamente ", raiz)


def rec_square(n, estimation=1):
    if abs(estimation ** 2 - n) <= (10 ** - 12):
        return estimation
    return rec_square(n, (estimation + (n / estimation)) / 2)


def main():
    print("Raiz de 1:", rec_square(1))
    print("Raiz de 2:", rec_square(2))
    print("Raiz de 3:", rec_square(3))
    print("Raiz de 4:", rec_square(4))
    print("Raiz de 5:", rec_square(5))
    print("Raiz de 6:", rec_square(6))
    print("Raiz de 7:", rec_square(7))
    print("Raiz de 8:", rec_square(8))
    print("Raiz de 9:", rec_square(9))
    print("Raiz de 16:", rec_square(16))
    print("Raiz de 25:", rec_square(25))

if __name__ == "__main__":
    main()