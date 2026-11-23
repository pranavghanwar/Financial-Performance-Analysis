
import pandas as pd

# Step 1: Load the Kaggle financial dataset
df = pd.read_csv("fundamentals.csv")

# Step 2: Display the first five records
print("FIRST FIVE RECORDS")
print(df.head())

# Step 3: Check dataset size
print("\nDATASET SHAPE")
print(df.shape)

# Step 4: Find the number of companies
print("\nTOTAL COMPANIES")
print(df["Ticker Symbol"].nunique())

# Step 5: Filter Apple's financial data
apple = df[df["Ticker Symbol"] == "AAPL"].copy()

# Step 6: Select financial columns
apple = apple[
    ["Period Ending", "Total Revenue", "Net Income"]
]

# Step 7: Calculate net profit margin
apple["Profit Margin (%)"] = (
    apple["Net Income"] / apple["Total Revenue"]
) * 100

# Step 8: Display Apple's results
print("\nAPPLE FINANCIAL PERFORMANCE")
print(apple.to_string(index=False))

# Filter Apple's financial records
apple = df[df["Ticker Symbol"] == "AAPL"].copy()

# Select important financial columns
apple = apple[
    ["Period Ending", "Total Revenue", "Net Income"]
]

# Convert revenue and income into billions
apple["Revenue (Billions)"] = (
    apple["Total Revenue"] / 1_000_000_000
)

apple["Net Income (Billions)"] = (
    apple["Net Income"] / 1_000_000_000
)

# Calculate profit margin
apple["Profit Margin (%)"] = (
    apple["Net Income"] / apple["Total Revenue"]
) * 100

# Display results
print("\nAPPLE FINANCIAL ANALYSIS")

print(
    apple[
        [
            "Period Ending",
            "Revenue (Billions)",
            "Net Income (Billions)",
            "Profit Margin (%)"
        ]
    ].round(2).to_string(index=False)
)
