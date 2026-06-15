from backend.data_engine import load_company_data, calculate_metrics


def compare_companies(company1, company2):

    df1 = load_company_data(company1)
    df2 = load_company_data(company2)

    m1 = calculate_metrics(df1)
    m2 = calculate_metrics(df2)

    comparison = {
        "company1": company1,
        "company2": company2,
        "metrics": {
            "sales_cagr": [m1["sales_cagr"], m2["sales_cagr"]],
            "profit_cagr": [m1["profit_cagr"], m2["profit_cagr"]],
            "eps_cagr": [m1["eps_cagr"], m2["eps_cagr"]],
            "operating_margin": [m1["avg_operating_margin"], m2["avg_operating_margin"]],
            "expense_ratio": [m1["expense_ratio"], m2["expense_ratio"]],
            "cashflow_margin": [m1["cashflow_margin"], m2["cashflow_margin"]],
            "debt_to_cashflow": [m1["debt_to_cashflow"], m2["debt_to_cashflow"]],
        }
    }

    return comparison