def rec_dec_to_bin(n: int):
    pre_converted = {0: "0", 1: "1"}
    if n in pre_converted:
        return pre_converted[n]
    r = n % 2
    result =  rec_dec_to_bin(n // 2) + str(r)
    return result


def main():
    print(rec_dec_to_bin(15))

if __name__ == "__main__":
    main()