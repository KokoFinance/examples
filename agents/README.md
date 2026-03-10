# Build an AI Credit Card Advisor

A minimal agentic example showing how to combine the Koko Finance API with an LLM to create an interactive credit card advisor.

## How It Works

1. User asks a natural language question ("Is the Amex Platinum worth it?")
2. The LLM decides which Koko API tool to call
3. Koko returns structured card data (fees, rewards, comparisons)
4. The LLM synthesizes the data into a helpful answer

## Run It

```bash
pip install koko-finance openai
export KOKO_API_KEY=your-koko-key
export OPENAI_API_KEY=your-openai-key

python card_advisor_agent.py
```

## Example Session

```
You: Should I keep my Chase Sapphire Reserve or switch to the Amex Gold?

Advisor: Based on the comparison, here's the breakdown:
- Chase Sapphire Reserve ($550/year): Strong travel benefits, 3x on dining/travel, $300 travel credit
- Amex Gold ($250/year): 4x on dining and groceries, $120 dining credit, $120 Uber credit
...
```

## Adapt It

The pattern works with any LLM that supports tool calling:
- **OpenAI** (GPT-4o, GPT-4o-mini) — shown in this example
- **Anthropic** (Claude) — use the Claude SDK's tool_use feature
- **MCP** — skip the wrapper entirely, connect Claude Desktop to `https://kokofinance.net/mcp/`

The Koko API handles all the card intelligence. Your agent just needs to route questions to the right endpoint.
