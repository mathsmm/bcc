import math

a = int(input("Digite o valor, em números inteiros, de a: "))
b = int(input("Digite o valor, em números inteiros, de b: "))

soma = a + b
diferenca = a - b
produto = a * b
quociente = a // b
resto = a % b
logaritmo = math.log(a, 10)
exponenciacao = a ** b

print("A soma de a e b é:", soma)
print("A diferença de a e b é:", diferenca)
print("O produto de a e b é:", produto)
print("O quociente de a e b é:", quociente)
print("O resto da divisão de a e b é:", resto)
print("O logaritmo de a é:", logaritmo)
print("A exponenciação de a elevado a b é:", exponenciacao)