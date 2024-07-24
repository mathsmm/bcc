import itertools

l = range(123)

result = itertools.combinations(l, 2)

i = 0
for r in result:
    i += 1
print(i)

def get_pairs_len(body_list_length: int):
    s = 0
    for i in range(body_list_length):
        s += i
    return s

def get_pairs_len_m(body_list_length: int):
    return int((body_list_length**2 - body_list_length) / 2)

print(get_pairs_len(len(l)))
print(get_pairs_len_m(len(l)))