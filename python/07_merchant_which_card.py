"""
Example 7: Which card to use at a specific merchant

The which_card_at_merchant endpoint resolves a merchant name to a
spending category and ranks your portfolio cards by reward value.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Find the best card for a Starbucks purchase
result = client.which_card_at_merchant(
    merchant="Starbucks",
    amount=35,
    portfolio=["Chase Sapphire Reserve", "Amex Gold", "Citi Double Cash"],
)

# SDK unwraps the APIResponse envelope — result IS the data dict
print(f"Merchant: Starbucks")
print(f"Category detected: {result['category_detected']} (method: {result['category_method']})")
print(f"Recommended card: {result['recommended_card']}")
print(f"Reason: {result['reason']}")
print()

# Show all card earnings
for card in result["earnings_comparison"]:
    print(f"  {card['card']}: {card['multiplier']} -> {card['estimated_value']}")
