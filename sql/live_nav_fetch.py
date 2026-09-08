import pandas as pd
import requests
from pathlib import Path

# Create output folder if it does not exist
RAW_FOLDER = Path("data/raw")
RAW_FOLDER.mkdir(parents=True, exist_ok=True)

# Required mutual fund scheme codes
schemes = {
    "hdfc_top_100_direct": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

print("===== LIVE NAV FETCH STARTED =====")

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        # Fund information
        meta = data["meta"]

        # NAV history data
        nav_df = pd.DataFrame(data["data"])

        # Add fund details as columns
        nav_df["scheme_code"] = scheme_code
        nav_df["scheme_name"] = meta["scheme_name"]
        nav_df["fund_house"] = meta["fund_house"]
        nav_df["scheme_category"] = meta["scheme_category"]
        nav_df["scheme_type"] = meta["scheme_type"]

        # Save each scheme NAV history as CSV
        output_file = RAW_FOLDER / f"{scheme_name}_nav.csv"
        nav_df.to_csv(output_file, index=False)

        print(f"\nSUCCESS: {scheme_name}")
        print(f"Scheme Code: {scheme_code}")
        print(f"Fund Name: {meta['scheme_name']}")
        print(f"Rows saved: {len(nav_df)}")
        print(f"Saved file: {output_file}")

    except Exception as e:
        print(f"\nERROR for {scheme_name}: {e}")

print("\n===== LIVE NAV FETCH COMPLETED =====")