import random as rd


def create_bingo_list():
    bingo_range_dict = {
        "B": [1, 15],
        "I": [16,30],
        "N": [31,45],
        "G": [46,60],
        "O": [61,75] 
    }

    bingo_result_dict = {"B": [], "I": [], "N": [], "G": [], "O": []}

    for key in bingo_result_dict:
        aux_set = set()
        while True:
            random = rd.randint(bingo_range_dict[key][0], bingo_range_dict[key][1])
            if random not in aux_set:
                aux_set.add(random)
                bingo_result_dict[key].append(random)
                if len(bingo_result_dict[key]) == 5:
                    bingo_result_dict[key].sort()
                    break

    return bingo_result_dict

def format_bingo_dict_to_str(bingo_dict: dict):
    result = ""
    for key in bingo_dict:
        result += f"{key}\t"
    else:
        result += "\n"

    i = 0
    while i < 5:
        for key in bingo_dict:
            result += f"{bingo_dict[key][i]}\t"
        result += "\n"
        i += 1

    return result


def main():
    bingo_dict = create_bingo_list()
    print(format_bingo_dict_to_str(bingo_dict))

if __name__ == "__main__":
    main()