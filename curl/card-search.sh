#!/bin/bash
# Search for credit cards with structured filters
# Returns ranked results based on spending alignment, fee value, and sign-on bonus

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"

curl -s -X POST "https://kokofinance.net/api/v1/cards/search" \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "card_type": "travel",
    "max_annual_fee": 300,
    "spending": {"dining": 500, "travel": 400, "groceries": 300},
    "credit_tier": "excellent",
    "max_results": 5
  }' | python3 -m json.tool
