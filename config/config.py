import os

LLM_API_BASE_URL = os.getenv("LLM_API_BASE_URL", "https://api.groq.com/openai/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "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")
LLM_CHAT_MODEL = os.getenv("LLM_CHAT_MODEL", "llama-3.1-8b-instant")
LLM_STREAMING = os.getenv("LLM_STREAMING", "yes").lower() != "no"
PORT = int(os.getenv("PORT", 3000))
