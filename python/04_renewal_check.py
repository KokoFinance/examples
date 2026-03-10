"""
Check if a credit card is worth renewing.

Annual fee coming up? Get a RENEW, DOWNGRADE, or CANCEL_AND_REPLACE verdict
with alternatives and retention tips.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

result = client.check_renewal(
    card={"card_name": "Chase Sapphire Reserve"}
)

print(f"Card: {result.get('card_name')}")
print(f"Annual fee: ${result.get('annual_fee', 0)}")
print(f"Verdict: {result.get('verdict')}")
print(f"Year 2+ net value: ${result.get('year2_net_value', 0)}")

# Downgrade options (same issuer, lower fee)
for option in result.get("downgrade_options", []):
    print(f"\n  Downgrade to: {option.get('card_name')} (${option.get('annual_fee', 0)}/year)")

# Replacement options (different issuer)
for option in result.get("replacement_options", []):
    print(f"\n  Replace with: {option.get('card_name')} — est. value ${option.get('estimated_net_value', 0)}/year")

# AI-generated explanation
if result.get("ai_explanation"):
    print(f"\nAnalysis: {result['ai_explanation']}")
