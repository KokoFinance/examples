#!/bin/bash
# Check if a card is worth renewing at annual fee time

curl -s -X POST https://kokofinance.net/api/v1/card/renewal-check \
  -H "X-API-Key: $KOKO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "card_name": "Chase Sapphire Reserve"
  }' | python3 -m json.tool
