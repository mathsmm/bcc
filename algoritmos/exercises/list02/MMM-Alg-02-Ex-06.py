numeroInformado = int(input("Digite um número de 4 dígitos: "))
unidadeMilhar = numeroInformado // 1000
numeroInformado = numeroInformado % 1000
unidadeCentena = numeroInformado // 100
numeroInformado = numeroInformado % 100
unidadeDezena = numeroInformado // 10
numeroInformado = numeroInformado % 10

print(f"A soma dos dígitos é: {unidadeMilhar + unidadeCentena + unidadeDezena + numeroInformado}")