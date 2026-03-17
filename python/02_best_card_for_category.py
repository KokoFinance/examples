"""
Find the best credit card for a spending category.

No portfolio needed — just tell us the category and get market recommendations.
Categories: dining, travel, groceries, gas, online_shopping, entertainment, general
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# What's the best card for dining? (Mode B — market search, no portfolio)
result = client.recommend_card(category="dining")

recs = result.get("recommendations", [])
if recs:
    best = recs[0]
    print(f"Best card for dining: {best.get('card_name')}")
    print(f"  Annual fee: ${best.get('annual_fee', 0)}")
    print(f"  Net value: ${best.get('net_value', 0)}/year")

    # Show alternatives
    for alt in recs[1:]:
        print(f"  Alternative: {alt.get('card_name')} — ${alt.get('net_value', 0)}/year")
else:
    print("No recommendations found.")

# With portfolio — recommend from your own cards (Mode A)
result = client.recommend_card(
    category="dining",
    portfolio_card_names=["Chase Sapphire Preferred", "Amex Gold Card", "Citi Double Cash"],
)

rec = result.get("recommended_card")
if rec:
    print(f"\nFrom your portfolio, use: {rec.get('card_name')}")
    print(f"  Reason: {rec.get('reason', '')}")
