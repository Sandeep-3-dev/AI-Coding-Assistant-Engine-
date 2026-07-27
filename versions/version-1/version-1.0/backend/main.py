from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import ask_llm

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = ask_llm(request.message)
    return {"reply": reply}