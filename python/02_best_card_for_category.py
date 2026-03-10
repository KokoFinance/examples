"""
Find the best credit card for a spending category.

No portfolio needed — just tell us the category and get market recommendations.
Categories: dining, travel, groceries, gas, online_shopping, entertainment, general
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# What's the best card for dining?
result = client.recommend_card(category="dining")

print(f"Best card for dining: {result.get('recommended_card', {}).get('card_name', 'N/A')}")
print(f"Why: {result.get('recommended_card', {}).get('reason', '')}")

# Show alternatives
for alt in result.get("alternatives", []):
    print(f"  Alternative: {alt.get('card_name')} — {alt.get('reason', '')}")
