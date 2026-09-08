import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import linregress
RAW_FOLDER = Path("data/raw")

nav = pd.read_csv(RAW_FOLDER / "02_nav_history.csv")
fund_master = pd.read_csv(RAW_FOLDER / "01_fund_master.csv")
benchmark = pd.read_csv(RAW_FOLDER / "10_benchmark_indices.csv")

benchmark["date"] = pd.to_datetime(benchmark["date"])

benchmark = benchmark.sort_values(["index_name", "date"])

benchmark["benchmark_return"] = benchmark.groupby("index_name")["close_value"].pct_change()

benchmark = benchmark[benchmark["index_name"] == "NIFTY100"]

print("\n===== BENCHMARK DATA =====")
print(benchmark.head())

print("\nAvailable Benchmark:")
print(benchmark["index_name"].unique())
print(nav.head())

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])

nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

print(nav.head(10))

print("\n===== DAILY RETURN STATISTICS =====")
print(nav["daily_return"].describe())

print("\nMissing Daily Returns:")
print(nav["daily_return"].isnull().sum())

extreme = nav[
    (nav["daily_return"] > 0.10) |
    (nav["daily_return"] < -0.10)
]

print("\nExtreme Returns:")
print(extreme)

plt.figure(figsize=(8, 5))
plt.hist(nav["daily_return"].dropna(), bins=50)
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.savefig("daily_return_distribution.png")
plt.close()

print("\n===== CAGR CALCULATION =====")

cagr_results = []

for code, fund in nav.groupby("amfi_code"):

    fund = fund.sort_values("date")

    start_nav = fund.iloc[0]["nav"]
    end_nav = fund.iloc[-1]["nav"]

    years = (fund.iloc[-1]["date"] - fund.iloc[0]["date"]).days / 365.25

    overall_cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    if years >= 1:
        one_year_nav = fund.iloc[-252]["nav"]
        cagr_1 = ((end_nav / one_year_nav) - 1) * 100
    else:
        cagr_1 = None

    if years >= 3:
        three_year_nav = fund.iloc[-756]["nav"]
        cagr_3 = ((end_nav / three_year_nav) ** (1 / 3) - 1) * 100
    else:
        cagr_3 = None

    if years >= 5:
        five_year_nav = fund.iloc[-1260]["nav"]
        cagr_5 = ((end_nav / five_year_nav) ** (1 / 5) - 1) * 100
    else:
        cagr_5 = None

    cagr_results.append({
        "amfi_code": code,
        "1 Year CAGR (%)": round(cagr_1, 2) if cagr_1 is not None else None,
        "3 Year CAGR (%)": round(cagr_3, 2) if cagr_3 is not None else None,
        "5 Year CAGR (%)": round(cagr_5, 2) if cagr_5 is not None else None,
        "Overall CAGR (%)": round(overall_cagr, 2)
    })

cagr_df = pd.DataFrame(cagr_results)

print("\n===== CAGR COMPARISON TABLE =====")
print(cagr_df)

cagr_df.to_csv("cagr_comparison.csv", index=False)

print("\nCAGR comparison table saved successfully!")

print("\nEarliest Date:", nav["date"].min())
print("Latest Date:", nav["date"].max())
print("\n===== SHARPE RATIO =====")

sharpe_results = []

risk_free_rate = 0.065 / 252

for code, fund in nav.groupby("amfi_code"):

    fund = fund.sort_values("date")

    avg_return = fund["daily_return"].mean()

    std_return = fund["daily_return"].std()

    if std_return != 0:
        sharpe = ((avg_return - risk_free_rate) / std_return) * (252 ** 0.5)
    else:
        sharpe = None

    sharpe_results.append({
        "amfi_code": code,
        "Sharpe Ratio": round(sharpe, 3) if sharpe is not None else None
    })

sharpe_df = pd.DataFrame(sharpe_results)

sharpe_df = sharpe_df.sort_values("Sharpe Ratio", ascending=False)

print("\n===== SHARPE RATIO TABLE =====")
print(sharpe_df)

sharpe_df.to_csv("sharpe_ratio.csv", index=False)

print("\nSharpe Ratio table saved successfully!")
print("\n===== SORTINO RATIO =====")

sortino_results = []

risk_free_rate = 0.065 / 252

for code, fund in nav.groupby("amfi_code"):

    fund = fund.sort_values("date")

    avg_return = fund["daily_return"].mean()

    downside_returns = fund[fund["daily_return"] < 0]["daily_return"]

    downside_std = downside_returns.std()

    if downside_std != 0 and not pd.isna(downside_std):
        sortino = ((avg_return - risk_free_rate) / downside_std) * (252 ** 0.5)
    else:
        sortino = None

    sortino_results.append({
        "amfi_code": code,
        "Sortino Ratio": round(sortino, 3) if sortino is not None else None
    })

sortino_df = pd.DataFrame(sortino_results)

sortino_df = sortino_df.sort_values("Sortino Ratio", ascending=False)

print("\n===== SORTINO RATIO TABLE =====")
print(sortino_df)

sortino_df.to_csv("sortino_ratio.csv", index=False)

print("\nSortino Ratio table saved successfully!")
print("\n===== ALPHA & BETA =====")

alpha_beta_results = []

benchmark_returns = benchmark[["date", "benchmark_return"]].dropna()

for code, fund in nav.groupby("amfi_code"):

    fund = fund[["date", "daily_return"]].dropna()

    merged = pd.merge(
        fund,
        benchmark_returns,
        on="date",
        how="inner"
    )

    if len(merged) > 30:

        slope, intercept, r_value, p_value, std_err = linregress(
            merged["benchmark_return"],
            merged["daily_return"]
        )

        beta = slope
        alpha = intercept * 252

    else:
        alpha = None
        beta = None

    alpha_beta_results.append({
        "amfi_code": code,
        "Alpha": round(alpha, 4) if alpha is not None else None,
        "Beta": round(beta, 4) if beta is not None else None
    })

alpha_beta_df = pd.DataFrame(alpha_beta_results)

print("\n===== ALPHA & BETA TABLE =====")
print(alpha_beta_df)

alpha_beta_df.to_csv("alpha_beta.csv", index=False)

print("\nAlpha & Beta saved successfully!")
print("\n===== MAXIMUM DRAWDOWN =====")

drawdown_results = []

for code, fund in nav.groupby("amfi_code"):

    fund = fund.sort_values("date")

    fund["running_max"] = fund["nav"].cummax()

    fund["drawdown"] = (fund["nav"] / fund["running_max"]) - 1

    max_drawdown = fund["drawdown"].min()

    drawdown_date = fund.loc[
        fund["drawdown"].idxmin(),
        "date"
    ]

    drawdown_results.append({
        "amfi_code": code,
        "Maximum Drawdown (%)": round(max_drawdown * 100, 2),
        "Worst Date": drawdown_date.date()
    })

drawdown_df = pd.DataFrame(drawdown_results)

drawdown_df = drawdown_df.sort_values(
    "Maximum Drawdown (%)"
)

print("\n===== MAXIMUM DRAWDOWN TABLE =====")
print(drawdown_df)

drawdown_df.to_csv("maximum_drawdown.csv", index=False)

print("\nMaximum Drawdown saved successfully!")
print("\n===== FUND SCORECARD =====")

scorecard = cagr_df.merge(
    sharpe_df,
    on="amfi_code"
)

scorecard = scorecard.merge(
    alpha_beta_df,
    on="amfi_code"
)

scorecard = scorecard.merge(
    drawdown_df[["amfi_code", "Maximum Drawdown (%)"]],
    on="amfi_code"
)

scorecard = scorecard.merge(
    fund_master[["amfi_code", "expense_ratio_pct"]],
    on="amfi_code"
)
scorecard["Return Rank"] = scorecard["3 Year CAGR (%)"].rank(ascending=False)

scorecard["Sharpe Rank"] = scorecard["Sharpe Ratio"].rank(ascending=False)

scorecard["Alpha Rank"] = scorecard["Alpha"].rank(ascending=False)

scorecard["Expense Rank"] = scorecard["expense_ratio_pct"].rank(ascending=True)

scorecard["Drawdown Rank"] = scorecard["Maximum Drawdown (%)"].rank(ascending=False)
scorecard["Fund Score"] = (

    scorecard["Return Rank"] * 0.30 +

    scorecard["Sharpe Rank"] * 0.25 +

    scorecard["Alpha Rank"] * 0.20 +

    scorecard["Expense Rank"] * 0.15 +

    scorecard["Drawdown Rank"] * 0.10

)
max_score = scorecard["Fund Score"].max()

scorecard["Fund Score"] = (
    (max_score - scorecard["Fund Score"]) / max_score
) * 100
scorecard = scorecard.sort_values(
    "Fund Score",
    ascending=False
)

print(scorecard[[
    "amfi_code",
    "Fund Score"
]])

scorecard.to_csv(
    "fund_scorecard.csv",
    index=False
)

print("\nFund Scorecard saved successfully!")
print("\n===== TOP 5 FUNDS =====")

top5 = scorecard.head(5)

print(top5[["amfi_code", "Fund Score"]])
comparison = nav[
    nav["amfi_code"].isin(top5["amfi_code"])
]
fig = px.line(
    comparison,
    x="date",
    y="nav",
    color="amfi_code",
    title="Top 5 Funds NAV Comparison"
)

fig.write_image("benchmark_comparison.png")
print("\n===== TRACKING ERROR =====")

tracking_results = []

benchmark_returns = benchmark[["date", "benchmark_return"]].dropna()

for code in top5["amfi_code"]:

    fund = nav[nav["amfi_code"] == code]

    merged = pd.merge(
        fund[["date", "daily_return"]],
        benchmark_returns,
        on="date",
        how="inner"
    )

    tracking_error = (
        (merged["daily_return"] - merged["benchmark_return"]).std()
    ) * (252 ** 0.5)

    tracking_results.append({
        "amfi_code": code,
        "Tracking Error": round(tracking_error, 4)
    })

tracking_df = pd.DataFrame(tracking_results)

print(tracking_df)

tracking_df.to_csv(
    "tracking_error.csv",
    index=False
)

print("\nTracking Error saved successfully!")