"""
Example 10: Get Schumer Box data (APR, penalties, fees) for a card

The card terms endpoint returns structured APR, penalty, and fee
data extracted from each card's Schumer Box disclosure.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# First, find the card_id via search
search = client.search_cards(issuer="Chase", max_annual_fee=100, max_results=1)
card = search["recommendations"][0]
card_id = card["card_id"]
print(f"Looking up terms for: {card['card_name']} (id={card_id})\n")

# Get Schumer Box terms
terms = client.get_card_terms(card_id)

print(f"Card: {terms['card_name']}")
print(f"Issuer: {terms['issuer']}")
print(f"Purchase APR: {terms['purchase_apr']}")
print(f"Cash Advance APR: {terms['cash_advance_apr']}")
print(f"Penalty APR: {terms['penalty_apr'] or 'N/A'}")
print(f"Balance Transfer APR: {terms['balance_transfer_apr'] or 'N/A'}")
print(f"Late Fee: {terms['late_fee'] or 'N/A'}")
print(f"Returned Payment Fee: {terms['returned_payment_fee'] or 'N/A'}")
print(f"Cash Advance Fee: {terms['cash_advance_fee'] or 'N/A'}")
print(f"Promotional APR: {terms['promotional_apr'] or 'None'}")
if terms.get("promo_apr_months"):
    print(f"Promo Period: {terms['promo_apr_months']} months")
print(f"Last Updated: {terms['last_extracted_at']}")
