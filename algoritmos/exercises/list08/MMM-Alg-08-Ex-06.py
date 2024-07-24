def rec_greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return rec_greatest_common_divisor(b, c)


def main():
    print("MDC de 625 e 300:", rec_greatest_common_divisor(625, 300))

if __name__ == "__main__":
    main()