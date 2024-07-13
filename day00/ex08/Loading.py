# from time import sleep
# from tqdm import tqdm

def ft_tqdm(lst: range) -> None:
    """ft_tqdm(itterable) ->None

    This function emulates the behavior of the original tqdm without using any
    libraries.

    Decorate an iterable object, returning an iterator which acts
    exactly like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested. """
    percent = 0
    for i in range(lst.stop + 1):
        print("\r" + str(percent) + "%|" + ("█" * percent) +
              (" " * (100 - percent)) + f'| {i}/{lst.stop}',
              end="", flush=True)
        percent = round((100 * i) / (lst.stop - 1))
        yield


#       Test        #

# def main():
#         print(tqdm.__doc__)
#     for elem in ft_tqdm(range(2322)):
#         sleep(0.01)
#     print()
#     for elem in tqdm(range(2322)):
#         sleep(0.1)


# if __name__ == "__main__":
#     main()
