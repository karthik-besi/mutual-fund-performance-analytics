import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/practice_data.csv")

print("DAY 2: DATA ANALYSIS")

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nLAST 2 ROWS:")
print(df.tail(2))

print("\nSHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nSTATISTICS:")
print(df.describe())

print("\nSCORES ABOVE 80:")
print(df[df["score"] > 80])

print("\nAVERAGE SCORE:")
print(df["score"].mean())

print("\nMAXIMUM SCORE:")
print(df["score"].max())

print("\nMINIMUM SCORE:")
print(df["score"].min())