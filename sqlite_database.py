import sqlite3
import pandas as pd
from pathlib import Path

# Folder containing CSV files
RAW_FOLDER = Path("data/raw")

# Create SQLite database
conn = sqlite3.connect("mutual_fund_analysis.db")

print("Database created successfully!")

# Load CSV files into SQLite tables

fund_master = pd.read_csv(RAW_FOLDER / "01_fund_master.csv")
fund_master.to_sql("fund_master", conn, if_exists="replace", index=False)

nav_history = pd.read_csv(RAW_FOLDER / "02_nav_history.csv")
nav_history.to_sql("nav_history", conn, if_exists="replace", index=False)

aum = pd.read_csv(RAW_FOLDER / "03_aum_by_fund_house.csv")
aum.to_sql("aum_by_fund_house", conn, if_exists="replace", index=False)

sip = pd.read_csv(RAW_FOLDER / "04_monthly_sip_inflows.csv")
sip.to_sql("monthly_sip_inflows", conn, if_exists="replace", index=False)

transactions = pd.read_csv(RAW_FOLDER / "08_investor_transactions.csv")
transactions.to_sql("investor_transactions", conn, if_exists="replace", index=False)

portfolio = pd.read_csv(RAW_FOLDER / "09_portfolio_holdings.csv")
portfolio.to_sql("portfolio_holdings", conn, if_exists="replace", index=False)

benchmark = pd.read_csv(RAW_FOLDER / "10_benchmark_indices.csv")
benchmark.to_sql("benchmark_indices", conn, if_exists="replace", index=False)

print("All tables loaded successfully!")

# Verify tables
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("\nTables in Database:")
print(tables)

conn.close()

print("\nSQLite Database Created Successfully!")