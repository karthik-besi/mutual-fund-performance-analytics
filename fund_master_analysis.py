import pandas as pd
from pathlib import Path

RAW_FOLDER = Path("data/raw")

fund_master = pd.read_csv(RAW_FOLDER / "01_fund_master.csv")
nav_history = pd.read_csv(RAW_FOLDER / "02_nav_history.csv")

print("FUND MASTER EXPLORATION")

print("\nUNIQUE FUND HOUSES:")
print(fund_master["fund_house"].unique())

print("\nUNIQUE CATEGORIES:")
print(fund_master["category"].unique())

print("\nUNIQUE SUB-CATEGORIES:")
print(fund_master["sub_category"].unique())

print("\nUNIQUE RISK CATEGORIES:")
print(fund_master["risk_category"].unique())

print("\nAMFI CODE VALIDATION:")

print("\nFUND MASTER COLUMNS:")
print(fund_master.columns.tolist())

print("\nNAV HISTORY COLUMNS:")
print(nav_history.columns.tolist())

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print(f"\nTotal AMFI codes in fund master: {len(fund_codes)}")
print(f"Total AMFI codes in NAV history: {len(nav_codes)}")
print(f"Missing AMFI codes in NAV history: {len(missing_codes)}")

if len(missing_codes) == 0:
    print("VALIDATION PASSED: Every AMFI code in fund_master exists in nav_history.")
else:
    print("VALIDATION FAILED: Some AMFI codes are missing in nav_history.")
    print("Missing codes:")
    print(sorted(missing_codes))