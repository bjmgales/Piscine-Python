import sys


def prompt_user():
    """Prompt user for an input and send it to
    super_char_counter() on receive."""

    sys.stdout.write("What is the text to count?\n")
    line = sys.stdin.read()
    super_chars_counter(line)


def super_chars_counter(str):
    """Count str characters, upper letters, lower letters,
    punctuation marks, spaces and digits"""

    ponct = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f'The text contains {len(str)} characters:')
    print(f'{sum(1 for c in str if c.isupper())} upper letters')
    print(f'{sum(1 for c in str if c.islower())} lower letters')
    print('{0} ponctuation marks'.format(sum(1 for c in str if c in ponct)))
    print(f'{sum(1 for c in str if c.isspace())} spaces')
    print(f'{sum(1 for c in str if c.isdigit())} digits')


def main():
    """If stdout is empty, redirect to prompt_user.
    If stdout has an argument, call super_char_counter().
    Otherwise, display error messages reduced to fit subject prerequisite"""

    sys.tracebacklimit = 0
    arg_len = len(sys.argv)
    assert arg_len <= 2, "more than one argument is provided"
    if arg_len < 2 or sys.argv[1] is None or sys.argv[1] == "":
        prompt_user()
    else:
        super_chars_counter(sys.argv[1])


if __name__ == "__main__":
    main()
