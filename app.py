from fastapi import FastAPI
import requests

app = FastAPI()

LOCAL_AI = "https://swing-ski-earning-durham.trycloudflare.com/chat"

@app.get("/")
def home():
    return {"status": "NeuraForge gateway online"}

@app.post("/chat")
async def chat(data: dict):
    r = requests.post(LOCAL_AI, json=data)
    return r.json()
