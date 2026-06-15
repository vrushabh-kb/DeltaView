import pandas as pd
import os

DATA_FOLDER = "data/raw"

BANKS = {"SBIBANK", "HDFCBANK", "ICICIBANK", "AXISBANK", "KOTAKBANK"}

REQUIRED_FULL = {
    "year",
    "sales",
    "expenses",
    "operating_profit",
    "net_profit",
    "eps",
    "cash_from_operating_activity",
    "total_debt"
}

REQUIRED_BANK = {
    "year",
    "sales",
    "net_profit",
    "eps",
    "cash_from_operating_activity",
    "total_debt"
}

print("\n🔍 VALIDATING ALL COMPANIES...\n")

files = os.listdir(DATA_FOLDER)

for file in files:
    if file.endswith(".xlsx") or file.endswith(".csv"):
        company = file.split(".")[0].upper()

        try:
            path = os.path.join(DATA_FOLDER, file)
            df = pd.read_excel(path) if file.endswith(".xlsx") else pd.read_csv(path)

            # Normalize column names
            df.columns = (
                df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
                .str.replace("-", "_")
            )

            # Accept operating_cash_flow as alias
            if "operating_cash_flow" in df.columns:
                df.rename(columns={"operating_cash_flow": "cash_from_operating_activity"}, inplace=True)

            required = REQUIRED_BANK if company in BANKS else REQUIRED_FULL
            missing = required - set(df.columns)

            if missing:
                print(f"❌ {company} — Missing column(s): {', '.join(missing)}")
            else:
                print(f"✅ {company} — OK")

        except Exception as e:
            print(f"❌ {company} — ERROR: {str(e)}")

print("\n✅ VALIDATION COMPLETE.")
