import pandas as pd

pd.options.display.max_rows = 50

df = pd.read_csv('data.csv')

print(df)

djson = pd.read_json('data.json')

print(djson.info())