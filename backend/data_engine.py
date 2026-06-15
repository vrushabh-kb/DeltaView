import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(BASE_DIR, "data", "raw")


def load_company_data(company_name):

    file_path = os.path.join(DATA_FOLDER, f"{company_name}.xlsx")

    df = pd.read_excel(file_path)

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    return df


def safe_cagr(start, end, years):

    if start <= 0 or end <= 0:
        return 0

    try:
        return ((end / start) ** (1 / years) - 1) * 100
    except:
        return 0


def calculate_metrics(df):

    sales_col = [c for c in df.columns if "sales" in c][0]
    profit_col = [c for c in df.columns if "profit" in c and "net" in c][0]

    # optional columns
    op_cols = [c for c in df.columns if "operating" in c]
    debt_cols = [c for c in df.columns if "debt" in c]
    cash_cols = [c for c in df.columns if "cash" in c]

    op_col = op_cols[0] if op_cols else None
    debt_col = debt_cols[0] if debt_cols else None
    cash_col = cash_cols[0] if cash_cols else None

    df = df.sort_index()

    years = len(df)

    sales_cagr = safe_cagr(df[sales_col].iloc[0], df[sales_col].iloc[-1], years - 1)
    profit_cagr = safe_cagr(df[profit_col].iloc[0], df[profit_col].iloc[-1], years - 1)

    # margin
    if op_col:
        margin = (df[op_col] / df[sales_col]) * 100
        avg_margin = margin.mean()
    else:
        avg_margin = (df[profit_col] / df[sales_col]).mean() * 100

    # debt
    if debt_col and cash_col:
        cashflow_mean = df[cash_col].mean()
        debt_ratio = df[debt_col].mean() / cashflow_mean if cashflow_mean != 0 else 0
    else:
        debt_ratio = 0

    return {
        "sales_cagr": round(float(sales_cagr), 2),
        "profit_cagr": round(float(profit_cagr), 2),
        "avg_operating_margin": round(float(avg_margin), 2),
        "debt_to_cashflow": round(float(debt_ratio), 2),
    }