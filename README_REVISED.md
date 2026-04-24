# Koko Finance API — Examples

[![PyPI version](https://img.shields.io/pypi/v/koko-finance)](https://pypi.org/project/koko-finance/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![API Status](https://img.shields.io/badge/API-Live-green)](https://kokofinance.net/api/v1/docs)

**The only credit card API that calculates net economic value instead of regurgitating reward tables.**

Stop building reward logic from scratch. Koko models real economics:
- **Expected rewards** based on actual spend patterns
- **Annual fee break-even** calculations
- **Net value per card** (rewards minus fees)
- **Renewal decisions** (keep, downgrade, or replace)

No spending data required. No portfolio setup. Just card names → economic value.

---

## Built For

- **Neobanks** - Add intelligent card recommendations to your app
- **Budgeting apps** - Help users optimize rewards and minimize fees
- **Financial advisors** - Compare client card portfolios programmatically
- **AI agents** - Decision backend for credit card intelligence (via MCP)

---

## Why Koko?

| Feature | Koko | NerdWallet | Static Tables |
|---------|:----:|:----------:|:-------------:|
| Net economic value calculations | ✅ | ❌ | ❌ |
| Break-even analysis | ✅ | ❌ | ❌ |
| Programmatic API access | ✅ | ❌ | N/A |
| MCP for AI agents | ✅ | ❌ | ❌ |
| Real-time data (150+ cards) | ✅ | ⚠️ Editorial | ⚠️ Outdated |
| Free tier (2,000 calls/mo) | ✅ | N/A | N/A |

**The difference:** Editorial sites rank cards subjectively. Koko computes actual value using break-even formulas and reward modeling.

---

## Get Started (30 seconds)

### 1. Get a free API key

Sign up at [kokofinance.net/dashboard.html](https://kokofinance.net/dashboard.html)

### 2. Install the Python SDK

```bash
pip install koko-finance
```

### 3. Make your first call

```python
import os
from koko_finance import KokoClient

client = KokoClient(api_key=os.environ["KOKO_API_KEY"])

# Compare two cards (fast, <100ms)
result = client.compare_cards(
    cards=["Chase Sapphire Preferred", "Amex Gold Card"]
)

for card in result["comparison_table"]:
    print(f"{card['card_name']}: ${card['net_value']}/year")
```

**Output:**
```
Chase Sapphire Preferred: $289/year
Amex Gold Card: $576/year

Why Amex wins:
- Higher grocery/dining multipliers (4x vs 3x)
- $360 annual credits ($240 Uber + $120 dining)
- Better effective value despite higher fee
```

**More examples:**

```python
# Best card for a spending category
result = client.recommend_card(category="dining")
print(result["recommendations"][0]["card_name"])
# → "Amex Gold Card"

# Should you renew this card?
result = client.check_renewal(card={"card_name": "Chase Sapphire Reserve"})
print(result["verdict"])
# → "RENEW" (or "DOWNGRADE" or "CANCEL_AND_REPLACE")
print(result["reasoning"])
# → "Benefits ($550) exceed annual fee ($550). Break-even with minimal spend."
```

---

## Examples Repository

### Python SDK

| Example | What It Does | Complexity |
|---------|-------------|------------|
| [01_compare_cards.py](python/01_compare_cards.py) | Compare two cards side-by-side with net value | Beginner |
| [02_best_card_for_category.py](python/02_best_card_for_category.py) | Find the best card for dining, travel, groceries, etc. | Beginner |
| [03_analyze_portfolio.py](python/03_analyze_portfolio.py) | Portfolio value breakdown across multiple cards | Beginner |
| [04_renewal_check.py](python/04_renewal_check.py) | Should you keep this card or cancel? | Beginner |
| [05_issuer_preferences.py](python/05_issuer_preferences.py) | Boost specific card issuers in recommendation results | Intermediate |
| [06_benefit_categories.py](python/06_benefit_categories.py) | List benefit categories and use selections for accurate value | Intermediate |
| [07_merchant_which_card.py](python/07_merchant_which_card.py) | Best card at a specific merchant (auto-detects category) | Beginner |
| [08_merchant_benefits.py](python/08_merchant_benefits.py) | Check merchant-specific credits (e.g. Saks → Amex credit) | Beginner |
| [09_card_benefits.py](python/09_card_benefits.py) | List all credits/benefits for a card with values and schedules | Beginner |
| [10_card_terms.py](python/10_card_terms.py) | Get Schumer Box data — APR, penalties, fees | Beginner |
| [11_card_search.py](python/11_card_search.py) | Search cards with structured filters (type, fee, spending) | Intermediate |
| [12_card_history.py](python/12_card_history.py) | Track card data changes and points program trends | Intermediate |

### curl (no SDK needed)

| Example | What It Does |
|---------|-------------|
| [compare.sh](curl/compare.sh) | Compare cards via raw HTTP |
| [recommend.sh](curl/recommend.sh) | Get card recommendations |
| [renewal.sh](curl/renewal.sh) | Check card renewal value |
| [merchant-which-card.sh](curl/merchant-which-card.sh) | Best card at a specific merchant |
| [merchant-benefits.sh](curl/merchant-benefits.sh) | Check merchant-specific credits |
| [card-benefits.sh](curl/card-benefits.sh) | List all benefits for a card |
| [card-terms.sh](curl/card-terms.sh) | Get Schumer Box data (APR, penalties, fees) |
| [card-search.sh](curl/card-search.sh) | Search cards with structured filters |
| [card-history.sh](curl/card-history.sh) | Track card data changes over time |
| [points-programs.sh](curl/points-programs.sh) | Points program reference data and valuations |

### MCP Server (for Claude Desktop / AI agents)

Turn Claude into a credit card advisor. Connect the Koko MCP server to get card intelligence inside conversational AI.

| Guide | What It Covers |
|-------|---------------|
| [Claude Desktop Setup](mcp/claude-desktop-setup.md) | Connect Koko MCP to Claude in 2 minutes |
| [Sample Prompts](mcp/sample-prompts.md) | Example conversations with the MCP server |

**Example prompt:**
> "I spend $800/month on dining and $1,200/month on groceries. Which credit card should I get?"

Claude uses Koko's API to calculate net value and recommend the optimal card.

### Agentic Examples

Build AI agents that make credit card decisions:

| Example | What It Does |
|---------|-------------|
| [card_advisor_agent.py](agents/card_advisor_agent.py) | AI credit card advisor using OpenAI + Koko |
| [Agent README](agents/README.md) | How the agentic pattern works |

---

## Two Ways to Access

| Method | Best For | Docs |
|--------|----------|------|
| **REST API** | Apps, backends, scripts | [API Docs](https://kokofinance.net/developers.html) / [Swagger UI](https://kokofinance.net/api/v1/docs) |
| **MCP Server** | Claude Desktop, AI agents | [MCP Setup](mcp/claude-desktop-setup.md) |

Both use the same calculation engine. Same data, same intelligence, same structured output.

---

## What You're Actually Getting

**This isn't a static card database.** Koko models economic outcomes:

✅ **Net value calculations** - Rewards earned minus annual fees (not just "4x points")
✅ **Break-even analysis** - How much spend needed to justify the annual fee
✅ **Renewal recommendations** - Keep, downgrade, or replace based on actual value
✅ **Category optimization** - Which card maximizes returns for specific spending
✅ **Portfolio analysis** - Total value across all cards you own
✅ **Merchant intelligence** - Best card at a specific merchant + merchant-specific credits
✅ **Schumer Box data** - Purchase APR, penalty APR, late fees, cash advance fees
✅ **Card search** - Structured search with filters (type, fee, spending, credit tier)
✅ **Data history** - Track fee changes, benefit updates, and program valuations over time

**Example:**
Most sites say "Amex Gold earns 4x on dining."
Koko says "Amex Gold nets you $576/year on your spend profile vs $289 with Chase Sapphire Preferred."

That's the difference between marketing and math.

---

## See It In Action

**Question:** "Which card should I use for $1,200/month dining spend?"

**Koko's Response:**
```json
{
  "recommendation": {
    "card_name": "Amex Gold Card",
    "annual_net_value": 576,
    "calculation": {
      "annual_rewards": 576,
      "annual_fee": 250,
      "credits_utilized": 250,
      "net_value": 576
    }
  },
  "reasoning": "4x points on dining ($14,400/year spend) = $576 rewards. Annual credits ($240 Uber + $120 dining) offset $250 fee entirely. Net value: $576/year.",
  "alternatives": [
    {
      "card_name": "Chase Sapphire Preferred",
      "net_value": 289,
      "why_not": "Lower dining multiplier (3x vs 4x) and fewer credits"
    }
  ]
}
```

---

## Free Tier

- **2,000 API calls/month** (REST + MCP combined)
- **All endpoints included** (compare, recommend, renewal, portfolio)
- **No credit card required**
- **[Get your API key →](https://kokofinance.net/dashboard.html)**

Upgrade to Pro for 10,000 calls/month ($29/mo). [See pricing](https://kokofinance.net/pricing.html).

---

## Links

- **Documentation**: [kokofinance.net/developers.html](https://kokofinance.net/developers.html)
- **Interactive API Explorer**: [kokofinance.net/api/v1/docs](https://kokofinance.net/api/v1/docs) (Swagger UI)
- **Python SDK**: [pypi.org/project/koko-finance](https://pypi.org/project/koko-finance/)
- **MCP Server**: [kokofinance.net/mcp/](https://kokofinance.net/mcp/)
- **Card Studio** (consumer tools): [kokofinance.net/card-studio.html](https://kokofinance.net/card-studio.html)

---

## Contributing

Found a bug? Have a feature request? [Open an issue](https://github.com/KokoFinance/examples/issues).

Want to add an example? PRs welcome!

---

## License

MIT - See [LICENSE](LICENSE) for details.

---

**Questions?** Email [support@kokofinance.net](mailto:support@kokofinance.net) or open an issue.
