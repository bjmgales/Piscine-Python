from matplotlib import pyplot as plt
from load_csv import load


def show_income_life_graph(income_path: str, life_path: str):
    income_df = load(income_path)
    life_df = load(life_path)
    plt.title("1900")
    x_gdp = income_df["1900"]
    y_life_exp = life_df["1900"]
    print(life_df["country"].values)
    plt.xlim(300, 10000)
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life expectancy')
    plt.plot(x_gdp, y_life_exp, marker='.', markersize=10, linestyle='')
    plt.show()


def main():
    show_income_life_graph("./ex03/income_per_person_gdpper"
                           "capita_ppp_inflation_adjusted.csv",
                           "./ex03/life_expectancy_years.csv")


if __name__ == "__main__":
    main()
