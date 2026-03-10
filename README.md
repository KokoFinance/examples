# Koko Finance API — Examples

Credit card intelligence in 5 minutes. Compare cards, get recommendations, analyze portfolios, and check renewal value — all via a simple API.

## Get Started

### 1. Get a free API key

Sign up at [kokofinance.net/dashboard.html](https://kokofinance.net/dashboard.html) — takes 30 seconds.

### 2. Install the Python SDK

```bash
pip install koko-finance
```

### 3. Make your first call

```python
import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Compare two cards
result = client.compare_cards(
    cards=["Chase Sapphire Preferred", "Amex Gold Card"]
)
print(result["winner"]["card_name"])

# Best card for dining
result = client.recommend_card(category="dining")
print(result["recommended_card"]["card_name"])

# Is this card worth renewing?
result = client.check_renewal(card={"card_name": "Chase Sapphire Reserve"})
print(result["verdict"])  # RENEW, DOWNGRADE, or CANCEL_AND_REPLACE
```

No spending data required. No portfolio setup. Just card names.

## Examples

### Python SDK

| Example | What It Does | Complexity |
|---------|-------------|------------|
| [01_compare_cards.py](python/01_compare_cards.py) | Compare two cards side-by-side | Beginner |
| [02_best_card_for_category.py](python/02_best_card_for_category.py) | Find the best card for dining, travel, etc. | Beginner |
| [03_analyze_portfolio.py](python/03_analyze_portfolio.py) | Portfolio value breakdown | Beginner |
| [04_renewal_check.py](python/04_renewal_check.py) | Should you keep this card? | Beginner |
| [05_issuer_preferences.py](python/05_issuer_preferences.py) | Boost specific card issuers in results | Intermediate |

### curl (no SDK needed)

| Example | What It Does |
|---------|-------------|
| [compare.sh](curl/compare.sh) | Compare cards via raw HTTP |
| [recommend.sh](curl/recommend.sh) | Get card recommendations |
| [renewal.sh](curl/renewal.sh) | Check card renewal value |

### MCP Server (for Claude Desktop / AI agents)

| Guide | What It Covers |
|-------|---------------|
| [Claude Desktop Setup](mcp/claude-desktop-setup.md) | Connect Koko MCP to Claude in 2 minutes |
| [Sample Prompts](mcp/sample-prompts.md) | Example conversations with the MCP server |

### Agentic

| Example | What It Does |
|---------|-------------|
| [card_advisor_agent.py](agents/card_advisor_agent.py) | Build an AI credit card advisor with OpenAI + Koko |
| [Agent README](agents/README.md) | How the agentic pattern works |

## Two Ways to Access

| Method | Best For | Docs |
|--------|----------|------|
| **REST API** | Apps, backends, scripts | [API Docs](https://kokofinance.net/developers.html) / [Swagger UI](https://kokofinance.net/api/v1/docs) |
| **MCP Server** | Claude Desktop, AI agents | [MCP Setup](mcp/claude-desktop-setup.md) |

Both use the same underlying intelligence. Same data, same calculations, same structured output.

## Free Tier

- 2,000 calls/month (REST + MCP combined)
- All endpoints included
- No credit card required
- [Get your API key](https://kokofinance.net/dashboard.html)

## Links

- **Docs**: [kokofinance.net/developers.html](https://kokofinance.net/developers.html)
- **Swagger UI**: [kokofinance.net/api/v1/docs](https://kokofinance.net/api/v1/docs)
- **Python SDK**: [pypi.org/project/koko-finance](https://pypi.org/project/koko-finance/)
- **MCP Server**: [kokofinance.net/mcp/](https://kokofinance.net/mcp/)
- **Card Studio** (consumer tools): [kokofinance.net/card-studio.html](https://kokofinance.net/card-studio.html)
