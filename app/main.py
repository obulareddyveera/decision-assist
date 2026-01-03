from app.routes.health import router as health_router
from app.routes.loan import router as loan_router
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()  # MUST be first


app = FastAPI(
    title="Decision Assist API",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(loan_router)


@app.get("/")
def root():
    return {"message": "Decision Assist API is running 🚀"}
