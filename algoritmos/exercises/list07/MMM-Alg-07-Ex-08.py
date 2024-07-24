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

def verify_bingo_dict(bingo_dict: dict):
    i = 0
    # Verify columns
    while i < 5:
        sum = 0
        for key in bingo_dict:
            sum += bingo_dict[key][i]
        if sum == 0:
            return True
        i += 1

    # Verify rows
    for key in bingo_dict:
        sum = 0
        for value in bingo_dict[key]:
            sum += value
        if sum == 0:
            return True

    #Verify diagonals
    sum1 = 0
    sum2 = 0
    i = 0
    j = 4
    for key in bingo_dict:
        sum1 += bingo_dict[key][i]
        sum2 += bingo_dict[key][j]
        i += 1
        j -= 1
    if sum1 == 0 or sum2 == 0:
        return True

    return False


def main():
    # bingo_dict = create_bingo_list()
    # print(format_bingo_dict_to_str(bingo_dict))

    bingo_dict1 = {
        "B": [0,0,0,0,0],
        "I": [16,17,18,19,30],
        "N": [31,32,33,34,45],
        "G": [46,47,48,49,60],
        "O": [61,62,63,64,75]
    }

    bingo_dict2 = {
        "B": [0,2,3,4,5],
        "I": [0,17,18,19,30],
        "N": [0,32,33,34,45],
        "G": [0,47,48,49,60],
        "O": [0,62,63,64,75]
    }

    bingo_dict3 = {
        "B": [0,2,3,4,5],
        "I": [16,0,18,19,30],
        "N": [41,32,0,34,45],
        "G": [46,47,48,0,60],
        "O": [61,62,63,64,0]
    }

    bingo_dict4 = {
        "B": [1,2,3,4,0],
        "I": [16,17,18,0,30],
        "N": [31,32,0,34,45],
        "G": [46,0,48,49,60],
        "O": [0,62,63,64,65]
    }

    bingo_dict5 = {
        "B": [1,2,3,4,0],
        "I": [16,0,18,19,30],
        "N": [31,32,0,34,45],
        "G": [0,0,48,0,60],
        "O": [0,0,63,64,75]
    }

    print(verify_bingo_dict(bingo_dict1))
    print(verify_bingo_dict(bingo_dict2))
    print(verify_bingo_dict(bingo_dict3))
    print(verify_bingo_dict(bingo_dict4))
    print(verify_bingo_dict(bingo_dict5))

if __name__ == "__main__":
    main()