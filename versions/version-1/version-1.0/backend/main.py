from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chat_bot

app = FastAPI()
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = chat_bot(request.message)
    return {"reply": reply}