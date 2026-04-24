"""
Example 12: Track card data changes over time

The history endpoints let you monitor fee changes, benefit updates,
and other card data modifications from weekly batch jobs.
"""

import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Get all annual fee changes since start of year
print("=== Annual Fee Changes (2026) ===\n")
changes = client.get_card_changes(since="2026-01-01", fields="annual_fee")
print(f"Total changes: {changes['count']}")
for c in changes["changes"][:5]:  # Show first 5
    print(f"  Card #{c['card_id']}: {c['old_value']} -> {c['new_value']} ({c['detected_at'][:10]})")

# Get history for a specific card
print("\n=== Card #5 Full History ===\n")
history = client.get_card_history(card_id=5, since="2026-01-01")
print(f"Changes found: {history['count']}")
for c in history["changes"][:5]:
    print(f"  {c['field']}: {c['old_value']} -> {c['new_value']}")

# Check points program valuation trends
print("\n=== Chase UR Valuation History ===\n")
program = client.get_program_history("chase_ur", since="2026-01-01")
print(f"Changes found: {program['count']}")
for c in program["changes"][:5]:
    print(f"  {c['field']}: {c['old_value']} -> {c['new_value']}")
