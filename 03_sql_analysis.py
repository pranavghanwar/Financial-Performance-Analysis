
import sqlite3
import pandas as pd

# Connect to financial database
conn = sqlite3.connect("finance_analysis.db")

# SQL query: Top 10 revenue records
query = """
SELECT
    "Ticker Symbol" AS Company,
    "Period Ending" AS Financial_Year,
    ROUND("Total Revenue" / 1000000000.0, 2)
        AS Revenue_Billions
FROM fundamentals
WHERE "Total Revenue" IS NOT NULL
ORDER BY "Total Revenue" DESC
LIMIT 10;
"""

results = pd.read_sql_query(query, conn)

print("\nTOP 10 COMPANY FINANCIAL RECORDS BY REVENUE")
print(results.to_string(index=False))

conn.close()
