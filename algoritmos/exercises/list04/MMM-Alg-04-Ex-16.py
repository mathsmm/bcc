import random


int_n_simulacoes = int(input("Digite o número de simulações desejado: "))

int_qtd_total_sorteios = 0
i = 0
while i < int_n_simulacoes:
    str_sequencia = ""
    int_sorteios = 1
    while True:
        int_aleatorio = random.randint(1, 2)
        if int_aleatorio == 1:
            str_sequencia += "A "
        else:
            str_sequencia += "O "

        if "A A A" in str_sequencia or "O O O" in str_sequencia:
            break
        else:
            int_sorteios += 1
    print(str_sequencia, f"({int_sorteios} sorteios)")
    int_qtd_total_sorteios += int_sorteios
    i += 1
else:
    float_media_sorteios = int_qtd_total_sorteios / int_n_simulacoes
    print(f"Em média, foram necessários: {float_media_sorteios} sorteios para se ter uma sequência de 3 Caras ou 3 Coroas.")
