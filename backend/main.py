from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sruthiAI import what_would_sruthi_say

app = FastAPI(title="Sruthi AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This is the "Master Key" that fixes the error
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_twin(request: ChatRequest):
    try:
        answer = what_would_sruthi_say(request.query)
        return {"response": answer}
    except Exception as e:
        # This will print the EXACT error in your Cloud Shell terminal
        print(f"DEBUG ERROR: {e}") 
        return {"response": f"Error: {str(e)}"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
