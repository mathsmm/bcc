# Aluno: Matheus Marchi Moro
# 
# escreva o codigo de cada questao no espaço especificado abaixo


# ------------------------ QUESTAO 1 -----------------------------------
# coloque aqui o código da questão 1

def concept_to_num_grade(concept: str):
    concept_dict = {
        "A+": 4.0,
        "A":  4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B":  3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C":  2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D":  1.0,
        "F":  0.0,
    }

    return concept_dict[concept]


# ------------------------ QUESTAO 2 -----------------------------------
# coloque aqui o código da questão 2

def concept_grades_input_to_list():
    result = []
    while True:
        str_input = input("Digite uma nota-conceito (vazio para parar): ")
        if str_input == "":
            break
        result.append(str_input.upper())

    return result

def calculate_concept_grades(concept_grade_list: list):
    if len(concept_grade_list) == 0:
        return None
    sum = 0.0
    for concept_grade in concept_grade_list:
        sum += concept_to_num_grade(concept_grade)

    return sum / len(concept_grade_list)


# ------------------------ QUESTAO 3 -----------------------------------
# coloque aqui o código da questão 3

def input_to_int():
    return int(input("Digite um número inteiro: "))

def return_first_prime_num(num: int):
    while True:
        num += 1
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            return num


# ------------------------ QUESTAO 4 -----------------------------------
# coloque aqui o código da questão 4

# ALTERNATIVA a)

def criaBaralho():
    naipe_dict = { 0: "o", 1: "s", 2: "c", 3: "p" }
    valores_dict = { 1: "A", 10: "D", 11: "J", 12: "Q", 13: "K" }

    cartas_list = []
    for i in range(4):
        for j in range(1, 14):
            naipe = naipe_dict[i]
            valor = valores_dict[j] if j in valores_dict else str(j)
            cartas_list.append(valor + naipe)

    return cartas_list


# ALTERNATIVA b)

import random


def embaralha(cartas_list: list):
    num_aleatorio_aux_list = []
    i = 0
    while True:
        num_aleatorio = random.randint(0, 51)
        if num_aleatorio in num_aleatorio_aux_list:
            continue

        num_aleatorio_aux_list.append(num_aleatorio)

        carta_temporaria = cartas_list[i]
        cartas_list[i] = cartas_list[num_aleatorio]
        cartas_list[num_aleatorio] = carta_temporaria

        i += 1

        if len(num_aleatorio_aux_list) == 52:
            break


# ------------------------ TESTES --------------------------------------

def main():
    print("QUESTÃO 1:")
    print("Nota-conceito A equivale a", concept_to_num_grade("A"))
    print("Nota-conceito C+ equivale a", concept_to_num_grade("C+"))
    print("Nota-conceito F equivale a", concept_to_num_grade("F"))
    print()
    print("QUESTÃO 2:")
    print("Média entre as nota informadas:", calculate_concept_grades(concept_grades_input_to_list()))
    print()
    print("QUESTÃO 3:")
    print("Primeiro número primo após o número informado:", return_first_prime_num(input_to_int()))
    print()
    print("QUESTÃO 4, ALTERNATIVA a):")
    baralho = criaBaralho()
    print("Baralho original:", baralho)
    # print(baralho)
    print()
    print("QUESTÃO 4, ALTERNATIVA b):")
    embaralha(baralho)
    print("Baralho embaralhado:", baralho)
    # print(baralho)

if __name__ == "__main__":
    main()