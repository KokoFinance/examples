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
| `compare_cards` | Side-by-side card comparison |
| `recommend_card` | Best card for a spending category |
| `analyze_portfolio` | Full portfolio value analysis |
| `renewal_check` | Should you renew this card? |
| `card_lookup` | Look up a specific card's details |
| `search_cards` | Search cards by criteria |
| `get_categories` | List available spending categories |

## Available MCP Prompts

| Prompt | Use Case |
|--------|----------|
| `portfolio-review` | Guided portfolio analysis |
| `which-card` | Find the right card for a purchase |
| `new-card-finder` | Discover new card options |

## Links

- MCP endpoint: `https://kokofinance.net/mcp/`
- Full docs: [kokofinance.net/developers.html](https://kokofinance.net/developers.html)
- REST API (alternative): [kokofinance.net/api/v1/docs](https://kokofinance.net/api/v1/docs)
