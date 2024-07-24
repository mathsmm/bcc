qtd_termos_precisao = 0
while qtd_termos_precisao < 15:
    
    pi_acumulado = 3
    i = 1
    while i <= qtd_termos_precisao:
        denominador = 1
        j = i * 2
        j_aux = j
        while j <= j_aux + 2:
            denominador *= j
            j += 1
        if i % 2 == 1:
            pi_acumulado += 4 / denominador
        else:
            pi_acumulado -= 4 / denominador
        i += 1

    print(f"Pi com {qtd_termos_precisao} termos de precisão: {pi_acumulado}")
    qtd_termos_precisao += 1