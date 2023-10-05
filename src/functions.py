import matplotlib.pyplot as plt
import folium
import webbrowser
import mpld3
import numpy as np


def get_nof_squirrels_bycolors(df):
    if df.empty:
        print("The provided dataframe is empty. No plot will be generated.")
        return

    fur_color_counts = df['Primary Fur Color'].value_counts()

    # Define a custom color palette for the categories
    color_palette = ['green', 'red',
                     'yellow']  # Add more colors as needed

    plt.figure(figsize=(8, 4))
    fur_color_counts.plot(kind='bar', color=color_palette)
    plt.title('Number of Squirrels Per Fur Color')
    plt.xlabel('Fur Color')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=45)

    # Set the x-axis tick labels to the actual category names
    plt.xticks(range(len(fur_color_counts)), fur_color_counts.index)

    # Create a legend mapping numeric values to category names with colors
    legend_labels = {i: (category, color_palette[i]) for i, category in enumerate(
        fur_color_counts.index)}
    legend_elements = [plt.Line2D([0], [0], color=color_palette[i],
                                  label=f"{legend_labels[i][0]} ({i})", lw=4) for i in range(len(legend_labels))]

    # Add the legend to the plot
    plt.legend(handles=legend_elements, title='Fur Color', loc='upper right')

    plt.tight_layout()

    html_plot = mpld3.fig_to_html(plt.gcf())
    with open('squirrel_plot.html', 'w') as file:
        file.write(html_plot)


# Distribution of Squirrels Per Area: Create a graph that shows the number of squirrels in different areas of NYC.

# Distribution of Squirrels Per Area: Create a graph that shows the number of squirrels in different areas of NYC.


def get_squirrels_by_area(df):
    if df.empty:
        print("The provided dataframe is empty. No plot will be generated.")
        return

    byarea_counts = df['Area Name'].value_counts()
    colour_palette = ['black', 'blue', 'green', 'Yellow']

    plt.figure(figsize=(8, 4))  # Increase figure size for better visualization
    byarea_counts.plot(kind='bar', color=colour_palette)
    plt.title('Distribution of Squirrels Per Area')
    plt.xlabel('Area')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=50)
    plt.xticks(range(len(byarea_counts)), byarea_counts.index)

    labels_legend = {i: (category, colour_palette[i]) for i, category in enumerate(
        byarea_counts.index)}
    elements_legend = [plt.Line2D([0], [0], color=colour_palette[i],
                                  label=f"{labels_legend[i][0]} ({i})", lw=4) for i in range(len(labels_legend))]

    # Place the legend outside the plot on the right
    plt.legend(handles=elements_legend, title='Squirrels By Area',
               loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()
    html_area_plot = mpld3.fig_to_html(plt.gcf())
    with open('graph2.html', 'w') as f:
        f.write(html_area_plot)


# Map of White Squirrels: Create a map that marks the locations of white squirrels spotted during the census.

def plot_white_squirrels(df):
    if df.empty:
        print("The provided dataframe is empty. No plot will be generated.")
        return

    # Filter for white squirrels and exclude rows with NaN values in lat/long columns
    white_squirrels = df[(df["Highlights in Fur Color"] == "White") &
                         (~np.isnan(df["Squirrel Latitude (DD.DDDDDD)"])) &
                         (~np.isnan(df["Squirrel Longitude (-DD.DDDDDD)"]))]

    if white_squirrels.empty:
        print(
            "No valid white squirrel sightings in the dataframe. No plot will be generated.")
        return

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
