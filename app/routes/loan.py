# lets you group related API endpoints.
from fastapi import APIRouter
# Used to define data models with validation and type hints
from pydantic import BaseModel
# This function:
# 	•	Applies deterministic rules
# 	•	Returns the final loan decision
from app.decision.loan_rules import evaluate_loan
# •	Imports an AI helper function.
# •	Used only to explain the decision.
from app.ai.gemini_assistant import generate_decision_explanation
# Creates a router object
router = APIRouter(prefix="/loan", tags=["Loan"])

# Defines a request body schema


class LoanApplication(BaseModel):
    first_name: str
    last_name: str
    annual_income_usd: float
    credit_score: int
    driver_license_number: str
    existing_loan_amount_usd: float = 0
    requested_loan_amount_usd: float

# Declares a POST endpoint.
# •	Defines an async endpoint handler.
# •	FastAPI:
# •	Parses JSON body
# •	Validates it
# •	Injects it as a LoanApplication object


@router.post("/apply")
async def apply_loan(application: LoanApplication):
    # Converts the Pydantic model into a standard Python dictionary.
    application_data = application.model_dump()

    # •	Calls your deterministic rule engine.
    # •	This function:
    # •	Applies lending rules
    # •	Returns approval/denial and metadata
    # •	No AI involved here.
    decision_result = evaluate_loan(application_data)

    # •	Calls an async AI function.
    # •	Uses:
    # •	Original application data
    # •	Final decision
    # •	Produces a human-readable explanation.
    ai_explanation = await generate_decision_explanation(
        application_data,
        decision_result
    )

    return {
        "application": application_data,
        "decision": decision_result,
        "ai_assistance": {
            "role": "EXPLANATION_ONLY",
            "summary": ai_explanation
        }
    }
