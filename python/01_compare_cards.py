"""
Compare two credit cards side-by-side.

The simplest Koko API call — just two card names, structured comparison back.
Fast endpoint returns deterministic data in <100ms.
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
    print(f"  Annual fee:    ${card.get('annual_fee', 'N/A')}")
    print(f"  Net value:     ${card.get('net_value', 'N/A')}/year")
    print(f"  Total rewards: ${card.get('total_rewards', 'N/A')}/year")
    print(f"  Break-even:    {card.get('break_even', {}).get('status', 'N/A')}")
