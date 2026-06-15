def generate_ai_summary(metrics, structured_report):

    sales = metrics.get("sales_cagr", 0)
    profit = metrics.get("profit_cagr", 0)
    margin = metrics.get("avg_operating_margin", 0)
    debt = metrics.get("debt_to_cashflow", 0)

    return f"""
This company shows {sales}% sales growth and {profit}% profit growth.

Operating margin is {margin}%, indicating {'strong' if margin > 20 else 'moderate'} profitability.

Debt ratio of {debt} suggests {'low financial risk' if debt < 1 else 'moderate risk'}.

Overall, this appears to be a {'strong' if sales > 10 else 'stable'} investment candidate.
"""