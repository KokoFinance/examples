#!/bin/bash
# Get Schumer Box data (APR, penalties, fees) for a card
# Requires card_id — get it from portfolio, search, or compare results

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"
CARD_ID="${1:-5}"  # Default: Chase Freedom Unlimited (id=5)

curl -s -X GET "https://kokofinance.net/api/v1/cards/${CARD_ID}/terms" \
  -H "X-API-Key: $API_KEY" | python3 -m json.tool
