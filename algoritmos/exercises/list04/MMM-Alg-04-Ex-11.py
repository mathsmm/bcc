frase = input("Digite uma frase. Será verificado se ela é um palíndromo: ")

frase = frase.lower()

simb_pontuacao = '''!()-[]{};:'"\,<>./?@#$%^&*_~`´ '''
letras_com_acento = [['á','à','ã','â','ä'], ['é','è','ê','ë'], ['í','ì','î','ï'], ['ó','ò','õ','ô','ö'], ['ú','ù','û','ü'], ['ç']]
letras_sem_acento = ['a', 'e', 'i', 'o', 'u', 'c']

i = 0
while i < len(letras_com_acento):
    j = 0
    while j < len(letras_com_acento[i]):
        frase = frase.replace(letras_com_acento[i][j], letras_sem_acento[i])
        j += 1
    i += 1

for caractere in simb_pontuacao:
    frase = frase.replace(caractere, "")

frase_ao_contrario = ""
i = 1
while i <= len(frase):
    frase_ao_contrario += frase[-i]
    i += 1
else:
    if frase_ao_contrario == frase:
        print("A frase é um palíndromo!")
    else:
        print("A frase não é um palíndromo!")