# Senha aleatória
import random


def generate_password():
    accumulated_password = ""

    i = 0
    while i < len(range(random.randint(7, 10))):
        j = random.randint(33, 126)
        accumulated_password += chr(j)

        i += 1
    return accumulated_password

def main():
    print("Senha gerada:", generate_password())

if __name__ == "__main__":
    main()
