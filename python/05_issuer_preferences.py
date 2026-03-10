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

# Without issuer preferences — neutral recommendations
neutral = client.recommend_card(category="travel")
print("Neutral recommendation:")
print(f"  {neutral.get('recommended_card', {}).get('card_name')}")

# With issuer preferences — boost Chase cards
biased = client.recommend_card(
    category="travel",
    issuer_preferences=[
        {"issuer": "Chase", "weight": 1.5},   # 50% boost to Chase
    ],
)
print("\nWith Chase preference (1.5x weight):")
print(f"  {biased.get('recommended_card', {}).get('card_name')}")

# Works with portfolio analysis too
result = client.analyze_portfolio(
    cards=[{"card_name": "Chase Sapphire Preferred"}],
    issuer_preferences=[
        {"issuer": "Chase", "weight": 1.3},
    ],
)

# Replacement suggestions will favor Chase products
for rec in result.get("recommendations", []):
    print(f"\n  Suggestion: {rec.get('card_name', '')} — {rec.get('reason', '')}")
