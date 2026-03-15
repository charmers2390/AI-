import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Load API key from environment variable
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY environment variable not set")

# Disable docs endpoints
app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

# Allow requests only from your website
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://id-preview--fcdc806e-49bf-48e8-9c79-daf036e1bd36.lovable.app "],  # change to your domain
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "NeuraForge AI running"}

@app.post("/chat")
async def chat(request: Request):

    # Check API key
    key = request.headers.get("x-api-key")

    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")

    data = await request.json()
    message = data.get("message")

    import requests

# Send the message to your AI backend
ai_backend = "https://swing-ski-earning-durham.trycloudflare.com/chat"

payload = {
    "message": message
}

try:
    r = requests.post(ai_backend, json=payload, timeout=60)

    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="AI backend error")

    response = r.json().get("response", "No response from AI")

except requests.exceptions.RequestException:
    raise HTTPException(status_code=500, detail="Could not reach AI backend")

    return {"response": response}
