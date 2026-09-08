import pandas as pd

benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

print(benchmark.head())

print("\nColumns:")
print(benchmark.columns.tolist())