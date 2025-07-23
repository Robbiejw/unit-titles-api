from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str

@app.post("/ask", response_model=AnswerResponse)
def ask_unit_titles(data: QuestionRequest):
    return {"question": data.question}
