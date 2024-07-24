import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

discriminante = b ** 2 - 4 * a * c

msg_retorno = ""

if discriminante < 0:
    msg_retorno = "Não existem raízes reais"
elif discriminante == 0:
    raiz = -b / (2 * a)
    msg_retorno = "Existe apenas uma raiz real: " + str(raiz)
else:
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    msg_retorno = "Existem duas raízes reais: " + str(raiz1) + " e " + str(raiz2)

print(msg_retorno)