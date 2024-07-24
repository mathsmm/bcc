palavra = input('Digite uma palavra. Será verificado se ela é um palíndromo: ')

palavra_ao_contrario = ""
i = 1
while i <= len(palavra):
    palavra_ao_contrario += palavra[-i]
    i += 1
else:
    if palavra_ao_contrario == palavra:
        print("A palavra é um palíndromo!")
    else:
        print("A palavra não é um palíndromo!")