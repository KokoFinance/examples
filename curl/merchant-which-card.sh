#!/bin/bash
# Which card to use at a specific merchant
# Auto-detects spending category from merchant name

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"

curl -s -X POST https://kokofinance.net/api/v1/which-card-at-merchant \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "merchant": "Starbucks",
    "amount": 35,
    "portfolio": [
      "Chase Sapphire Reserve",
      "Amex Gold",
      "Citi Double Cash"
    ]
  }' | python3 -m json.tool
