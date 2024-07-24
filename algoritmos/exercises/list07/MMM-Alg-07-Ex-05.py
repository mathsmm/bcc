def is_anagram(word1: str, word2: str):
    dict_word1 = {}
    dict_word2 = {}

    for char in word1.upper():
        if char in dict_word1:
            dict_word1[char] += 1
        else:
            dict_word1[char] = 1

    for char in word2.upper():
        if char in dict_word2:
            dict_word2[char] += 1
        else:
            dict_word2[char] = 1

    if dict_word1 == dict_word2:
        return True
    else:
        return False


def main():
    word1 = 'amor'
    word2 = 'roma'
    print(is_anagram(word1, word2))

if __name__ == "__main__":
    main()