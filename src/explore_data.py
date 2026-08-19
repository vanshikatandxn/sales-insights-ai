import pandas as pd

df = pd.read_csv("../data/raw/sales_data_raw.csv", encoding="ISO-8859-1")

print("Shape:", df.shape)
print(df.head())
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
