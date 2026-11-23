
import sqlite3
import pandas as pd
from pathlib import Path

# Connect to your existing SQL database
folder = Path(__file__).resolve().parent
conn = sqlite3.connect(folder / "finance_analysis.db")

# Calculate financial KPIs
query = """
SELECT
    "Ticker Symbol" AS Company,
    "Period Ending" AS Financial_Year,

    ROUND("Total Revenue" / 1000000000.0, 2)
        AS Revenue_Billions,

    ROUND("Net Income" / 1000000000.0, 2)
        AS Net_Income_Billions,

    ROUND(
        "Net Income" * 100.0 /
        NULLIF("Total Revenue", 0), 2
    ) AS Profit_Margin_Percent,

    ROUND(
        "Net Income" * 100.0 /
        NULLIF("Total Assets", 0), 2
    ) AS Return_On_Assets_Percent

FROM fundamentals

WHERE "Ticker Symbol" IN ('AAPL', 'MSFT', 'WMT')
  AND "Total Revenue" > 0

ORDER BY Company, Financial_Year;
"""

results = pd.read_sql_query(query, conn)

print("\nFINANCIAL KPI ANALYSIS")
print(results.to_string(index=False))

# Save results for future dashboard
results.to_csv("financial_kpi_results.csv", index=False)

print("\nFinancial KPI results saved successfully!")

conn.close()
