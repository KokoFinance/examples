"""
Compare two credit cards side-by-side.

The simplest Koko API call — just two card names, structured comparison back.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

result = client.compare_cards(
    cards=["Chase Sapphire Preferred", "Amex Gold Card"]
)

# Print the comparison
for card in result.get("comparison_table", []):
    print(f"\n--- {card['card_name']} ---")
    print(f"  Annual fee: ${card.get('annual_fee', 'N/A')}")
    print(f"  Net value:  ${card.get('net_value', 'N/A')}/year")
    print(f"  Best for:   {card.get('best_for', 'N/A')}")

winner = result.get("winner", {})
print(f"\nWinner: {winner.get('card_name', 'N/A')} — {winner.get('reason', '')}")
