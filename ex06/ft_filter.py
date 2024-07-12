def ft_filter(function, itterable):
    """ft_filter(function or None, iterable) --> filter object


    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that
    are true. """

    filtered = (elem for elem in itterable if function(elem) is True)
    return filtered


# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'


# def test():

#     #           Numbers         #

#     def x(): return lambda elem: elem % 2 == 0

#     print(bcolors.OKGREEN + "My filter:" + bcolors.ENDC, list(ft_filter(x(),
# [10, 11, 12, 13.1, 42.00000])))
    # print(bcolors.WARNING + "filter():" + bcolors.ENDC, list(filter(x(), [10,
# 11, 12, 13.1, 42.00000])), "\n")

#     #           Set             #

#     def x(): return lambda elem: 'a' in elem
#     print(bcolors.OKGREEN + "My filter:" + bcolors.ENDC, list(ft_filter(x(),
# {"banana", "cucumber", 'apple', 'peer'})))
#     print(bcolors.WARNING + "filter():" + bcolors.ENDC, list(filter(x(),
# {"banana", "cucumber", 'apple', 'peer'})), "\n")

#     #           Tuple           #

#     def x(): return lambda elem: any(char.isdigit() for char in elem)
#     print(bcolors.OKGREEN + "My filter:" + bcolors.ENDC,
#     list(ft_filter(x(), ("banana", "cucumber06", 'apple', '42peer'))))
#     print(bcolors.WARNING + "filter():" +
# bcolors.ENDC, list(filter(x(), ("banana", "cucumber06",
# 'apple', '42peer'))), "\n")

#     #           String          #

#     def x(): return lambda elem: elem == 'Z'
#     print(bcolors.OKGREEN + "My filter:" + bcolors.ENDC, list(ft_filter(x(),
#     "Zinedine Zidane")))
    # print(bcolors.WARNING + "filter():" + bcolors.ENDC,
# list(filter(x(), "Zinedine Zidane"))), "\n"


# if __name__ == "__main__":
#     test()
