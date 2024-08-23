import json
import requests
from config.config import LLM_API_BASE_URL, LLM_API_KEY, LLM_CHAT_MODEL, LLM_STREAMING

def parse(line):
    try:
        line = line.strip()
        if line.startswith("data: "):
            line = line[len("data: "):]
            if line:
                parsed_data = json.loads(line)
                if "choices" in parsed_data and parsed_data["choices"]:
                    choice = parsed_data["choices"][0]
                    if "delta" in choice and "content" in choice["delta"]:
                        return choice["delta"]["content"]
        return None
    except json.JSONDecodeError:
        return None

def chat(messages, handler):
    url = f"{LLM_API_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": messages,
        "model": LLM_CHAT_MODEL,
        "max_tokens": 400,
        "temperature": 0.5,
        "top_p": 0.9,  
        "top_k": 30,  
        "stream": True
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    if not response.ok:
        raise Exception(f"HTTP error with the status: {response.status_code} {response.reason}")

    answer = ""
    buffer = ""
    for line in response.iter_lines(decode_unicode=True):
        line = buffer + line
        if line.startswith(":"):
            buffer = ""
            continue
        if line == "data: [DONE]":
            break
        if line:
            partial = parse(line)
            if partial is None:
                buffer = line
            elif partial:
                buffer = ""
                answer += partial
                if handler:
                    handler(partial)
    return answer
