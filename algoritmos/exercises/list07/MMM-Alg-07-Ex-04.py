def str_to_morse(str: str):
    morse_dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',  'E': '.',      'F': '..-.', 
        'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..', 
        'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.', 
        'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-', 
        'Y': '-.--',  'Z': '--..',  '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    result_list = []

    for char in str:
        char_upper = char.upper()
        if char_upper in morse_dict:
            result_list.append(morse_dict[char_upper])

    list_to_str = ' '.join(result_list)
    return list_to_str


def main():
    str = 'Hello, World!'
    print(str_to_morse(str))

if __name__ == "__main__":
    main()