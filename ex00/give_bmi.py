def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """Calculates and returns bmi list \
        for each entries of weight and height."""
    if not height or not weight:
        raise ValueError("Error: parameters cannot be empty.")
    if not isinstance(weight, list) or not isinstance(height, list)\
            or not all(isinstance(w, (int, float)) for w in weight)\
            or not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Error: parameters must be of list[int|float] type.")
    if len(height) != len(weight):
        raise ValueError("Error: weight & height must \
have equal number of elements")

    ret_lst = []
    for i in range(len(height)):
        ret_lst.append(weight[i] / (height[i] * height[i]))
    return ret_lst


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of boolean. True if the provided bmi is superior\
         to the provided limit. False otherwise."""

    if not bmi:
        raise ValueError("Error:bmi parameter must not be empty")
    if not isinstance(bmi, list) or\
            not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("Error:bmi parameter must be of list[int|float] type")
    if type(limit) is not int:
        raise TypeError("Error:limit parameter must be of type int")
    ret_lst = []
    for element in bmi:
        if element > limit:
            ret_lst.append(True)
        else:
            ret_lst.append(False)
    return ret_lst


def main():
    try:
        height = [10, 1]
        weight = [35, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, "toto"))
    except (TypeError, ValueError) as msg:
        print(msg)
        return


if __name__ == "__main__":
    main()
