# North

North is a context-aware GenAI assistant designed for reliability and consistent responses during extended conversations.

It uses a primary LLM for generation and automatically switches to a fallback model if the primary model fails, ensuring uninterrupted replies.

---

## Features

- Automatic model failover for reliability  
- Context-aware responses using recent conversation history  
- Last **250 messages** sent as context to maintain continuity  
- **250-character limit** on user input and model responses to maintain speed & reliability  
- SQLite-based local conversation storage  
- Efficient context window to reduce latency and token usage  
- Chat history viewing and deletion support  

---

## Tech Stack

- Python  
- SQLite  
- Groq API (OpenAI's GPT OSS 120B) -> Primary Model
- OpenRouter API (Meta's Llama 3.3 70B) -> Fallback Model

---

## How it Works

1. User sends a message  
2. Previous conversation history (up to 250 messages) is included for context  
3. Primary model generates response  
4. If an error occurs → fallback model takes over  
5. Conversation is stored locally for continuity  

---

## Design Decisions

- Limiting context to recent messages ensures relevance while keeping responses fast.  
- Character limits help maintain responsiveness and prevent model overload.  
- Local storage keeps conversations private and lightweight.  
- Failover logic improves reliability during API failures or downtime.

---

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```
Replace these in the .env with your keys, models and prompt:
```bash
GROQ_API_KEY=<YOUR_GROQ_API_KEY>
OPENROUTER_API_KEY=<YOUR_OPENROUTER_API_KEY>
GROQ_MODEL=<YOUR_GROQ_MODEL>
OPEN_ROUTER_MODEL=<YOUR_OPEN_ROUTER_MODEL>
SYSTEM_PROMPT=<YOUR_SYSTEM_PROMPT>
```
Run:
```bash
main.py
```
