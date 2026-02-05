# 🕵️ Agentic Honeypot API – Scam Detection & Intelligence Extraction

An **Agentic Honeypot system** designed to **detect scam messages**, **autonomously engage scammers**, and **extract actionable intelligence** through multi-turn conversations.
# Agentic Honeypot API

## Endpoint
POST /honeypot

## Authentication
Header:
x-api-key: <API_KEY>

## Response Format
{
  "status": "success",
  "reply": "Why is my account being suspended?"
}

## Deployment
Built with FastAPI and deployed on Render.

Built as part of a **large-scale hackathon (3,00,000+ participants)** and deployed as a **public, authenticated REST API** for automated evaluation.

---

## 🚀 Problem Statement

Design and deploy an API that:

- Detects scam intent from incoming messages  
- Seamlessly hands over interaction to an autonomous agent  
- Engages scammers without revealing detection  
- Extracts intelligence such as:
  - Bank account numbers
  - UPI IDs
  - Phishing URLs  
- Returns structured JSON suitable for automated evaluation  

---

## ✨ Key Features

- 🔍 **Scam Intent Detection**  
  Keyword & pattern-based detection logic

- 🤖 **Autonomous Agent Engagement**  
  Multi-turn, human-like interaction flow

- 🧠 **Conversation Memory**  
  Tracks turns & engagement duration per conversation

- 🗂 **Intelligence Extraction**  
  Identifies UPI IDs, bank account numbers, and URLs

- 🔐 **Secure API Authentication**  
  API key–based access control

- 🌐 **Public Deployment**  
  Live, evaluation-ready API hosted on Render

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **Logic:** Regex & heuristic-based NLP  
- **Deployment:** Render  
- **Testing:** Thunder Client / Swagger UI  

---

## 📡 Live API

**Base URL**
https://agentic-honeypot-final-cc20.onrender.com

**Endpoint**

POST /honeypot


**Swagger Documentation**

/docs


---

## 🔐 Authentication

All requests must include an API key.

**Header**


X-API-Key: honeypot_2026_secure_key


---

## 📥 Request Example

```json
{
  "conversation_id": "eval_test_001",
  "message": "Congratulations! You won a prize. Pay to test@upi",
  "timestamp": "2026-02-04T12:00:00Z"
}

📤 Response Example
{
  "scam_detected": true,
  "agent_engaged": true,
  "conversation_id": "eval_test_001",
  "engagement": {
    "turns": 2,
    "duration_seconds": 120
  },
  "extracted_intelligence": {
    "upi_ids": ["test@upi"],
    "bank_accounts": [],
    "urls": []
  },
  "agent_reply": "Oh okay, how do I receive the money?"
}

🧠 Agent Behavior

Detects scam intent discreetly

Engages only after scam confirmation

Maintains realistic, non-alerting conversation flow

Gradually probes for scam intelligence

⚙️ Local Setup
git clone https://github.com/Arun-bytecoder/agentic-honeypot-final.git
cd agentic-honeypot-final
pip install -r requirements.txt
uvicorn main:app --reload

🏆 Hackathon Context

🤖 Automated API-based evaluation

✅ Built to meet strict stability, schema, and latency requirements

👤 Author

Arunachalam
Backend Developer | Python | FastAPI | Agentic Systems

GitHub: https://github.com/Arun-bytecoder

⚠️ Disclaimer

This project is intended solely for educational, research, and security-awareness purposes.
It does not interact with real scammers or financial systems.
