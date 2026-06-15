from backend.ranking_engine import rank_all_companies

def build_portfolio(strategy, amount, stocks=5):

    ranked = rank_all_companies(strategy)
    selected = ranked[:stocks]

    total_score = sum([s["score"] for s in selected])

    portfolio = []

    for s in selected:

        weight = s["score"] / total_score
        investment = amount * weight

        portfolio.append({
            "company": s["company"],
            "investment": round(investment, 2),
            "weight": round(weight * 100, 2),
            "score": s["score"]
        })

    return portfolio