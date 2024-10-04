class calculator:
    """
    Utility class.

    You don't need to instanciate this class in order to use it.

    Usage :
        `calculator.method([], [])`
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is:", sum(map(lambda x, y: x * y, V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print("Add vector is:", list(map(lambda x, y: float(x + y), V1, V2)))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print("Sous vector is:", list(map(lambda x, y: float(x - y), V1, V2)))


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == ("__main__"):
    main()
