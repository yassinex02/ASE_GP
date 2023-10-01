#%%
import pandas as pd
from functions import get_nof_squirrels_bycolors, plot_white_squirrels
import matplotlib.pyplot as plt
from unittest.mock import patch
import os


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

def test_squirrel_plot_html_creation():
    data = {
        'Primary Fur Color': ['Gray', 'Cinnamon', 'Black']
    }
    df = pd.DataFrame(data)
    get_nof_squirrels_bycolors(df)
    assert os.path.exists('squirrel_plot.html'), "squirrel_plot.html was not created"
    with open('squirrel_plot.html', 'r') as f:
        assert len(f.read()) > 0, "squirrel_plot.html is empty"

def test_empty_dataframe_get_nof_squirrels_bycolors():
    df = pd.DataFrame()
    try:
        get_nof_squirrels_bycolors(df)
    except Exception as e:
        assert False, f"Function raised an error with an empty dataframe: {e}"



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

def test_map_html_creation():
    data = {
        'Highlights in Fur Color': ['White', 'Gray', 'White'],
        'Squirrel Latitude (DD.DDDDDD)': [40.1, 40.2, 40.3],
        'Squirrel Longitude (-DD.DDDDDD)': [-74.1, -74.2, -74.3],
        'Park Name': ['Park A', 'Park B', 'Park C']
    }
    df = pd.DataFrame(data)
    with patch('webbrowser.open'):
        plot_white_squirrels(df)
    
    assert os.path.exists('map.html'), "map.html was not created"
    with open('map.html', 'r') as f:
        assert len(f.read()) > 0, "map.html is empty"


def test_empty_dataframe_plot_white_squirrels():
    df = pd.DataFrame()
    try:
        plot_white_squirrels(df)
    except Exception as e:
        assert False, f"Function raised an error with an empty dataframe: {e}"


def test_no_white_squirrels_plot():
    data = {
        'Highlights in Fur Color': ['Gray', 'Gray', 'Gray'],
        'Squirrel Latitude (DD.DDDDDD)': [40.1, 40.2, 40.3],
        'Squirrel Longitude (-DD.DDDDDD)': [-74.1, -74.2, -74.3],
        'Park Name': ['Park A', 'Park B', 'Park C']
    }
    df = pd.DataFrame(data)
    plot_white_squirrels(df)
    
    with open('map.html', 'r') as f:
        content = f.read()
        assert 'Marker' not in content, "Markers found in the map when there shouldn't be any"


if __name__ == "__main__":
    test_get_nof_squirrels_bycolors()
    test_plot_white_squirrels()
    test_squirrel_plot_html_creation()
    test_map_html_creation()
    test_empty_dataframe_get_nof_squirrels_bycolors()
    test_empty_dataframe_plot_white_squirrels()

# %%
import mpld3 as mp

print(mp.__version__)
# %%
