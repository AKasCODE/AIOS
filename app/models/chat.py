from pydantic import BaseModel
class ChatRequest(BaseModel):
    message:str
'''
All request/response models will live here.

Later we'll have:
LoginRequest
MemoryRequest
VoiceRequest
ToolRequest

Everything stays organized.
'''