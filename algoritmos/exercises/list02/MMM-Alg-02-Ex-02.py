segundos = int(input("Digite a quantidade de segundos: "))

dia = segundos // 86400
segundos = segundos % 86400
hora = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f"O tempo total, no formato D:HH:MM:SS, é: {dia:}:{hora:02d}:{minutos:02d}:{segundos:02d}")

