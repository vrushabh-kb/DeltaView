import os
from backend.data_engine import load_company_data, calculate_metrics

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(BASE_DIR, "data", "raw")


def percentile_score(value, all_values, reverse=False):

    sorted_vals = sorted(all_values)

    rank = sorted_vals.index(value)

    percentile = rank / (len(sorted_vals) - 1)

    if reverse:
        percentile = 1 - percentile

    return percentile * 100


def get_weights(strategy):

    if strategy == "growth":
        return {
            "sales": 0.35,
            "profit": 0.35,
            "margin": 0.15,
            "debt": 0.15
        }

    elif strategy == "value":
        return {
            "sales": 0.15,
            "profit": 0.20,
            "margin": 0.25,
            "debt": 0.40
        }

    else:  # quality
        return {
            "sales": 0.20,
            "profit": 0.20,
            "margin": 0.30,
            "debt": 0.30
        }


def rank_all_companies(strategy="quality"):

    weights = get_weights(strategy)

    companies = [
        f.replace(".xlsx", "")
        for f in os.listdir(DATA_FOLDER)
        if f.endswith(".xlsx")
    ]

    raw_data = []

    for company in companies:

        try:

            df = load_company_data(company)
            metrics = calculate_metrics(df)

            if not metrics:
                continue

            raw_data.append({
                "company": company,
                **metrics
            })

        except Exception as e:

            print("Error:", company, e)

    if len(raw_data) == 0:
        return []

    sales_vals = [c["sales_cagr"] for c in raw_data]
    profit_vals = [c["profit_cagr"] for c in raw_data]
    margin_vals = [c["avg_operating_margin"] for c in raw_data]
    debt_vals = [c["debt_to_cashflow"] for c in raw_data]

    ranked = []

    for c in raw_data:

        sales_score = percentile_score(
            c["sales_cagr"],
            sales_vals
        )

        profit_score = percentile_score(
            c["profit_cagr"],
            profit_vals
        )

        margin_score = percentile_score(
            c["avg_operating_margin"],
            margin_vals
        )

        debt_score = percentile_score(
            c["debt_to_cashflow"],
            debt_vals,
            reverse=True
        )

        final_score = (
            sales_score * weights["sales"]
            + profit_score * weights["profit"]
            + margin_score * weights["margin"]
            + debt_score * weights["debt"]
        )

        reason = []

        if c["sales_cagr"] > 15:
            reason.append("Strong Sales Growth")

        if c["profit_cagr"] > 15:
            reason.append("Strong Profit Growth")

        if c["avg_operating_margin"] > 20:
            reason.append("High Operating Margin")

        if c["debt_to_cashflow"] < 1:
            reason.append("Low Debt Risk")

        ranked.append({
            "company": c["company"],
            "score": round(final_score, 2),
            "reason": reason
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked