# Connect Koko Finance MCP Server to Claude Desktop

## Quick Setup

Add this to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "koko-finance": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-remote@latest", "https://kokofinance.net/mcp/"]
    }
  }
}
```

Restart Claude Desktop. You'll be prompted to authorize via Google OAuth on first use.

## What You Can Do

Once connected, you can ask Claude things like:

- "Compare the Chase Sapphire Reserve and Amex Gold Card"
- "What's the best credit card for dining?"
- "Analyze my portfolio: I have a Chase Sapphire Preferred and Citi Double Cash"
- "Is the Amex Platinum worth renewing?"
- "Recommend a travel card with no annual fee"

## Available MCP Tools

| Tool | What It Does |
|------|-------------|
| `search_credit_cards` | Search cards by natural language query (e.g., "best travel card under $200/year") |
| `compare_cards` | Side-by-side card comparison with net value and break-even |
| `get_card_details` | Look up a specific card's fees, rewards, benefits, and application URL |
| `calculate_card_value` | Calculate whether a card's rewards exceed its annual fee |
| `optimize_portfolio` | Full portfolio value analysis with per-card verdicts (KEEP/OPTIMIZE/CANCEL) |
| `recommend_card_for_category` | Best card for a spending category from your portfolio |
| `check_card_renewal` | Should you renew this card? Verdict + downgrade/replacement options |
| `create_mcp_session` | Create a session for multi-tool workflows |

## Available MCP Prompts

| Prompt | Use Case |
|--------|----------|
| `portfolio-review` | Guided portfolio analysis with optimization strategies |
| `which-card` | Find the right card from your wallet for a purchase |
| `new-card-finder` | Discover new card options based on spending and goals |
| `renewal-check` | Walk through a card renewal decision step by step |

## Claude Code Setup

```bash
claude mcp add --transport http koko-credit-cards https://kokofinance.net/mcp/
```

## Links

- MCP endpoint: `https://kokofinance.net/mcp/`
- Full docs: [kokofinance.net/developers.html](https://kokofinance.net/developers.html)
- REST API (alternative): [kokofinance.net/api/v1/docs](https://kokofinance.net/api/v1/docs)
