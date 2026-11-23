
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project folder
folder = Path(__file__).resolve().parent

# Load the results from our previous analyses
kpi = pd.read_csv(folder / "financial_kpi_results.csv")
growth = pd.read_csv(folder / "revenue_growth_results.csv")

# Extract financial years
kpi["Year"] = pd.to_datetime(
    kpi["Financial_Year"]
).dt.year

growth["Year"] = pd.to_datetime(
    growth["Financial_Year"]
).dt.year

# CHART 1: Revenue comparison
revenue = kpi.pivot(
    index="Year",
    columns="Company",
    values="Revenue_Billions"
)

revenue.plot(kind="bar", figsize=(10, 6))
plt.title("Company Revenue Comparison")
plt.xlabel("Fiscal Year Ending")
plt.ylabel("Revenue (USD Billions)")
plt.tight_layout()
plt.savefig(folder / "01_revenue_comparison.png")
plt.close()

# CHART 2: Year-over-year revenue growth
growth_chart = growth.pivot(
    index="Year",
    columns="Company",
    values="Revenue_Growth_Percent"
)

growth_chart.plot(kind="line", marker="o", figsize=(10, 6))
plt.axhline(0, linestyle="--")
plt.title("Year-over-Year Revenue Growth")
plt.xlabel("Fiscal Year Ending")
plt.ylabel("Revenue Growth (%)")
plt.tight_layout()
plt.savefig(folder / "02_revenue_growth.png")
plt.close()

# CHART 3: Profit margin comparison
profit = kpi.pivot(
    index="Year",
    columns="Company",
    values="Profit_Margin_Percent"
)

profit.plot(kind="line", marker="o", figsize=(10, 6))
plt.title("Net Profit Margin Comparison")
plt.xlabel("Fiscal Year Ending")
plt.ylabel("Net Profit Margin (%)")
plt.tight_layout()
plt.savefig(folder / "03_profit_margin.png")
plt.close()

print("FINANCIAL CHARTS CREATED SUCCESSFULLY!")
print("1. 01_revenue_comparison.png")
print("2. 02_revenue_growth.png")
print("3. 03_profit_margin.png")
