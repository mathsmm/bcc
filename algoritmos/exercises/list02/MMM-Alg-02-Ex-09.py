dataOriginal = int(input("Digite uma data no formato DDMMAA: "))

dias = dataOriginal // 10000
meses = (dataOriginal % 10000) // 100
anos = dataOriginal % 100

print(f"A data original é: {dias:02d}{meses:02d}{anos:02d}")
print(f"A data invertida é: {anos:02d}{meses:02d}{dias:02d}")