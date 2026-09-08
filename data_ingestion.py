import pandas as pd
from pathlib import Path
RAW_FOLDER = Path("data/raw")
csv_files = [
    file for file in RAW_FOLDER.glob("*.csv")
    if file.name[0:2].isdigit()
]
print("===== DAY 1: DATA INGESTION =====")
print(f"Total CSV files found: {len(csv_files)}")
csv_files = [
    file for file in RAW_FOLDER.glob("*.csv")
    if file.name[0:2].isdigit()
]
if len(csv_files) != 10:
    print("\nWARNING: Expected 10 CSV files.")
    print("Check whether all files are inside data/raw folder.")

for file in csv_files:
    print("\n" + "=" * 60)
    print(f"FILE NAME: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nDUPLICATE ROWS:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"ERROR while reading {file.name}: {e}")

print("\n===== DATA INGESTION COMPLETED =====")  