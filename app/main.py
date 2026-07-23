from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("OPENROUTER_API_KEY"))


app = FastAPI()

class ChatRequest(BaseModel):
    message:str

@app.get("/")
def home():
    return {"message":"JARVIS is running..."}

@app.post("/chat")
def chat(request:ChatRequest):
    return {"reply":f"You said: {request.message}"}