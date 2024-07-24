# from xmlrpc.client import Boolean
from emb import *

# def salvarEmb(bits,file):
#     bytesArray = bytearray()
#     bits = desembaralhar(bits)
#     quadro = ''
#     for i in bits:
#         quadro += i
#         if len(quadro) == 8:
#             bytesArray.append(int(dados[:8],2))
#     file.write(bytesArray)


def retornar_quadro_bit_flipado(quadro, posicao):
    """
    Recebe um quadro de Hamming estendido e retorna uma lista igual ao quadro, porém com o bit na posição especificada flipado
    """
    result = list(quadro)
    if quadro[posicao] == '1':
        result[posicao] = '0'
    else:
        result[posicao] = '1'

    return result

def decodificar_quadro(quadro):
    """
    Recebe um quadro de Hamming estendido (16 bits) e retorna:

    * Os bits de dados em string e False se o algoritmo não detectar erro;\n
    * String vazia e False se o algoritmo detectar erro mas não determinar sua posição;\n
    * Os bits de dados em string já corrigidos e True se o algoritmo detectar erro e determinar sua posição.

    - O segundo retorno é do tipo booleano e recebe True se o algoritmo efetuar a correção do quadro.

    LIMITAÇÃO: Se o algoritmo determinar a posição do erro e houver um número ímpar de erros diferente de 1, ele retornará os bits de dados corrigidos por uma suposta posição de erro. Desta forma, ele retorna os bits de dados corrigidos de uma maneira não acertiva!
    """
    posicoes_bits_dados = [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]
    bits_dados = []
    soma_primeiro_bit = int(quadro[0])
    posicao_erro = 0

    # Para o próximo laço, não é considerada a posição do primeiro bit do quadro
    for i in range(1, 16):
        # Pula as posições de bits de paridade
        if i in posicoes_bits_dados:
            bits_dados.append(quadro[i])

        # Se o bit na posição i estiver ligado, então:
            # Soma o bit de dado i para posteriormente verificar a paridade do bit da posição 0 do quadro de Hamming estendido;
            # Aplica-se XOR à variável posicao_erro e à posição i do bit ligado.
        # Ao final do laço, a variável posicao_erro terá exatamente a posição do erro detectado em decimal
        if int(quadro[i]):
            soma_primeiro_bit += 1
            posicao_erro = posicao_erro ^ i

    # Se a soma de todos os bits ligados for par, quadro_eh_par recebe True. Caso contrário, quadro_eh_par recebe False
    quadro_eh_par = True if soma_primeiro_bit % 2 == 0 else False

    # Se não for detectado erro (posicao_erro = 0), retorna os bits de dados
    if   posicao_erro == 0 and quadro_eh_par:
        return ''.join(bits_dados), False

    # Se for detectado 2 erros, retorna string vazia. Acima de 2, pode não funcionar, pois pode haver um quadro falso positivo com posicao_erro = 0
    elif (posicao_erro != 0 and quadro_eh_par) or (posicao_erro == 0 and not quadro_eh_par):
        return '', False

    # Se for detectado 1 erro, flipa o bit incorreto e retorna os bits de dados
    else:
        bit_dados = []
        quadro_bit_flipado = retornar_quadro_bit_flipado(quadro, posicao_erro)
        for i in posicoes_bits_dados:
            bit_dados.append(quadro_bit_flipado[i])

        return ''.join(bit_dados), True

def ler_cabecalho(t):
    chave = 'bcc2022'
    stringC = ''
    for i in chave:
        b = format(ord(i),'b')
        b = '0' * ( 8 - len(b)) + b
        stringC += b
    cabecalhos = []
    f = ''
    data = ''
    on = False
    for index, i in enumerate(t):
        f += i
        if len(f) > len(stringC):
            f = f[1:]
        if not on:
            data += i
        if f == stringC:
            if not on:
                on = False
                bits = ''
                dados = ''
                for cada in data:
                    bits += cada
                    if len(bits) == 8:
                        dados += chr(int(bits,2))
                        bits = ''
                data = ''
                final = dados[:len(dados) - len(chave)]
                if final != '':
                    cabecalhos.append(final)
            else:
                on = True
    certo = ''
    for ix,x in enumerate(cabecalhos):
        for iy,y in enumerate(cabecalhos):
            if x == y and ix != iy:
                certo = x
    return certo

def decodificar_arquivo(caminho_arquivo_codificado: str, caminho_arquivo_recriado='coded-converted-files\\original'):
    """
    Decodifica um arquivo especificado e recria o arquivo original (antes de ser codificado).

    Se decodificar_quadro detectar um quadro corrompido, decodificar_arquivo adiciona 11 bits desligados na conversão para o arquivo original ao invés dos dados de um quadro corrompido.
    """
    inicio_arquivo = 0
    cabecalho = ''
    with open(caminho_arquivo_codificado, 'rb') as arq_codificado:
        i = 0
        while i <= 375:
            dado = arq_codificado.read(1)
            byte_formatado = format(ord(dado), '08b')
            cabecalho += byte_formatado
            i += 1

    dados_cabecalho = ler_cabecalho(cabecalho).split('-')
    extensao = dados_cabecalho[0]
    tamanho_arquivo = int(dados_cabecalho[1])
    inicio_arquivo = int(dados_cabecalho[2])

    with open(caminho_arquivo_recriado + '.' + extensao, 'wb') as arq_original:
        with open(caminho_arquivo_codificado, 'rb') as arq_codificado:
            contador_tamanho = 0
            byte_formatado = ''
            bytes_formatados = ''
            dados = ''
            efetuou_correcao = False
            contador_quadros_verificados = 0
            contador_quadros_corrigidos = 0
            contador_quadros_corrompidos = 0
            bytesArray = bytearray()
            escrever = False
            quadros = ''
            while True:
                dado = arq_codificado.read(1)
                contador_tamanho += 8
                if tamanho_arquivo <= (contador_tamanho - inicio_arquivo):
                    break
                byte_formatado = format(ord(dado), '08b')
                bytes_formatados += byte_formatado
                if len(bytes_formatados) == inicio_arquivo and not escrever:
                    escrever = True
                    bytes_formatados = ''
                if escrever:
                    if len(bytes_formatados) == 16:
                        quadros += bytes_formatados
                        bytes_formatados = ''

                    # Se a quantidade de quadros for 100:
                    if len(quadros) == 1600:
                        quadros = desembaralhar(quadros)
                        quadro = ''
                        for n in quadros:
                            quadro += n
                            if len(quadro) == 16:
                                novos_dados, efetuou_correcao = decodificar_quadro(quadro)
                                contador_quadros_verificados += 1
                                if novos_dados != '' and not efetuou_correcao:
                                    dados += novos_dados
                                elif novos_dados != '' and efetuou_correcao:
                                    contador_quadros_corrigidos += 1
                                    dados += novos_dados
                                else:
                                    contador_quadros_corrompidos += 1
                                    dados += '00000000000'
                                quadro = ''
                                bytes_formatados = ''
                            if len(dados) >= 8:
                                bytesArray.append(int(dados[:8], 2))
                                dados = dados[8:]
                            if len(bytesArray) >= 16:
                                arq_original.write(bytesArray)
                                bytesArray = bytearray()
                        quadros = ''

            # Se a quantidade de quadros for diferente de 0:
            if quadros != '':
                quadros = desembaralhar(quadros)
                quadro = ''
                for n in quadros:
                    quadro += n
                    if len(quadro) == 16:
                        novos_dados, efetuou_correcao = decodificar_quadro(quadro)
                        contador_quadros_verificados += 1
                        if novos_dados != '' and not efetuou_correcao:
                            dados += novos_dados
                        elif novos_dados != '' and efetuou_correcao:
                            contador_quadros_corrigidos += 1
                            dados += novos_dados
                        else:
                            contador_quadros_corrompidos += 1
                            dados += '00000000000'
                        bytes_formatados = ''
                        quadro = ''
                    if len(dados) >= 8:
                        bytesArray.append(int(dados[:8], 2))
                        dados = dados[8:]
                    if len(bytesArray) >= 16:
                        arq_original.write(bytesArray)
                        bytesArray = bytearray()
                quadros = ''

            if len(dados) != 8:
                contador_tamanho -= len(dados)

            if len(bytes_formatados+dados) != 0:
                bytesArray.append(int(bytes_formatados+dados, 2))
            # bytesArray.append(int(bytes_formatados+dados, base=2).to_bytes(2, byteorder='big'))

            arq_original.write(bytesArray)

    diferenca_tamanho = (contador_tamanho - inicio_arquivo) - tamanho_arquivo
    if diferenca_tamanho != 0:
        print('*Foi detectada uma diferença de', diferenca_tamanho, 'bits ao comparar o tamanho do arquivo codificado armazenado em seu cabeçalho e seu atual tamanho. O arquivo pode estar corrompido')

    print("Quantidade de quadros verificados:", contador_quadros_verificados)
    print("Quantidade de quadros corrompidos:", contador_quadros_corrompidos)
    print("Quantidade de quadros corrigidos:", contador_quadros_corrigidos)


def main():
    # Marca o tempo de execução
    import time
    start_time = time.time()

    print()

    decodificar_arquivo(caminho_arquivo_codificado='files\\codificado.bin', caminho_arquivo_recriado='files\\original')

    print("--- Receiver --> Tempo de execução: %s segundos ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()