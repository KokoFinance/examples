"""
Analyze a credit card portfolio.

Pass your cards (just names are enough) and get a full value breakdown.
Add spending data and benefit selections for more accurate results.
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

# With benefit selections (only benefits you use count at 100%)
# Use client.get_benefit_categories() to discover valid keys
result_with_benefits = client.analyze_portfolio(
    cards=[
        {"card_name": "American Express Platinum Card"},
    ],
    spending={"dining": 500, "travel": 300},
    benefit_selections=["uber", "airline_fee", "digital_entertainment", "saks"],
)

print("\n--- With benefit selections ---")
for card in result_with_benefits.get("card_details", []):
    print(f"  {card.get('card_name')}: net value ${card.get('net_value', 0)}/year — {card.get('verdict', '')}")

# With points balances for redemption-aware analysis
result_with_points = client.analyze_portfolio(
    cards=[
        {"card_name": "Chase Sapphire Reserve"},
        {"card_name": "Amex Gold Card"},
    ],
    point_balances=[
        {"program": "chase_ur", "balance": 80000},
        {"program": "amex_mr", "balance": 150000},
    ],
)

print("\n--- With points balances ---")
summary = result_with_points.get("portfolio_summary", {})
print(f"Net value: ${summary.get('net_value', 0)}")
for card in result_with_points.get("card_details", []):
    print(f"  {card.get('card_name')}: {card.get('verdict', '')}")
