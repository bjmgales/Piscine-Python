import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice and returns the provided list \
        into the new shape ``lst[start:end]``."""
    try:
        if not isinstance(start, int) or not isinstance(end, int)\
                or not isinstance(family, list):
            raise ValueError("expecting => family: list, start: int, end: int")
        elif family == []:
            raise ValueError("family parameter must not be empty")
        elif any(type(f) is not type(family[0]) for f in family):
            raise ValueError("Family list must be "
                             "composed of member from the same type")
        a = np.array(family)
        print("My shape is:", a.shape)
        a = (a[start:end])
        print("My new shape is:", a.shape)
        return a.tolist()
    except ValueError as msg:
        print("ValueError:", msg)
        return None


# def main():

#     # Subject Tests #

#     family = [[1.80, 78.4],
#               [2.15, 102.7],
#               [2.10, 98.5],
#               [1.88, 75.2]]

#     print(slice_me(family, 0, 2))
#     print("toto", slice_me(family, 1, -2))

#     # Error cases #

#     family = []
#     slice_me(family, 0, 2)
#     family = ["toto", 1]
#     slice_me(family, 0, 2)
#     slice_me(None, 0, 2)
#     slice_me([0, 1], 0, "toto")


# if __name__ == "__main__":
#     main()
