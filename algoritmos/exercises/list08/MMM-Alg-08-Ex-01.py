pre_calculated = {0: 1, 1: 1}

def recursive_fat(n):
    if n in pre_calculated:
        return pre_calculated[n]
    return n * recursive_fat(n-1)


def main():
    print("Fatorial de 5:", recursive_fat(5))
    print("Fatorial de 10:", recursive_fat(10))
    print("Fatorial de 20:", recursive_fat(20))

if __name__ == "__main__":
    main()