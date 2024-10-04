def is_valid(vargs) -> bool:
    """Checks if the requested operation is valid."""
    valid = ["mean", "median", "quartile", "std", "var"]

    for v in vargs:
        if any(v == val for val in valid):
            return True
        else:
            return False


def float_check(num):
    """Checks if the operation resulted in a float number. If so, returns the\
          float number, otherwise, removes the remaining \".0\""""
    return int(num) if num % 1 == 0 else num


def mean(nums):
    """Returns the mean of the number list."""
    return float_check(sum(nums) / len(nums))


def median(nums):
    """Returns the median of the number list."""
    nums = sorted(nums)
    med_len = int(len(nums) / 2)
    if (len(nums) % 2) != 0:
        return nums[med_len]
    else:
        return mean([nums[med_len], nums[med_len - 1]])


def quartile(nums):
    """Returns the quartile of the number list."""
    nums = sorted(nums)
    med_len = int(len(nums) / 2)
    if len(nums) % 2 == 0:
        med = median(nums)
    else:
        med = (nums[med_len + 1] - nums[med_len]) / 2
        nums.insert(nums[med_len], med)
    i = int(len(nums) / 2)
    Q25 = median(nums[:i])
    Q75 = median(nums[i:])
    return [float(Q25), float(Q75)]


def var(nums):
    """Returns the variance of the number list."""
    m = mean(nums)
    return float(sum([(m - elem) ** 2 for elem in nums]) / (len(nums) - 1))


def std(nums):
    """Returns the standard deviation of the number list."""
    return float(var(nums) ** 0.5)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Checks for the parameters validity and calls the right function\
         depending on the requested operation."""
    functions = {
        'mean': mean,
        'median': median,
        'quartile': quartile,
        'std': std,
        'var': var
    }
    try:
        assert all(isinstance(a, int) for a in args), "ERROR"
        assert all(isinstance(value, str) for key, value in kwargs.items()), \
            "ERROR"
        param = [value for key, value in kwargs.items()]
        if is_valid(param) is False:
            return None
        for p in param:
            if args:
                print(p + ":", f"{functions[p](args)}")
            else:
                print("ERROR")

    except Exception as e:
        print(e)
        return None


def main():
    """Main function for statistics.py"""
    # ft_statistics(0, 0, 0, 0, toto="mean", tutu="median", tata="quartile")
    ft_statistics(1, 2, 3, 4, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == ("__main__"):
    main()
