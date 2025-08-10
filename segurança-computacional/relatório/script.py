import pypxlib

table_1 = pypxlib.Table("tabelas-cifradas\\TFUNCAUX.DB", encoding="cp1252", px_encoding="cp1252")

def preenche_esquerda(s: str, tamanho: int, preenchimento: str):
        return (preenchimento * (tamanho - len(s))) + s

def uncrypt_CEP(idx):
    s = ''
    i = 1 # ignora primeiro byte
    # print(len(table_1[idx].bdCEP))
    byte_b = bytearray()
    ints_b = []
    byte_b.append(table_1[idx].bdCEP[0])
    ints_b.append(table_1[idx].bdCEP[0])
    while i < len(table_1[idx].bdCEP):
        s = preenche_esquerda(bin(table_1[idx].bdCEP[i])[2:], 8, '0')[::-1] + s
        byte_b.append(table_1[idx].bdCEP[i])
        ints_b.append(table_1[idx].bdCEP[i])
        i += 1
    bits_extras = len(table_1[idx].bdCEP) - 8
    msg = ''
    byte_a = bytearray()
    ints_a = []
    while s != '':
        byte = int(s[:7], base=2)
        byte_a.append(byte)
        ints_a.append(byte)
        if bits_extras > 0:
            bits_extras -= 1
            s = s[8:]
        else:
            s = s[7:]
        msg = msg + chr(byte)
    print("ORIGINAL:", byte_b.decode(encoding="cp1252", errors="replace"))
    print("ORIGINAL:", ints_b)
    print("ORIGINAL:", byte_b.hex())
    # print("DECIFRADO:", msg)
    # print("DECIFRADO:", byte_a.decode(encoding="cp1252"))
    # print("DECIFRADO:", ints_a)

def uncrypt_ENDERECO(idx):
    s = ''
    i = 1 # ignora primeiro byte
    # print(len(table_1[idx].bdENDERECO))
    byte_b = bytearray()
    ints_b = []
    byte_b.append(table_1[idx].bdENDERECO[0])
    ints_b.append(table_1[idx].bdENDERECO[0])
    while i < len(table_1[idx].bdENDERECO):
        s = preenche_esquerda(bin(table_1[idx].bdENDERECO[i])[2:], 8, '0')[::-1] + s
        byte_b.append(table_1[idx].bdENDERECO[i])
        ints_b.append(table_1[idx].bdENDERECO[i])
        i += 1
    bits_extras = len(table_1[idx].bdENDERECO) - 8
    print(s)
    msg = ''
    byte_a = bytearray()
    ints_a = []
    while s != '':
        byte = int(s[:7], base=2)
        byte_a.append(byte)
        ints_a.append(byte)
        if bits_extras > 0:
            bits_extras -= 1
            s = s[8:]
        else:
            s = s[7:]
        msg = msg + chr(byte)
    print("ORIGINAL:", byte_b.decode(encoding="cp1252", errors="replace"))
    print("ORIGINAL:", ints_b)
    print("ORIGINAL:", byte_b.hex())
    print("DECIFRADO:", msg)
    # print("DECIFRADO:", byte_a.decode(encoding="cp1252"))
    # print("DECIFRADO:", ints_a)

def print_bin_bdCEP(idx):
    s = ''
    for byte in table_1[idx].bdCEP:
        print(preenche_esquerda(bin(byte)[2:], 8, '0'), end=" ")
        # s = preenche_esquerda(bin(byte)[2:], 8, '0')[::-1] + ' ' + s
    # print(s)
    print()

# uncrypt_CEP(0)
uncrypt_ENDERECO(0)
# print_bin_bdCEP(0)