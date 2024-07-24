n = int(input("Digite um número de 3 algarismos: "))
u = n % 10
d = (n % 100) // 10
c = n // 100

m = u * 100 + d * 10 + c
print(f"N={n:03d} -> M={m:03d}")
