from fastapi import FastAPI
from pydantic import BaseModel
from database import session_local
from model import PlannerTable
from chat_service import chat


app = FastAPI(
    title="Cognizant company chatbot",
    description="Agent capable of clarifying query regarding Cognizant company",
    version="1.0.0"
)


class DataValidation(BaseModel):
    message: str


@app.get("/")
def Home():
    return {"Welcome to Astronomical world"}


@app.post("/message")
def message_endpoint(data: DataValidation):
    answer = chat(data.message, [])

    # Connect to database
    db = session_local()

    try:
        # Insert question and answer
        new_record = PlannerTable(
            question=data.message,
            answer=answer
        )

        db.add(new_record)
        db.commit()
        db.refresh(new_record)

        return {
            "id": new_record.id,
            "question": new_record.question,
            "answer": new_record.answer
        }

    finally:
        db.close()