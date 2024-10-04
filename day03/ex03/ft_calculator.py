class calculator:
    def __init__(self, object):
        """
            Initialize a calculator object.

            Parameters:
            `object : ` - The first name of the character. \
    This is a mandatory argument.
        """
        self.values = object

    def __add__(self, object) -> None:
        self.values = [values + object for values in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        self.values = [values * object for values in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        self.values = [values - object for values in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        try:
            if object == 0:
                raise ZeroDivisionError("cannot divide by 0.")
            self.values = [values / object for values in self.values]
            print(self.values)
        except ZeroDivisionError as e:
            print(type(e).__name__ + ":", e)


def main():
    v1 = calculator(("toto", "titi"))
    v1 + " lol"
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 0


if __name__ == ("__main__"):
    main()
