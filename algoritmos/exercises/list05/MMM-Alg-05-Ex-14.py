def is_magic_date(day, month, year):
    if day * month == (year % 100):
        return True
    else:
        return False

def main():
    day = int(input("Digite o dia: "))
    month = int(input("Digite o mês: "))
    year = int(input("Digite o ano: "))

    if is_magic_date(day, month, year):
        print("Data mágica!")
    else:
        print("Data não mágica!")

if __name__ == "__main__":
    main()