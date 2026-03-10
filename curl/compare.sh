#!/bin/bash
# Compare two credit cards — minimal curl example

curl -s -X POST https://kokofinance.net/api/v1/cards/compare \
  -H "X-API-Key: $KOKO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "card_names": ["Chase Sapphire Preferred", "Amex Gold Card"]
  }' | python3 -m json.tool
