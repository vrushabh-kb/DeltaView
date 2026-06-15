def interpret_metrics(metrics):
    sales_cagr = metrics["sales_cagr"]
    profit_cagr = metrics["profit_cagr"]
    margin = metrics["avg_operating_margin"]
    debt_ratio = metrics["debt_to_cashflow"]

    report = ""

    # -------------------- REVENUE ANALYSIS --------------------

    if sales_cagr >= 15:
        report += (
            f"The company has demonstrated strong revenue expansion over the evaluated period, "
            f"with sales compounding at an annual rate of {sales_cagr}%. "
            "Such growth typically reflects either increasing market share, pricing power, or structural industry tailwinds. "
            "Sustained double-digit growth at this level indicates a business operating in a favorable demand environment. "
        )
    elif sales_cagr >= 8:
        report += (
            f"Revenue has compounded at {sales_cagr}% annually, reflecting steady and consistent growth. "
            "While not hyper-growth, this level of expansion suggests business stability and predictable demand dynamics. "
            "The company appears capable of maintaining gradual scale without excessive volatility. "
        )
    else:
        report += (
            f"Revenue growth has been modest at {sales_cagr}% CAGR. "
            "This may indicate a mature business profile, competitive pressures, or limited expansion opportunities. "
            "Sustained low growth could constrain long-term value creation unless margins improve significantly. "
        )

    # -------------------- PROFIT VS SALES DYNAMICS --------------------

    if profit_cagr > sales_cagr:
        report += (
            f"Importantly, profit growth at {profit_cagr}% exceeds revenue growth, "
            "suggesting improving operating leverage and rising efficiency. "
            "This indicates that incremental revenue is translating into disproportionately higher earnings, "
            "a favorable sign of cost control and scalability. "
        )
    elif profit_cagr < sales_cagr:
        report += (
            f"However, profit growth at {profit_cagr}% trails revenue growth, "
            "which may signal cost pressures, margin compression, or reinvestment into expansion. "
            "If this trend persists, it could indicate structural profitability constraints. "
        )
    else:
        report += (
            "Profit growth remains broadly aligned with revenue growth, "
            "indicating a stable relationship between top-line expansion and earnings generation. "
        )

    # -------------------- MARGIN QUALITY --------------------

    if margin >= 25:
        report += (
            f"The business operates at a high average operating margin of approximately {margin}%, "
            "which reflects strong pricing power, brand positioning, or structural cost advantages. "
            "High-margin profiles often provide resilience during economic slowdowns and greater reinvestment flexibility. "
        )
    elif margin >= 15:
        report += (
            f"Operating margins average around {margin}%, which is healthy for most industries. "
            "This suggests reasonable operational efficiency, though sustained margin expansion would further strengthen the business profile. "
        )
    else:
        report += (
            f"Operating margins of around {margin}% indicate relatively tight profitability. "
            "In competitive sectors, low margins can expose the business to earnings volatility during downturns. "
        )

    # -------------------- DEBT & FINANCIAL STABILITY --------------------

    if debt_ratio is None:
        report += (
            "Debt sustainability cannot be fully assessed due to insufficient cash flow data. "
        )
    elif debt_ratio < 1:
        report += (
            "Debt levels appear highly manageable relative to annual operating cash flow. "
            "This implies strong balance sheet flexibility and low financial stress risk. "
            "The company should be capable of servicing obligations comfortably even under moderate downturn scenarios. "
        )
    elif debt_ratio < 3:
        report += (
            "Debt levels are reasonable but warrant monitoring. "
            "While current cash generation appears adequate, significant deterioration in profitability could tighten coverage metrics. "
        )
    else:
        report += (
            "Leverage appears elevated relative to operating cash flow. "
            "Such a structure increases financial risk, particularly in cyclical environments or periods of earnings contraction. "
        )

    # -------------------- OVERALL ASSESSMENT --------------------

    report += (
        "Overall, the company exhibits a financial profile that combines growth dynamics, margin structure, "
        "and leverage positioning. Investors should monitor whether profit growth accelerates in line with revenue "
        "and whether capital allocation decisions sustain long-term value creation. "
    )

    return report.strip()