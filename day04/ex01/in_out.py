
def is_num(x: any) -> bool:
    if not isinstance(x, int | float):
        print("ValueError: parameter x must be either int or float")
        return False
    return True


def square(x: int | float) -> int | float:
    return x ** 2 if is_num(x) else None


def pow(x: int | float) -> int | float:
    return x ** x if is_num(x) else None


def outer(x: int | float, function) -> object:
    """"""
    count = 0
    if not is_num(x):
        return outer(0, function)

    def inner() -> float:
        nonlocal count  # allow count to be re-assigned insigned inner scope.
        result = x
        for i in range(count):
            result = function(result)
        count += 1
        return function(result)

    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()