from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI API is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "message": request.message,
        "response": "Gemma response gill be connected next."
    }