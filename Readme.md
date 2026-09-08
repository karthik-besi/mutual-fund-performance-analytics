# 📊 Mutual Fund Performance Analytics

A comprehensive **Python-based Mutual Fund Performance Analytics project** that analyzes mutual fund NAV, returns, risk, investor behavior, benchmark performance, and portfolio characteristics.

The project uses **Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, SQLite, and statistical analysis** to transform raw mutual fund data into meaningful investment insights.

---

## 🎯 Project Objective

The main objective of this project is to analyze mutual fund performance and answer questions such as:

* Which mutual funds performed better over different time periods?
* Which funds provide better risk-adjusted returns?
* How much return did investors receive over 1-year, 3-year, and 5-year periods?
* How risky are different mutual funds?
* How do mutual funds perform compared with their benchmark indices?
* Which funds have better Alpha and Beta?
* Which funds have lower Maximum Drawdown?
* Which funds have better Sharpe and Sortino Ratios?
* Which funds are recommended based on a composite performance score?
* How are investor transactions and portfolio holdings distributed?
* How have SIP inflows, AUM, and folio counts changed over time?

---

# 🛠️ Technologies Used

### Programming

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SciPy
* Requests

### Database

* SQLite
* SQL

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 📁 Project Structure

```text
mutual-fund-analysis/
│
├── data/
│   └── raw/
│       ├── 01_fund_master.csv
│       ├── 02_nav_history.csv
│       ├── 03_aum_by_fund_house.csv
│       ├── 04_monthly_sip_inflows.csv
│       ├── 05_category_inflows.csv
│       ├── 06_industry_folio_count.csv
│       ├── 07_scheme_performance.csv
│       ├── 08_investor_transactions.csv
│       ├── 09_portfolio_holdings.csv
│       ├── 10_benchmark_indices.csv
│       ├── axis_bluechip_nav.csv
│       ├── hdfc_top_100_direct_nav.csv
│       ├── icici_bluechip_nav.csv
│       ├── kotak_bluechip_nav.csv
│       ├── nippon_large_cap_nav.csv
│       └── sbi_bluechip_nav.csv
│
├── notebooks/
│
├── sql/
│   └── data_ingestion.py
│
├── EDA.ipynb
├── Advanced_Analytics.ipynb
│
├── data_ingestion.py
├── day1_practice.py
├── day2_eda.py
├── fund_master_analysis.py
├── live_nav_fetch.py
├── performance_analytics.py
├── advanced_analytics.py
├── benchmark.py
├── sqlite_database.py
├── test_database.py
│
├── cagr_comparison.csv
├── sharpe_ratio.csv
├── sortino_ratio.csv
├── alpha_beta.csv
├── maximum_drawdown.csv
├── fund_scorecard.csv
├── recommended_funds.csv
├── tracking_error.csv
├── var_cvar_report.csv
├── sector_hhi_report.csv
├── investor_cohort_analysis.csv
└── sip_continuity_report.csv
```

---

# 📂 Dataset

The project uses multiple datasets covering different aspects of the mutual fund industry.

### 1. Fund Master

Contains information such as:

* AMFI Code
* Fund House
* Scheme Name
* Category
* Sub-category
* Plan
* Launch Date
* Benchmark
* Expense Ratio
* Exit Load
* Minimum SIP Amount
* Minimum Lumpsum Amount
* Fund Manager
* Risk Category
* SEBI Category Code

### 2. NAV History

Contains historical Net Asset Value information used for:

* Daily returns
* NAV trends
* CAGR
* Volatility
* Risk analysis
* Drawdown analysis

The historical NAV dataset covers approximately:

**January 2022 – May 2026**

### 3. AUM Data

Used to analyze:

* Assets Under Management
* Fund-house level AUM
* AUM growth

### 4. SIP Inflows

Used to analyze:

* Monthly SIP inflows
* SIP growth
* Investor contribution trends

### 5. Category Inflows

Used to analyze capital flows across mutual fund categories.

### 6. Folio Count

Used to analyze investor participation and growth in mutual fund folios.

### 7. Scheme Performance

Contains scheme-level performance information.

### 8. Investor Transactions

Used for:

* Investor behavior analysis
* Cohort analysis
* SIP continuity analysis

### 9. Portfolio Holdings

Used for portfolio and sector-level analysis.

### 10. Benchmark Indices

Used to compare mutual fund performance against relevant benchmarks.

---

# 🔄 Data Pipeline

The project follows the following analytical workflow:

```text
Raw CSV Data
     ↓
Data Ingestion
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
NAV & Return Calculation
     ↓
Risk & Performance Analysis
     ↓
Benchmark Comparison
     ↓
Advanced Analytics
     ↓
Fund Scorecard
     ↓
Investment Insights
```

---

# 📥 Data Ingestion

The project includes scripts for loading and validating the available datasets.

The data ingestion process checks:

* Dataset shape
* Column names
* Data types
* Missing values
* Duplicate records
* Basic data quality

Live NAV data was also fetched for selected mutual fund schemes using the MFAPI service.

---

# 🔎 Exploratory Data Analysis

EDA was performed to understand the structure and behavior of the mutual fund data.

### Key areas analyzed:

* Fund houses
* Mutual fund categories
* Sub-categories
* NAV trends
* AUM
* SIP inflows
* Folio counts
* Scheme performance
* Investor transactions
* Portfolio holdings
* Benchmark indices

### Fund Houses Analyzed

Examples include:

* SBI Mutual Fund
* HDFC Mutual Fund
* ICICI Prudential Mutual Fund
* Nippon India Mutual Fund
* Kotak Mahindra Mutual Fund
* Axis Mutual Fund
* Aditya Birla Sun Life Mutual Fund
* UTI Mutual Fund
* Mirae Asset Mutual Fund
* DSP Mutual Fund

### Major Categories

The dataset includes categories such as:

* Equity
* Debt

with sub-categories including:

* Large Cap
* Mid Cap
* Small Cap
* Flexi Cap
* Large & Mid Cap
* Value
* ELSS
* Gilt
* Liquid
* Short Duration
* Index
* Index/ETF

---

# 📈 Performance Analytics

The project calculates several important mutual fund performance metrics.

## CAGR

Compound Annual Growth Rate is calculated for:

* 1-Year
* 3-Year
* 5-Year

CAGR helps compare long-term investment growth across funds.

---

## 📊 Daily Returns

Daily returns are calculated from historical NAV data.

The basic calculation is:

```text
Daily Return = (Today's NAV / Previous NAV) - 1
```

Daily returns are then used for further risk and performance calculations.

---

# ⚖️ Risk Analysis

The project analyzes multiple risk measures.

### Sharpe Ratio

Measures risk-adjusted returns.

A higher Sharpe Ratio generally indicates better return relative to the amount of risk taken.

---

### Sortino Ratio

Similar to Sharpe Ratio but focuses on downside volatility.

This helps evaluate performance while giving more importance to negative returns.

---

### Maximum Drawdown

Measures the largest decline from a previous peak in NAV.

It helps identify the potential downside experienced by an investor.

---

### Value at Risk (VaR)

VaR is used to estimate potential losses under a specified confidence level.

---

### Conditional Value at Risk (CVaR)

CVaR measures the expected loss during the worst outcomes beyond the VaR threshold.

---

# 📐 Alpha & Beta Analysis

The project performs regression-based Alpha and Beta analysis.

### Alpha

Alpha indicates the excess return generated relative to the expected return based on the benchmark.

A positive Alpha can indicate outperformance relative to the benchmark.

### Beta

Beta measures the sensitivity of a fund's returns to movements in its benchmark.

```text
Beta > 1
Higher sensitivity to market movements

Beta < 1
Lower sensitivity to market movements
```

---

# 📊 Benchmark Comparison

Mutual fund performance is compared against relevant benchmark indices.

The analysis includes:

* Fund returns
* Benchmark returns
* Excess returns
* Alpha
* Beta
* Tracking Error

This helps determine whether a fund is outperforming or underperforming its benchmark.

---

# 📏 Tracking Error

Tracking Error measures the difference between fund returns and benchmark returns.

A lower tracking error generally indicates that a fund follows its benchmark more closely.

---

# 📈 Rolling Sharpe Ratio

Rolling Sharpe Ratio analysis is used to understand how risk-adjusted performance changes over time.

This provides a time-based view of fund consistency rather than relying only on a single Sharpe Ratio.

---

# 👥 Investor Analysis

The project also analyzes investor behavior using transaction-level data.

### Analyses include:

* Investor cohort analysis
* SIP continuity
* Transaction patterns
* Portfolio holdings
* Investor participation

---

# 🏭 Sector Concentration Analysis

Sector-level portfolio concentration is analyzed using the **Herfindahl-Hirschman Index (HHI)**.

This helps identify whether a portfolio is:

* Highly concentrated
* Moderately diversified
* Broadly diversified

---

# 🏆 Fund Scorecard

A composite Fund Scorecard was created to rank mutual funds based on multiple performance and risk factors.

### Scorecard Weights

| Metric                | Weight |
| --------------------- | -----: |
| 3-Year Return Rank    |    30% |
| Sharpe Ratio Rank     |    25% |
| Alpha Rank            |    20% |
| Expense Ratio Rank    |    15% |
| Maximum Drawdown Rank |    10% |

### Composite Score

```text
Fund Score =
    30% × 3-Year Return Rank
  + 25% × Sharpe Rank
  + 20% × Alpha Rank
  + 15% × Expense Ratio Rank
  + 10% × Maximum Drawdown Rank
```

This scorecard combines **return, risk, cost, and consistency** into a single ranking framework.

---

# ⭐ Fund Recommendations

Based on the composite scorecard, the project generates a list of recommended funds.

The recommendation framework considers:

* Historical returns
* Risk-adjusted performance
* Alpha
* Expense ratio
* Maximum drawdown

> **Note:** These recommendations are based on historical data and analytical scoring. They should not be considered financial advice or guaranteed future performance.

---

# 🗄️ SQLite Database

The project also includes a SQLite database:

```text
mutual_fund_analysis.db
```

The database is used to organize and query mutual fund data using SQL.

The database workflow includes:

```text
CSV Files
   ↓
Data Ingestion
   ↓
SQLite Database
   ↓
SQL Queries
   ↓
Analytics
```

---

# 📊 Visualizations

The project generates multiple visualizations for analytical interpretation.

Examples include:

* NAV trend charts
* Daily return distributions
* Benchmark comparison
* Rolling Sharpe Ratio
* Fund performance comparisons
* Risk analysis charts

Example generated files:

```text
benchmark_comparison.png
daily_return_distribution.png
rolling_sharpe_chart.png
rolling_sharpe_100016.png
rolling_sharpe_100025.png
rolling_sharpe_100033.png
rolling_sharpe_101206.png
rolling_sharpe_101207.png
```

---

# 📁 Key Analytical Outputs

The project generates several analytical datasets:

| File                           | Purpose                     |
| ------------------------------ | --------------------------- |
| `cagr_comparison.csv`          | CAGR comparison             |
| `sharpe_ratio.csv`             | Sharpe Ratio analysis       |
| `sortino_ratio.csv`            | Sortino Ratio analysis      |
| `alpha_beta.csv`               | Alpha & Beta analysis       |
| `maximum_drawdown.csv`         | Drawdown analysis           |
| `fund_scorecard.csv`           | Composite fund ranking      |
| `recommended_funds.csv`        | Recommended funds           |
| `tracking_error.csv`           | Benchmark tracking analysis |
| `var_cvar_report.csv`          | VaR & CVaR analysis         |
| `sector_hhi_report.csv`        | Sector concentration        |
| `investor_cohort_analysis.csv` | Investor cohort analysis    |
| `sip_continuity_report.csv`    | SIP continuity analysis     |

---

# 💡 Key Industry KPIs

The dataset provides a broad view of the Indian mutual fund industry.

Important KPIs analyzed include:

* **Total AUM:** approximately ₹81 lakh crore
* **SIP Inflows:** approximately ₹31 thousand crore
* **Total Folios:** approximately 26.12 crore
* **Number of Schemes:** approximately 1,908

The analysis also tracks folio growth from approximately:

```text
13.26 crore — January 2022
        ↓
26.12 crore — December 2025
```

This demonstrates substantial growth in investor participation during the analyzed period.

---

# 🔬 Advanced Analytics

The project goes beyond basic EDA and includes:

* CAGR analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Rolling Sharpe Ratio
* Benchmark comparison
* Tracking Error
* VaR
* CVaR
* Sector HHI
* Investor Cohort Analysis
* SIP Continuity Analysis
* Composite Fund Scorecard

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/karthik-besi/mutual-fund-performance-analytics.git
```

## 2. Navigate to the Project

```bash
cd mutual-fund-performance-analytics
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## 5. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn plotly scipy requests sqlalchemy jupyter
```

## 6. Run Data Ingestion

```bash
python data_ingestion.py
```

## 7. Run Performance Analytics

```bash
python performance_analytics.py
```

## 8. Run Advanced Analytics

```bash
python advanced_analytics.py
```

## 9. Run Benchmark Analysis

```bash
python benchmark.py
```

## 10. Run Database Operations

```bash
python sqlite_database.py
```

---

# 📓 Jupyter Notebooks

The project also includes notebooks for interactive analysis.

### EDA

```text
EDA.ipynb
```

Used for exploratory data analysis and visualization.

### Advanced Analytics

```text
Advanced_Analytics.ipynb
```

Used for advanced performance and risk analysis.

Run Jupyter Notebook using:

```bash
jupyter notebook
```

---

# 🔮 Future Improvements

Potential improvements include:

* Interactive Streamlit dashboard
* Real-time NAV updates
* Automated daily data ingestion
* Portfolio optimization
* Risk profiling
* Machine learning-based return prediction
* Automated fund recommendation system
* Cloud database integration
* Interactive benchmark comparison
* Automated reporting
* Deployment as a web application

---

# ⚠️ Disclaimer

This project is created for **educational, analytical, and portfolio purposes**.

The analysis is based on historical data. Historical performance does not guarantee future returns.

The fund rankings and recommendations generated by this project should **not be considered financial advice**.

---

# 👨‍💻 Author

**B Karthik**

Computer Science & Engineering

---

# ⭐ Project Highlights

This project demonstrates practical experience in:

```text
Python
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Statistical Analysis
   ↓
Financial Analytics
   ↓
Risk Analysis
   ↓
SQL & Database Management
   ↓
Data Visualization
   ↓
Investment Performance Analysis
```

---

## 📌 GitHub Repository

**Mutual Fund Performance Analytics**

https://github.com/karthik-besi/mutual-fund-performance-analytics
