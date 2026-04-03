"""
Example 9: Get all benefits for a specific card

The card_benefits endpoint returns every credit and benefit
for a card, with structured data including value, frequency,
schedule, conditions, and rewards multipliers.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Get full benefit breakdown for Amex Platinum
result = client.card_benefits(card="Amex Platinum")

# SDK unwraps the APIResponse envelope — result IS the data dict
print(f"Card: {result['card']}")
print(f"Issuer: {result['issuer']}")
print(f"Annual Fee: ${result['annual_fee']}")
print(f"Total Credit Value: ${result['total_credit_value']}")
print(f"Points Program: {result['points_program']}")
print(f"Portal CPP: {result['portal_cpp']}")
print()

# List all credits
print("Credits & Benefits:")
for c in result["credits"]:
    line = f"  {c['name']}: ${c['value']}"
    if c.get("frequency"):
        line += f" ({c['frequency']})"
    print(line)
    if c.get("schedule"):
        print(f"    Schedule: {c['schedule']}")

# Show multipliers
print(f"\nRewards Multipliers:")
for cat, mult in result["rewards_multipliers"].items():
    print(f"  {cat}: {mult}x")
