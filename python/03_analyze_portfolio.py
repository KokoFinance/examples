"""
Analyze a credit card portfolio.

Pass your cards (just names are enough) and get a full value breakdown.
Add spending data for more accurate results.
Fast endpoint returns deterministic calculations in <100ms.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Simple: just card names
result = client.analyze_portfolio(
    cards=[
        {"card_name": "Chase Sapphire Reserve"},
        {"card_name": "Amex Gold Card"},
        {"card_name": "Citi Double Cash"},
    ]
)

# Portfolio summary
summary = result.get("portfolio_summary", {})
print(f"Total annual fees: ${summary.get('total_annual_fees', 0)}")
print(f"Net value: ${summary.get('net_value', 0)}")

# Per-card breakdown with verdicts
for card in result.get("card_details", []):
    name = card.get("card_name", "Unknown")
    fee = card.get("annual_fee", 0)
    net = card.get("net_value", 0)
    verdict = card.get("verdict", "")
    print(f"\n  {name}: ${fee} fee, net value ${net}/year — {verdict}")

# With spending data for better accuracy
result_detailed = client.analyze_portfolio(
    cards=[
        {"card_name": "Chase Sapphire Reserve"},
        {"card_name": "Amex Gold Card"},
    ],
    spending={
        "dining": 600,
        "travel": 400,
        "groceries": 500,
        "gas": 150,
    },
)

print("\n--- With spending data ---")
for card in result_detailed.get("card_details", []):
    print(f"  {card.get('card_name')}: net value ${card.get('net_value', 0)}/year")
