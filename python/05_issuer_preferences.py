"""
Issuer preference weighting — the credit union angle.

If you're a card issuer (bank, credit union, fintech), you can boost your own
card products in recommendations. The API applies a configurable weight to
sort results in your favor when the math is close.

This is the core value prop for institutional customers.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Without issuer preferences — neutral analysis
neutral = client.analyze_portfolio(
    cards=[
        {"card_name": "Chase Sapphire Preferred"},
        {"card_name": "Amex Gold Card"},
        {"card_name": "Capital One Venture X"},
    ],
    spending={"dining": 500, "travel": 400, "groceries": 300},
)

print("Neutral portfolio analysis:")
for card in neutral.get("card_details", []):
    print(f"  {card.get('name')}: {card.get('verdict')} — {card.get('decision_reason', '')}")

# With issuer preferences — boost Chase cards
biased = client.analyze_portfolio(
    cards=[
        {"card_name": "Chase Sapphire Preferred"},
        {"card_name": "Amex Gold Card"},
        {"card_name": "Capital One Venture X"},
    ],
    spending={"dining": 500, "travel": 400, "groceries": 300},
    issuer_preferences=[
        {"issuer": "Chase", "weight": 1.5},   # 50% boost to Chase
    ],
)

print("\nWith Chase preference (1.5x weight):")
for card in biased.get("card_details", []):
    print(f"  {card.get('name')}: {card.get('verdict')} — {card.get('decision_reason', '')}")

# Compare summaries
neutral_summary = neutral.get("portfolio_summary", {})
biased_summary = biased.get("portfolio_summary", {})
print(f"\nNeutral net value: ${neutral_summary.get('net_value', 0)}/year")
print(f"With Chase boost:  ${biased_summary.get('net_value', 0)}/year")
