def main():
    try:
        # Abre o arquivo exportado da consulta
        arq = open('A1_b_resultado.csv', 'r')
    except Exception as e:
        print('Não foi possível abrir o arquivo. Erro:', e)
        return

    # Pula a primeira linha
    arq.readline()

    for linha in arq:
        # Armazena algumas informações da consulta
        linha_split = linha.split(',')
        c_id     = linha_split[0]
        pri_nome = linha_split[2]
        ult_nome = linha_split[3]
        email    = linha_split[4]

        # Printa as informações para expor que elas
        # estão contidas no programa
        print(c_id, pri_nome, ult_nome, email)

if __name__ == "__main__":
    main()