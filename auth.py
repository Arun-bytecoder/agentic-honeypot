from fastapi import Header, HTTPException
import os

API_KEY = os.getenv("API_KEY", "honeypot_2026_secure_key")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
