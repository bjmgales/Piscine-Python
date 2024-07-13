import sys
from ft_filter import ft_filter


def main():
    """main() : await 2 arguments from command line:\n
    arg[1] must be an alphanumeric string,
    arg[2] must be a number.
    Once values are parsed, arg[1] is split into words and
    sent to ft_filter(arg[1], arg[2]) that will return words >= arg[2]"""

    main_err = "the arguments are bad"
    arg_len = len(sys.argv)

    try:
        if arg_len != 3:
            raise AssertionError
        goal_len = int(sys.argv[2])
        words = sys.argv[1].split()
        for word in words:
            for c in word:
                if c.isalnum() is False:
                    raise ValueError
        print(list(ft_filter(lambda elem: len(elem) >= goal_len, words)))

    except (AssertionError, ValueError):
        print("AssertionError:", main_err)
        return


if __name__ == "__main__":
    main()
