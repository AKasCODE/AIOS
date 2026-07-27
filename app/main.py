from fastapi import FastAPI, HTTPException
from app.models.chat import ChatRequest
from app.services.chat_service import process_chat
from .database.database import create_tables

app = FastAPI()
create_tables()
@app.get("/")
def home():
    return {"message":"JARVIS is running..."}

@app.post("/chat")
def chat(request:ChatRequest):
    reply = process_chat(request.message)

    if not reply['success']:
        raise HTTPException(status_code=500, detail=reply['error'])
    
    return {"reply":reply['reply']}