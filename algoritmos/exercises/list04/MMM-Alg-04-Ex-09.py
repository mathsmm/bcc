x = float(input("Informe o valor de x: "))
raiz = x / 2

while ((raiz * raiz) - x) > (10**-12) or ((raiz * raiz) - x) < -(10**-12):
    raiz = (raiz + (x / raiz)) / 2

print("A raiz de x é aproximadamente ", raiz)
