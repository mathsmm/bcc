def is_anagram(word1: str, word2: str):
    word1 = word1.replace(' ', '').upper()
    word2 = word2.replace(' ', '').upper()

    dict_word1 = {}
    dict_word2 = {}

    for char in word1:
        ord_char = ord(char)
        if ord_char >= 65 and ord_char <= 90:
            if char in dict_word1:
                dict_word1[char] += 1
            else:
                dict_word1[char] = 1

    for char in word2:
        ord_char = ord(char)
        if ord_char >= 65 and ord_char <= 90:
            if char in dict_word2:
                dict_word2[char] += 1
            else:
                dict_word2[char] = 1

    if dict_word1 == dict_word2:
        return True
    else:
        return False


def main():
    word1 = 'William Shakespeare!'
    word2 = 'I am a weakish speller'
    print(is_anagram(word1, word2))


if __name__ == "__main__":
    main()