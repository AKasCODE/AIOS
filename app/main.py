from fastapi import FastAPI, HTTPException
from app.models.chat import ChatRequest
from app.services.llm_service import ask_llm

app = FastAPI()

@app.get("/")
def home():
    return {"message":"JARVIS is running..."}

@app.post("/chat")
def chat(request:ChatRequest):
    reply = ask_llm(request.message)

    if not reply['success']:
        raise HTTPException(status_code=500, detail=reply['error'])
    
    return {"reply":reply['reply']}