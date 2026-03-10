#!/bin/bash
# Get the best credit card for a spending category

curl -s -X POST https://kokofinance.net/api/v1/cards/recommend \
  -H "X-API-Key: $KOKO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "category": "dining"
  }' | python3 -m json.tool
