#!/bin/bash
# Check if any cards have credits at a merchant
# Also returns an earning recommendation

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"

curl -s -X POST https://kokofinance.net/api/v1/merchant-benefits \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "merchant": "Saks Fifth Avenue",
    "portfolio": [
      "Amex Platinum",
      "Chase Sapphire Reserve"
    ]
  }' | python3 -m json.tool
