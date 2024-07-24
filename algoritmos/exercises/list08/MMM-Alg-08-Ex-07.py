def iterative_dec_to_bin(q: int):
    result = ""
    while q != 0:
        r = q % 2
        result = str(r) + result
        q = q // 2
    return result


def main():
    print(iterative_dec_to_bin(15))

if __name__ == "__main__":
    main()