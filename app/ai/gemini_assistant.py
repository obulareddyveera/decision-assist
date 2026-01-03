import os
from google import genai
from typing import Dict

MODEL_NAME = "models/gemini-flash-latest"

_client = None


def _get_client():
    global _client

    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError(
                "GOOGLE_API_KEY environment variable is not set")
        _client = genai.Client(api_key=api_key)

    return _client


async def generate_decision_explanation(
    application: Dict,
    decision: Dict
) -> str:
    """
    Gemini is used strictly as an ASSISTANT.
    It explains decisions, never makes them.
    """

    prompt = f"""
You are an AI assistant explaining a loan decision.

RULES:
- Do NOT approve or reject.
- Do NOT change the decision.
- Only explain the provided outcome.

Decision: {decision['decision']}
Reasons: {decision['reasons']}

Application:
Income: {application['annual_income_usd']}
Credit Score: {application['credit_score']}
Existing Loans: {application['existing_loan_amount_usd']}

Explain clearly and professionally.
"""

    client = _get_client()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text.strip()
