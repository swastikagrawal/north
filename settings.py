import os
from dotenv import load_dotenv
env_path = ".env"
load_dotenv(env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")
GROQ_MODEL = os.getenv("GROQ_MODEL")
OPEN_ROUTER_MODEL = os.getenv("OPEN_ROUTER_MODEL")