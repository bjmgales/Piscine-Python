def callLimit(limit: int):
    try:
        if not isinstance(limit, int):
            raise ValueError("limit parameter must be of int type.")
    except ValueError as e:
        print(type(e).__name__, e)
        return None

    count = 0

    def callLimiter(function):
        nonlocal count

# *args and **kwds are here solely to ensure
# any type of function could be called.

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print("Error:", function, "call too many times")
        return limit_function
    return callLimiter


def main():
    @callLimit(-3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()  # calls "limit_function()"
        g()


if __name__ == "__main__":
    main()
