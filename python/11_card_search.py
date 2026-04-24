"""
Example 11: Search for credit cards with structured filters

The search endpoint uses deterministic ranking based on spending
alignment, fee value, and sign-on bonus. Fast (<100ms).
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Search for travel cards under $300/year
result = client.search_cards(
    card_type="travel",
    max_annual_fee=300,
    spending={"dining": 500, "travel": 400, "groceries": 300},
    credit_tier="excellent",
    max_results=5,
)

print(f"Found {result['total_found']} matching cards")
print(f"Filters: {result['filters_applied']}\n")

for i, card in enumerate(result["recommendations"], 1):
    print(f"{i}. {card['card_name']}")
    print(f"   Issuer: {card['issuer']} | Fee: ${card['annual_fee']} | Score: {card['match_score']}")
    print(f"   Sign-on Bonus: {card['sign_on_bonus']:,} points")
    print(f"   {card['reasoning']}")
    print()
