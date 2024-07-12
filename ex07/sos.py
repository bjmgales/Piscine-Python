import sys


def main():
    """main(): await one argument from command line

    arg[1] must be an alphanumeric string.
    Once arg[1] is parsed, translate
    it's content into morse, then
    outputs the result.
    """

    sys.tracebacklimit = 0
    MORSE_CODE_DICT = {' ':  '/ ', 'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----'}

    assert len(sys.argv) == 2, "the arguments are bad"
    if len(sys.argv[1]) <= 0:
        return
    assert all(c.isalnum() or c == ' '
               for c in sys.argv[1]), "the arguments are bad"

    morse_code = ""
    for i, c in enumerate(sys.argv[1]):
        morse_code += MORSE_CODE_DICT[c.upper()]
        if i == len(sys.argv[1]) - 1:
            break
        morse_code += " "

    print(morse_code)


if __name__ == "__main__":
    main()
