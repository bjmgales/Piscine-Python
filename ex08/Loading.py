from time import sleep


def ft_tqdm(lst: range):
    toto = 0
    modulo = (lst.stop / 100)
    for i in lst:
        if (i % modulo) == 0:
            toto += 1
            print(str(toto) + "%|" + ("=" * toto) + (" " * (100 - toto)) + "|", end="\r", flush=True)
        yield toto


def main():

    for elem in ft_tqdm(range(100)):
        sleep(1)


if __name__ == "__main__":
    main()
