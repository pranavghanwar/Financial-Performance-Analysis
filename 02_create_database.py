
import pandas as pd
import sqlite3
from pathlib import Path

# Get the project folder
folder = Path(__file__).resolve().parent

# Load Kaggle CSV files
fundamentals = pd.read_csv(folder / "fundamentals.csv")
securities = pd.read_csv(folder / "securities.csv")

# Connect to SQLite database
conn = sqlite3.connect(folder / "finance_analysis.db")

# Create SQL tables
fundamentals.to_sql(
    "fundamentals",
    conn,
    if_exists="replace",
    index=False
)

securities.to_sql(
    "securities",
    conn,
    if_exists="replace",
    index=False
)

# Verify the database
tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("DATABASE CREATED SUCCESSFULLY!")
print(tables)

conn.close()
