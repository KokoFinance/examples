#!/bin/bash
# Get all credits and benefits for a specific card
# Returns structured data with value, frequency, schedule

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"

curl -s -X GET "https://kokofinance.net/api/v1/card-benefits?card=Amex%20Platinum" \
  -H "X-API-Key: $API_KEY" | python3 -m json.tool
