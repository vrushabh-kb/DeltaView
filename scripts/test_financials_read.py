import pandas as pd

FILE_PATH = "data/raw/TCS_financials.xlsx"

df = pd.read_excel(FILE_PATH, sheet_name="financials")

print("\n✅ RAW DATA FROM EXCEL:\n")
print(df)

print("\n✅ DATA TYPES:\n")
print(df.dtypes)

# Simple derived metrics test
df["operating_margin_pct"] = (df["operating_profit"] / df["sales"]) * 100
df["debt_to_cashflow"] = df["total_debt"] / df["operating_cash_flow"]

print("\n✅ WITH DERIVED METRICS:\n")
print(df[[
    "year",
    "sales",
    "operating_profit",
    "operating_margin_pct",
    "eps",
    "operating_cash_flow",
    "total_debt",
    "debt_to_cashflow"
]])
