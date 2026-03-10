"""
Simple Credit Card Advisor Agent

A minimal example showing how to build an AI-powered credit card advisor
using the Koko Finance API. This agent takes natural language questions
and routes them to the appropriate API endpoint.

Requirements:
    pip install koko-finance openai

Usage:
    export KOKO_API_KEY=your-koko-key
    export OPENAI_API_KEY=your-openai-key
    python card_advisor_agent.py
"""

import os
import json
from koko_finance import KokoClient
from openai import OpenAI

koko = KokoClient(api_key=os.environ["KOKO_API_KEY"])
llm = OpenAI()

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "compare_cards",
            "description": "Compare two or three credit cards side-by-side",
            "parameters": {
                "type": "object",
                "properties": {
                    "cards": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Card names to compare (2-3)",
                    }
                },
                "required": ["cards"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "recommend_card",
            "description": "Find the best credit card for a spending category",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Spending category: dining, travel, groceries, gas, online_shopping, general",
                    }
                },
                "required": ["category"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_renewal",
            "description": "Check if a credit card is worth renewing at annual fee time",
            "parameters": {
                "type": "object",
                "properties": {
                    "card_name": {
                        "type": "string",
                        "description": "Name of the card to check",
                    }
                },
                "required": ["card_name"],
            },
        },
    },
]

SYSTEM_PROMPT = """You are a helpful credit card advisor. You help users compare cards,
find the best card for their needs, and decide whether to keep or cancel cards.

Use the available tools to look up real card data. Give concise, actionable advice."""


def handle_tool_call(name, args):
    """Route tool calls to the Koko Finance API."""
    if name == "compare_cards":
        return koko.compare_cards(cards=args["cards"])
    elif name == "recommend_card":
        return koko.recommend_card(category=args["category"])
    elif name == "check_renewal":
        return koko.check_renewal(card={"card_name": args["card_name"]})
    return {"error": f"Unknown tool: {name}"}


def chat(user_message, history):
    """Send a message and handle tool calls in a loop."""
    history.append({"role": "user", "content": user_message})

    while True:
        response = llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            tools=TOOLS,
        )

        message = response.choices[0].message

        if message.tool_calls:
            history.append(message)
            for call in message.tool_calls:
                args = json.loads(call.function.arguments)
                result = handle_tool_call(call.function.name, args)
                history.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(result),
                })
        else:
            history.append({"role": "assistant", "content": message.content})
            return message.content


def main():
    print("Credit Card Advisor (powered by Koko Finance API)")
    print("Ask me about credit cards. Type 'quit' to exit.\n")

    history = []
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if not user_input:
            continue

        response = chat(user_input, history)
        print(f"\nAdvisor: {response}\n")


if __name__ == "__main__":
    main()
