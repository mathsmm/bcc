def run_length_code(list: list):
    result = []
    i = 1
    j = 1
    while i < len(list):
        if list[i - 1] == list[i]:
            j += 1
        else:
            result.append(list[i - 1])
            result.append(j)
            j = 1
        i += 1
    else:
        result.append(list[i - 1])
        result.append(j)

    return result

# Incompleto!
def rec_run_length_code(list: list):
    if len(list) == 0:
        return []
    if len(list) == 1:
        return [list[0], 1]
    if list[0] == list[1]:
        return 
    return 


def main():
    list = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
    # print(run_length_code(list))
    print(rec_run_length_code(list))

if __name__ == "__main__":
    main()