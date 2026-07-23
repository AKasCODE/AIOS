from fastapi import FastAPI
from app.models.chat import ChatRequest
from app.services.llm_service import ask_llm

app = FastAPI()

@app.get("/")
def home():
    return {"message":"JARVIS is running..."}

@app.post("/chat")
def chat(request:ChatRequest):
    reply = ask_llm(request.message)
    return {"reply":reply}