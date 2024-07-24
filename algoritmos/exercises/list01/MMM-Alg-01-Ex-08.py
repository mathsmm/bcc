peso_bugiganga = 75
peso_quinquilharia = 112

qtd_bugigangas = int(input("Informe a quantidade de bugigangas: "))
qtd_quinquilharias = int(input("Informe a quantidade de quinquilharias: "))

peso_total = (qtd_bugigangas * peso_bugiganga) + (qtd_quinquilharias * peso_quinquilharia)

print(f"O peso total é {peso_total}g, {peso_total / 1000}kg")