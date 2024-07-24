def simetric_difference(M: set, N: set):
    aux_set1 = M.difference(N)
    aux_set2 = N.difference(M)
    aux_set3 = aux_set1.union(aux_set2)

    aux_list = list(aux_set3)
    aux_list.sort()
    return aux_list


def main():
    set1 = {2,4,5,9}
    set2 = {2,4,11,12}
    print(simetric_difference(set1, set2))

if __name__ == "__main__":
    main()

