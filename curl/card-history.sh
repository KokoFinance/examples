#!/bin/bash
# Get card data change history (fee changes, benefit updates, etc.)
# Use /cards/{id}/history for one card, or /cards/changes for bulk

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"

# Option 1: Single card history
echo "=== Card #5 history ==="
curl -s -X GET "https://kokofinance.net/api/v1/cards/5/history?since=2026-01-01" \
  -H "X-API-Key: $API_KEY" | python3 -m json.tool

# Option 2: Bulk changes (all cards since a date)
echo ""
echo "=== All annual_fee changes since 2026-01-01 ==="
curl -s -X GET "https://kokofinance.net/api/v1/cards/changes?since=2026-01-01&fields=annual_fee" \
  -H "X-API-Key: $API_KEY" | python3 -m json.tool
