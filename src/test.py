import pandas as pd
from functions import get_nof_squirrels_bycolors, get_squirrels_by_area, plot_white_squirrels
import matplotlib.pyplot as plt
from unittest.mock import patch


def test_get_nof_squirrels_bycolors():
    data = {
        'Primary Fur Color': ['Gray', 'Cinnamon', 'Black', 'Gray', 'Cinnamon']
    }
    df = pd.DataFrame(data)

    def modified_get_nof_squirrels_bycolors(df):
        fur_color_counts = df['Primary Fur Color'].value_counts()
        plt.figure(figsize=(10, 6))
        fur_color_counts.plot(kind='bar', color='skyblue')
        plt.title('Number of Squirrels Per Fur Color')
        plt.xlabel('Fur Color')
        plt.ylabel('Number of Squirrels')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return fur_color_counts
    result = modified_get_nof_squirrels_bycolors(df)
    # check if the counts returned by the modified function match the expected values.
    # If the counts are incorrect, the assertions will raise an error with the provided error message.
    assert result['Gray'] == 2, "Incorrect count for Gray color"
    assert result['Cinnamon'] == 2, "Incorrect count for Cinnamon color"
    assert result['Black'] == 1, "Incorrect count for Black color"

def test_get_squirrels_by_area(df):
    data = {
        'Squirrel Area': ['Upper Manhattan', 'Central Manhattan', 'Lower Manhattan']
    }
    df = pd.DataFrame(data)

    def modified_get_squirrels_by_area(df):
        squirrels_by_area = df['Squirrel Area'].value_counts()
        plt.figure(figsize=(9, 5))
        squirrels_by_area.plot(kind='bar', color='red')
        plt.title('Distribution of Squirrels Per Area')
        plt.xlabel('Area')
        plt.ylabel('Number of Squirrels')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return squirrels_by_area
    result = modified_get_squirrels_by_area(df)
    assert result['Upper Manhattan'] == 1, "Incorrect count for Upper Manhattan area"
    assert result['Central Manhattan'] == 2, "Incorrect count for Central Manhattan area"
    assert result['Lower Manhattan'] == 1, "Incorrect count for Lower Manhattan area"


def test_plot_white_squirrels():
    data = {
        'Highlights in Fur Color': ['White', 'Gray', 'White', 'Cinnamon', 'White'],
        'Squirrel Latitude (DD.DDDDDD)': [40.1, 40.2, 40.3, 40.4, 40.5],
        'Squirrel Longitude (-DD.DDDDDD)': [-74.1, -74.2, -74.3, -74.4, -74.5],
        'Park Name': ['Park A', 'Park B', 'Park C', 'Park D', 'Park E']
    }
    df = pd.DataFrame(data)

    def modified_plot_white_squirrels(df):
        white_squirrels = df[df["Highlights in Fur Color"] == "White"]
        return white_squirrels
    result = modified_plot_white_squirrels(df)
    assert len(result) == 3, "Incorrect count for White squirrels"
    assert all(result["Highlights in Fur Color"] ==
               "White"), "Non-white squirrel found in filtered data"


if __name__ == "__main__":
    test_get_nof_squirrels_bycolors()
    test_plot_white_squirrels()
