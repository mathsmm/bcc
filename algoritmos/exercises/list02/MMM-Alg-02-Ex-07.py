n = int(input("Digite um número de 3 algarismos: "))
c = n // 100
d = (n % 100) // 10
u = n % 10

print(f"A centena é: {c}")
print(f"A dezena é: {d}")
print(f"A unidade é: {u}")