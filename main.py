from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=AnswerResponse)
def ask_unit_titles_act(data: QuestionRequest):
    if "body corporate" in data.question.lower():
        return {"answer": "The Body Corporate is responsible for managing common property under the Unit Titles Act 2010."}
    return {"answer": "Sorry, I couldn't find an answer in the Unit Titles Act 2010."}




