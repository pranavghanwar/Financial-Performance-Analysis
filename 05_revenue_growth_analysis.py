
import sqlite3
import pandas as pd
from pathlib import Path

# Connect to existing financial database
folder = Path(__file__).resolve().parent
conn = sqlite3.connect(folder / "finance_analysis.db")

# Calculate year-over-year revenue growth
query = """
WITH revenue_data AS (
    SELECT
        "Ticker Symbol" AS Company,
        "Period Ending" AS Financial_Year,
        "Total Revenue" AS Revenue,

        LAG("Total Revenue") OVER (
            PARTITION BY "Ticker Symbol"
            ORDER BY "Period Ending"
        ) AS Previous_Revenue,

        LAG("Period Ending") OVER (
            PARTITION BY "Ticker Symbol"
            ORDER BY "Period Ending"
        ) AS Previous_Year

    FROM fundamentals
    WHERE "Ticker Symbol" IN ('AAPL', 'MSFT', 'WMT')
)

SELECT
    Company,
    Financial_Year,

    ROUND(Revenue / 1000000000.0, 2)
        AS Revenue_Billions,

    ROUND(
        (Revenue - Previous_Revenue) * 100.0 /
        NULLIF(Previous_Revenue, 0),
        2
    ) AS Revenue_Growth_Percent

FROM revenue_data
ORDER BY Company, Financial_Year;
"""

results = pd.read_sql_query(query, conn)

print("\nYEAR-OVER-YEAR REVENUE GROWTH")
print(results.to_string(index=False))

# Save results
results.to_csv(
    folder / "revenue_growth_results.csv",
    index=False
)

print("\nRevenue growth analysis saved successfully!")

conn.close()
