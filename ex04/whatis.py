import sys

arg_len = len(sys.argv)
sys.tracebacklimit = 0
assert arg_len <= 2, "more than one argument is provided"

if arg_len == 2:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")

    if n % 2 == 0:
        print("I'm Even")
    else:
        print("I'm odd")
