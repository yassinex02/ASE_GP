#%%
import pandas as pd
from src.functions import get_nof_squirrels_bycolors, plot_white_squirrels, get_squirrels_by_area


def plot():
    df = pd.read_csv('data/dataset.csv', encoding='ISO-8859-1')
    get_nof_squirrels_bycolors(df)
    plot_white_squirrels(df)
    get_squirrels_by_area(df)


if __name__ == "__main__":
    plot()

# %%
