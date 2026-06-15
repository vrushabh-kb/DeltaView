from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

from backend.ranking_engine import rank_all_companies
from backend.data_engine import load_company_data, calculate_metrics
from backend.ai_engine import generate_ai_summary

app = FastAPI()

# -----------------------------
# CORS (Frontend access)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = os.path.join(BASE_DIR, "data", "raw")


# -----------------------------
# COMPANY RANKING API
# -----------------------------
@app.get("/rank")
def get_rankings(strategy: str = "quality"):

    results = rank_all_companies(strategy)

    return [
        {
            "company": r["company"],
            "score": r["score"],
            "rank": i + 1,
            "reason": r["reason"]
        }
        for i, r in enumerate(results)
    ]


# -----------------------------
# COMPANY FINANCIAL DATA
# -----------------------------
@app.get("/company")
def get_company(company: str):

    company = company.upper()

    try:

        df = load_company_data(company)

        metrics = calculate_metrics(df)

        return {
            "company": company,

            "years": df.iloc[:, 0].tolist(),
            "revenue": df.iloc[:, 1].tolist(),
            "profit": df.iloc[:, 2].tolist(),

            "sales_cagr": metrics["sales_cagr"],
            "profit_cagr": metrics["profit_cagr"],
            "operating_margin": metrics["avg_operating_margin"],
            "debt_to_cashflow": metrics["debt_to_cashflow"]
        }

    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# AI SUMMARY API
# -----------------------------
@app.get("/ai-summary")
def get_ai_summary(company: str):

    try:
        company = company.upper()

        df = load_company_data(company)
        metrics = calculate_metrics(df)

        if not metrics:
            return {"summary": "Not enough data to analyze."}

        summary = generate_ai_summary(metrics, "")

        return {"summary": summary}

    except Exception as e:
        print("AI ERROR:", e)
        return {"summary": "AI summary unavailable."}


# -----------------------------
# COMPARE API (FIXED)
# -----------------------------
@app.get("/compare")
def compare_companies(company1: str, company2: str):
    try:
        company1 = company1.upper()
        company2 = company2.upper()

        df1 = load_company_data(company1)
        df2 = load_company_data(company2)

        m1 = calculate_metrics(df1)
        m2 = calculate_metrics(df2)

        return {
            "company1": company1,
            "company2": company2,
            "metrics": {
                "sales_cagr": [m1["sales_cagr"], m2["sales_cagr"]],
                "profit_cagr": [m1["profit_cagr"], m2["profit_cagr"]],
                "avg_operating_margin": [
                    m1["avg_operating_margin"],
                    m2["avg_operating_margin"]
                ],
                "debt_to_cashflow": [
                    m1["debt_to_cashflow"],
                    m2["debt_to_cashflow"]
                ]
            }
        }
    except Exception as e:
        print("COMPARE ERROR:", e)
        return {"error": str(e)}


# -----------------------------
# DELTASCORE BREAKDOWN API
# -----------------------------
@app.get("/score-breakdown")
def score_breakdown(company: str):

    try:

        company = company.upper()

        df = load_company_data(company)

        metrics = calculate_metrics(df)

        sales_score = min(
            metrics["sales_cagr"] * 2,
            25
        )

        profit_score = min(
            metrics["profit_cagr"] * 2,
            25
        )

        margin_score = min(
            metrics["avg_operating_margin"],
            25
        )

        debt_score = min(
            max(
                25 - (metrics["debt_to_cashflow"] * 5),
                0
            ),
            25
        )

        total_score = (
            sales_score +
            profit_score +
            margin_score +
            debt_score
        )

        return {

            "company": company,

            "sales_score": round(sales_score, 2),

            "profit_score": round(profit_score, 2),

            "margin_score": round(margin_score, 2),

            "debt_score": round(debt_score, 2),

            "total_score": round(total_score, 2)

        }

    except Exception as e:

        return {
            "error": str(e)
        }

    except Exception as e:

        return {
            "error": str(e)
        }