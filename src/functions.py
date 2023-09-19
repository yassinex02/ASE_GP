import matplotlib.pyplot as plt


def get_nof_squirrels_bycolors(df):
    fur_color_counts = df['Primary Fur Color'].value_counts()
    plt.figure(figsize=(10, 6))
    fur_color_counts.plot(kind='bar', color='skyblue')
    plt.title('Number of Squirrels Per Fur Color')
    plt.xlabel('Fur Color')
    plt.ylabel('Number of Squirrels')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Show the plot
    plt.show()
