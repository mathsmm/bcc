nmatricula = int(input("Digite o número de matrícula: "))

ano = nmatricula // 10000
semestre = (nmatricula % 10000) // 1000

print(f"O aluno foi matriculado no ano {ano} e no semestre {semestre}")