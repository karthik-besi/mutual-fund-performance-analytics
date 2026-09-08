import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
RAW_FOLDER = Path("data/raw")
nav = pd.read_csv(RAW_FOLDER / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()
nav = pd.read_csv(RAW_FOLDER / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()
print("\n===== NAV DATA =====")
print(nav.head())

print("\nTotal Schemes:")
print(nav["amfi_code"].nunique())
print("\n===== HISTORICAL VaR & CVaR =====")

var_results = []

for code, fund in nav.groupby("amfi_code"):

    returns = fund["daily_return"].dropna()

    if len(returns) == 0:
        continue

    var_95 = np.percentile(returns, 5)

    cvar_95 = returns[returns <= var_95].mean()

    var_results.append({
        "amfi_code": code,
        "VaR_95 (%)": round(var_95 * 100, 2),
        "CVaR_95 (%)": round(cvar_95 * 100, 2)
    })

var_df = pd.DataFrame(var_results)

print(var_df)

var_df.to_csv("var_cvar_report.csv", index=False)

print("\nVaR & CVaR report saved successfully!")
print("\n===== ROLLING 90-DAY SHARPE RATIO =====")

plt.figure(figsize=(14,7))

top5_funds = nav["amfi_code"].unique()[:5]

for code in top5_funds:

    fund = nav[nav["amfi_code"] == code].copy()

    rolling_mean = fund["daily_return"].rolling(90).mean()

    rolling_std = fund["daily_return"].rolling(90).std()

    fund["rolling_sharpe"] = (
        rolling_mean / rolling_std
    ) * np.sqrt(252)

    plt.plot(
        fund["date"],
        fund["rolling_sharpe"],
        label=str(code)
    )

plt.title("Rolling 90-Day Sharpe Ratio (Top 5 Funds)")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend(title="AMFI Code")
plt.grid(True)

plt.tight_layout()

plt.savefig("rolling_sharpe_chart.png")

plt.close()

print("\nRolling Sharpe chart saved successfully!")
print("\n===== INVESTOR COHORT ANALYSIS =====")

transactions = pd.read_csv(
    RAW_FOLDER / "08_investor_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

print("\nFIRST 5 ROWS:")
print(transactions.head())

print("\nCOLUMNS:")
print(transactions.columns.tolist())
print("\n===== INVESTOR COHORT ANALYSIS =====")

transactions["cohort_year"] = (
    transactions.groupby("investor_id")["transaction_date"]
    .transform("min")
    .dt.year
)

sip_transactions = transactions[
    transactions["transaction_type"] == "SIP"
]

avg_sip = (
    sip_transactions
    .groupby("cohort_year")["amount_inr"]
    .mean()
    .reset_index(name="Average SIP Amount")
)

total_invested = (
    transactions
    .groupby("cohort_year")["amount_inr"]
    .sum()
    .reset_index(name="Total Invested")
)

top_fund = (
    transactions
    .groupby(["cohort_year", "amfi_code"])
    .size()
    .reset_index(name="Count")
)

top_fund = (
    top_fund
    .sort_values(["cohort_year", "Count"], ascending=[True, False])
    .groupby("cohort_year")
    .first()
    .reset_index()
)

cohort_report = (
    avg_sip
    .merge(total_invested, on="cohort_year")
    .merge(
        top_fund[["cohort_year", "amfi_code"]],
        on="cohort_year"
    )
)

print(cohort_report)

cohort_report.to_csv(
    "investor_cohort_analysis.csv",
    index=False
)

print("\nInvestor Cohort Analysis saved successfully!")
print("\n===== SIP CONTINUITY ANALYSIS =====")

sip = transactions[
    transactions["transaction_type"] == "SIP"
].copy()

sip = sip.sort_values(
    ["investor_id", "transaction_date"]
)

sip["gap_days"] = (
    sip.groupby("investor_id")["transaction_date"]
    .diff()
    .dt.days
)

sip_summary = (
    sip.groupby("investor_id")
    .agg(
        sip_transactions=("transaction_date", "count"),
        average_gap_days=("gap_days", "mean")
    )
    .reset_index()
)

sip_summary = sip_summary[
    sip_summary["sip_transactions"] >= 6
]

sip_summary["status"] = np.where(
    sip_summary["average_gap_days"] > 35,
    "At Risk",
    "Active"
)

print(sip_summary)

sip_summary.to_csv(
    "sip_continuity_report.csv",
    index=False
)

print("\nSIP Continuity Report saved successfully!")
print("\n===== SIMPLE FUND RECOMMENDER =====")

fund_master = pd.read_csv(
    RAW_FOLDER / "01_fund_master.csv"
)

print("\nFund Master Columns:")
print(fund_master.columns.tolist())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())
sharpe_df = pd.read_csv("sharpe_ratio.csv")
print("\n===== FUND RECOMMENDER =====")

recommendation = input(
    "\nEnter Risk Appetite (Low / Moderate / Moderately High / High / Very High): "
)

recommendation = recommendation.strip().title()

funds = fund_master[
    fund_master["risk_category"] == recommendation
]

recommended = funds.merge(
    sharpe_df,
    on="amfi_code"
)

recommended = recommended.sort_values(
    "Sharpe Ratio",
    ascending=False
)

top3 = recommended.head(3)

print("\n===== TOP 3 RECOMMENDED FUNDS =====")
print(
    top3[
        [
            "scheme_name",
            "fund_house",
            "risk_category",
            "Sharpe Ratio"
        ]
    ]
)

top3.to_csv(
    "recommended_funds.csv",
    index=False
)

print("\nRecommended funds saved successfully!")
print("\n===== SECTOR HHI CONCENTRATION =====")

holdings = pd.read_csv(
    RAW_FOLDER / "09_portfolio_holdings.csv"
)

print("\nPortfolio Holdings Columns:")
print(holdings.columns.tolist())

print("\nFirst 5 Rows:")
print(holdings.head())
print("\n===== SECTOR HHI CONCENTRATION REPORT =====")

holdings["weight_decimal"] = holdings["weight_pct"] / 100

hhi = (
    holdings
    .groupby("amfi_code")["weight_decimal"]
    .apply(lambda x: (x ** 2).sum())
    .reset_index(name="HHI")
)

hhi = hhi.sort_values("HHI", ascending=False)

print(hhi)

hhi.to_csv(
    "sector_hhi_report.csv",
    index=False
)

print("\nSector HHI report saved successfully!")