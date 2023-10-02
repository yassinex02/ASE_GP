import pandas as pd


df = pd.read_csv('data/dataset.csv', encoding='ISO-8859-1')
print(df['Primary Fur Color'].value_counts())
