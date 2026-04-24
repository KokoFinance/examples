#!/bin/bash
# List all points programs or get details for a specific program

API_KEY="${KOKO_API_KEY:-koko_your_key_here}"

# List all programs
echo "=== All Programs ==="
curl -s -X GET "https://kokofinance.net/api/v1/points/programs" \
  -H "X-API-Key: $API_KEY" | python3 -m json.tool

# Get details for Chase Ultimate Rewards (including transfer partners)
echo ""
echo "=== Chase Ultimate Rewards ==="
curl -s -X GET "https://kokofinance.net/api/v1/points/programs/chase_ur" \
  -H "X-API-Key: $API_KEY" | python3 -m json.tool
