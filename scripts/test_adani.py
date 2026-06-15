import pandas as pd

COMPANY = "ADANIPORTS"
FILE_PATH = f"data/raw/{COMPANY}.xlsx"

df = pd.read_excel(FILE_PATH, sheet_name="financials")

# 🔥 Fix hidden spaces in column names
df.columns = df.columns.str.strip()

print("\n✅ RAW DATA:\n")
print(df)

print("\n✅ DATA TYPES:\n")
print(df.dtypes)

# Derived metrics
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
