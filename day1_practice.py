import pandas as pd

df = pd.read_csv("data/raw/practice_data.csv")

print("DATA:")
print(df)

print("\nSHAPE:")
print(df.shape)

print("\nDATA TYPES:")
print(df.dtypes)

print("\n 5 ROWS:")
print(df.head())
print("\nSTATISTICS:")
print(df.describe())

print("\nAVERAGE SCORE:")
print(df["score"].mean())