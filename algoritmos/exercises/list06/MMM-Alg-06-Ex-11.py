import random


def mega_sena():
    list = []
    while True:
        number = random.randint(1, 60)
        
        if number in list:
            continue

        list.append(number)

        if len(list) == 6:
            break

    list.sort()
    return list

def main():
    list = mega_sena()
    print(list)

if __name__ == "__main__":
    main()