#!/bin/bash
# Check if a card is worth renewing at annual fee time

# Basic renewal check
curl -s -X POST https://kokofinance.net/api/v1/card/renewal-check \
  -H "X-API-Key: $KOKO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "card_name": "Chase Sapphire Reserve"
  }' | python3 -m json.tool

# With spending and benefit selections (only selected benefits count at 100%)
# Discover valid keys: curl -s https://kokofinance.net/api/v1/benefit-categories | python3 -m json.tool
curl -s -X POST https://kokofinance.net/api/v1/card/renewal-check \
  -H "X-API-Key: $KOKO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "card_name": "Amex Platinum",
    "params": {
      "spending": {"dining": 400, "travel": 300, "groceries": 500}
    },
    "benefit_selections": ["uber", "airline_fee", "digital_entertainment"]
  }' | python3 -m json.tool
