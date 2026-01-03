# Decision Assist API  
**AI as an Assistant, Not a Decision-Maker**

---

## Can AI Take Responsibility for Decision-Making on Behalf of Humans?

In today’s automation-driven world, speed has become a defining factor in how decisions are made. From instant recommendations to online approvals, artificial intelligence (AI) is increasingly embedded in systems that influence financial, legal, and social outcomes.

This project was inspired by a real-world experience while applying for a car loan (for example, a Kia K4 GT-Line priced around $27,000). The application process was simple and fully digital—requiring only basic details such as income, credit score, and existing loan obligations. Yet, despite automation, the final decision still took up to 48 hours.

This raised a natural question:

> If data is already digital and systems are automated, why can’t AI make an instant decision?

At first glance, the idea seems logical. AI can process vast amounts of data quickly and consistently. However, this leads to a deeper and more important question:

> **Should AI take authority over decisions, or should it remain an assistant to human judgment?**

The distinction may appear subtle, but the line between **assistance and authority is thin**—and crossing it without care can introduce serious ethical, legal, and social consequences.

---

## Why AI Should Not Own Decisions

Granting AI full authority over decisions such as loan approvals or credit limits does more than increase speed—it transfers responsibility.

### A Real-World Risk: Invisible Bias

- Traditional rule-based systems are explicit and auditable  
- AI systems may infer sensitive attributes indirectly (e.g., ZIP codes, behavior patterns)
- Decisions can become opaque and difficult to explain
- Accountability becomes unclear when outcomes are challenged

When asked why a decision was made, the answer often becomes:
> *“The system gave a low score.”*

This lack of transparency erodes trust.

---

## AI as an Assistant: The Safer Model

This project adopts a different approach—one where AI is **explicitly limited to an assistant role**.

### Clear Responsibility Split

- **AI**: Analysis, explanation, insight generation  
- **Humans**: Judgment, accountability, final authority  

In this model:
- Decisions are made using **deterministic, rule-based logic**
- AI never approves or rejects
- AI only explains *why* a decision was reached

A good decision is one that a human is willing to stand behind.

---

## Project Overview

This repository implements a **Loan Evaluation API** using Python and FastAPI that demonstrates this principle in practice.

### Key Characteristics

- Rule-based decision engine (authoritative)
- AI-powered explanation layer (assistant-only)
- Fully auditable and transparent
- Production-ready API design

---

## Architecture
Client
↓
FastAPI
├── Rule Engine (Authoritative)
└── AI Assistant (Explanation Only)

---

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- Gemini-1.5-Flash (AI assistant)
- Render Cloud (deployment)

---

## Project Structure
decision-assist/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── health.py
│   │   └── loan.py
│   ├── decision/
│   │   └── loan_rules.py
│   └── ai/
│       └── gemini_assistant.py
├── requirements.txt
└── venv/

> The initial project setup seed is available as a tagged version in this repository.

---

## Setup Instructions

### Prerequisites

```bash
python --version
python -m pip --version
Environment Setup
mkdir decision-assist
cd decision-assist
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

---

## Rule-Based Decision Engine
### Authoritative layer — AI does not participate here
```
APPROVAL_RULES = {
    "MIN_CREDIT_SCORE": 700,
    "MIN_ANNUAL_INCOME": 60000,
    "MAX_DEBT_TO_INCOME_RATIO": 0.40
}
```
AI Assistant (Explanation Only)

The AI layer:
	•	Uses Gemini-1.5-Flash
	•	Explains outcomes in clear, human-readable language
	•	Never changes or overrides decisions

Loan API Endpoint

POST /loan/apply
	•	Validates input using Pydantic
	•	Applies rule-based decision logic
	•	Generates AI explanation after the decision
	•	Returns a structured response

### Running the Application
```
uvicorn app.main:app --reload
```
### API Documentation
The application is deployed on Render.
```
👉 Swagger UI:
https://decision-assist-wde0.onrender.com/docs
```
## Example Requests
### ❌ Rejected Request
```
{
  "first_name": "Veera",
  "last_name": "reddy",
  "annual_income_usd": 10000,
  "credit_score": 650,
  "driver_license_number": "AONE9329043",
  "existing_loan_amount_usd": 6000,
  "requested_loan_amount_usd": 27000
}
```
### ✅ Approved Request
```
{
  "first_name": "Veera",
  "last_name": "Reddy",
  "annual_income_usd": 85000,
  "credit_score": 720,
  "driver_license_number": "AONE9329043",
  "existing_loan_amount_usd": 12000,
  "requested_loan_amount_usd": 27000
}
```
---
## License
### MIT License
