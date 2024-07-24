q = int(input("Informe um número decimal: "))
result = ""
while q != 0:
    r = q % 2
    result = str(r) + result
    q = q // 2

print(result)