"""
Example 8: Check card credits at a merchant

The merchant_benefits endpoint checks which of your cards have
credits at a specific merchant (e.g. Saks, Uber, Disney+) and
also tells you which card earns the most there.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Check for credits at Saks Fifth Avenue
result = client.merchant_benefits(
    merchant="Saks Fifth Avenue",
    portfolio=["Amex Platinum", "Chase Sapphire Reserve"],
)

# SDK unwraps the APIResponse envelope — result IS the data dict

# Show matching credits
if result["matching_benefits"]:
    print("Credits found:")
    for b in result["matching_benefits"]:
        print(f"  {b['card']}: {b['name']} - ${b['value']}")
        if b.get("frequency"):
            print(f"    Frequency: {b['frequency']}")
        if b.get("schedule"):
            print(f"    Schedule: {b['schedule']}")
        print(f"    {b['note']}")
else:
    print("No credits found at this merchant.")

# Show earning recommendation
if result.get("earning_recommendation"):
    rec = result["earning_recommendation"]
    print(f"\nEarning tip: {rec['note']}")
