import matplotlib.pyplot as plt
import folium
import webbrowser
import mpld3


def get_nof_squirrels_bycolors(df):
    fur_color_counts = df['Primary Fur Color'].value_counts()
    plt.figure(figsize=(8, 4))
    fur_color_counts.plot(kind='bar', color='skyblue')
    # plt.title('Number of Squirrels Per Fur Color')
    plt.title('TTESTTTT')
    plt.xlabel('Fur Color')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    html_plot = mpld3.fig_to_html(plt.gcf())
    with open('squirrel_plot.html', 'w') as file:
        file.write(html_plot)


# Map of White Squirrels: Create a map that marks the locations of white squirrels spotted during the census.

def plot_white_squirrels(df):

    white_squirrels = df[df["Highlights in Fur Color"] == "White"]

    m = folium.Map(location=[white_squirrels["Squirrel Latitude (DD.DDDDDD)"].mean(),
                             white_squirrels["Squirrel Longitude (-DD.DDDDDD)"].mean()],
                   zoom_start=13)

    # Add markers for each white squirrel sighting
    for index, row in white_squirrels.iterrows():
        folium.Marker([row["Squirrel Latitude (DD.DDDDDD)"], row["Squirrel Longitude (-DD.DDDDDD)"]],
                      tooltip=row["Park Name"]).add_to(m)

    mapfile = "map.html"
    m.save(mapfile)
    webbrowser.open(mapfile)
    return
