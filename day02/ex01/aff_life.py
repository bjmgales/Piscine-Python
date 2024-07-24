from matplotlib import pyplot as plt
from load_csv import load


def aff_life(path: str):

    dataset = load(path)
    if dataset is None:
        return None
    france = dataset.loc[dataset["country"] == "France"]
    x = [int(year) for year in dataset.columns.to_list()[1:]]
    y = france.drop(columns=['country']).values.flatten()

    plt.title("France life expectancy Projections")
    plt.xlabel('Years'), plt.ylabel('Life expectancy')
    plt.xticks(range(min(x), max(x), 40))

    plt.plot(x, y)
    plt.show()


def main():
    aff_life("./ex01/life_expectancy_years.csv")


if __name__ == "__main__":
    main()
