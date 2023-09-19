import pandas as pd
from src.functions import get_nof_squirrels_bycolors


def plot():
    df = pd.read_csv('data/dataset.csv', delimiter=';', encoding='ISO-8859-1')
    get_nof_squirrels_bycolors(df)


if __name__ == "__main__":
    plot()
