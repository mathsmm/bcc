vlr_suco = float(input("Informe o preço do suco, em reais: "))
vlr_prato_principal = float(input("Informe o preço do prato principal, em reais: "))
vlr_sobremesa = float(input("Informe o preço da sobremesa, em reais: "))

vlr_conta = (vlr_suco + vlr_prato_principal + vlr_sobremesa) * 1.10

print(f"Valor da conta: R${vlr_conta:.2f}")