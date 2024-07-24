def number_of_days(month, year):
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def main():
    month = int(input("Digite o mês: "))
    year = int(input("Digite o ano: "))
    print("O número de dias do mês especificado é:", number_of_days(month, year))

if __name__ == "__main__":
    main()