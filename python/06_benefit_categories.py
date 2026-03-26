"""
Discover valid benefit keys and use them in analysis.

The benefit_selections parameter lets you specify which card benefits
you actually use. Selected benefits count at 100%; unselected at 0%.
This gives accurate net-value calculations instead of the default 50% estimate.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Discover all valid benefit keys (no auth required)
categories = client.get_benefit_categories()

print("Benefit categories:")
for cat in categories["categories"]:
    print(f"  {cat['label']}: {', '.join(cat['keys'])}")

print(f"\nAll valid keys: {categories['all_keys']}")

# Use benefit selections in portfolio analysis
result = client.analyze_portfolio(
    cards=[
        {"card_name": "American Express Platinum Card"},
    ],
    spending={"dining": 500, "travel": 300},
    benefit_selections=["uber", "airline_fee", "digital_entertainment", "saks"],
)

for card in result.get("card_details", []):
    print(f"\n{card.get('card_name')}:")
    print(f"  Annual fee: ${card.get('annual_fee', 0)}")
    print(f"  Net value: ${card.get('net_value', 0)}/year")
    print(f"  Verdict: {card.get('verdict', '')}")

# Use benefit selections in renewal check
renewal = client.check_renewal(
    card={"card_name": "American Express Platinum Card"},
    spending={"dining": 500, "travel": 300},
    benefit_selections=["uber", "airline_fee", "digital_entertainment", "saks"],
)

print(f"\nRenewal verdict: {renewal.get('verdict')}")
