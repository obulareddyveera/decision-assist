from typing import Dict, List

APPROVAL_RULES = {
    "MIN_CREDIT_SCORE": 700,
    "MIN_ANNUAL_INCOME": 60000,
    "MAX_DEBT_TO_INCOME_RATIO": 0.40
}


def evaluate_loan(application: Dict) -> Dict:
    """
    Evaluates loan application using deterministic rules.
    Returns a structured decision result.
    """

    reasons: List[str] = []

    if application["credit_score"] < APPROVAL_RULES["MIN_CREDIT_SCORE"]:
        reasons.append("Credit score below minimum threshold")

    if application["annual_income_usd"] < APPROVAL_RULES["MIN_ANNUAL_INCOME"]:
        reasons.append("Annual income below minimum requirement")

    debt_ratio = (
        application["existing_loan_amount_usd"]
        / application["annual_income_usd"]
    )

    if debt_ratio > APPROVAL_RULES["MAX_DEBT_TO_INCOME_RATIO"]:
        reasons.append("Debt-to-income ratio exceeds allowed limit")

    approved = len(reasons) == 0

    return {
        "decision": "APPROVED" if approved else "REJECTED",
        "decision_source": "RULE_ENGINE",
        "reasons": reasons,
        "metrics": {
            "credit_score": application["credit_score"],
            "annual_income_usd": application["annual_income_usd"],
            "debt_to_income_ratio": round(debt_ratio, 2)
        }
    }
