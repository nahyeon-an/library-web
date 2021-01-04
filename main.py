import pandas as pd
df = pd.read_csv("library-data.csv", encoding='CP949')
print(df.shape)
print(df.iloc[0])
print(df.info(verbose=True))
print(df.columns)
