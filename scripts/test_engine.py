from backend.data_engine import load_company_data, calculate_metrics
from backend.delta_engine import interpret_metrics
from backend.ai_engine import generate_ai_summary

company = "TCS"

df = load_company_data(company)
metrics = calculate_metrics(df)
structured_report = interpret_metrics(metrics)

ai_summary = generate_ai_summary(metrics, structured_report)

print("\nAI SUMMARY:\n")
print(ai_summary)