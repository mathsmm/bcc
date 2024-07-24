vlr_prod_arr = [4.95, 9.95, 14.95, 19.95, 24.95]

i = 0
while i < len(vlr_prod_arr):
    vlr_descontado = vlr_prod_arr[i] * 0.6
    vlr_prod_com_desconto = vlr_prod_arr[i] - vlr_descontado
    print(f"Valor original do produto {i + 1}: R$ {vlr_prod_arr[i]:.02f}", "\t|", end="   ")
    print(f"Valor do desconto de 60%: R$ {vlr_descontado:.02f}", "\t|", end="   ")
    print(f"Valor do produto com desconto: R$ {vlr_prod_com_desconto:.02f}")

    i += 1