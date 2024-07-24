from matplotlib import pyplot as plt
from load_csv import load


def convert_abbr_num(num: str):
    if 'K' in num:
        num = float(num.replace('K', '')) * 1000
    if 'M' in num:
        num = float(num.replace('M', '')) * 1000000
    return int(round(num))


def compare_pop(path: str):

    dataset = load(path)
    france = dataset.loc[dataset["country"] == "France"]
    belgium = dataset.loc[dataset["country"] == "Belgium"]
    france = france.drop(columns=['country']).values.flatten()
    belgium = belgium.drop(columns=['country']).values.flatten()
    x = [int(year) for year in dataset.columns.to_list()[1:]
         if int(year) <= 2050]
    france = [convert_abbr_num(pop) for pop in france[:len(x)]]
    belgium = [convert_abbr_num(pop) for pop in belgium[:len(x)]]
    plt.title("Population Projections")
    plt.xlabel('Years'), plt.ylabel('Life expectancy')
    plt.xticks(range(min(x), 2041, 40))
    plt.yticks(range(20000000, 80000000, 20000000), ["20M", "40M", "60M"])
    plt.plot(x, france, label="France", linestyle='-', color='g')
    plt.plot(x, belgium, label="Belgium", linestyle='-', color='b')
    plt.legend(loc="lower right")
    plt.show()


def main():
    compare_pop("./ex02/population_total.csv")


if __name__ == "__main__":
    main()
