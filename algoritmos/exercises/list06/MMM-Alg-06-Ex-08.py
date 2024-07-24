def sentence_to_word_list(sentence: str):
    sentence = sentence.strip()
    sentence = sentence + " "
    aux_str = ""
    word_list = []

    for char in sentence:
        if   char == "!" or char == "?" or char == "." or char == ":" or char == ";" or char == ",":
            continue
        elif char == " ":
            word_list.append(aux_str)
            aux_str = ""
        else:
            aux_str += char

    return word_list


def main():
    sentence = input("Informe uma frase. O programa separará as palavras desta frase: ")
    print(sentence)
    list = sentence_to_word_list(sentence)
    print(list)

if __name__ == "__main__":
    main()