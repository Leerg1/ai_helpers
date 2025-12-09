import httpx

URL = "http://localhost:11434/api/generate"

def from_deepseek_coder_6_7(prompt: str):
    payload = {
        "model": "deepseek-coder:6.7b-instruct-q4_1",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.0,
        "options": {
            "num_predict": 180,
            "repeat_penalty": 1.15,
            "top_k": 20,
            "top_p": 0.7
        }
    }
    with httpx.Client(timeout=300) as client:
        r = client.post(URL, json=payload)
        r.raise_for_status()
        return r.json()


def from_codellama_7b(prompt: str):
    payload = {
        "model": "codellama:7b-instruct-q4_1",
        "prompt": prompt,
        "stream": False,
        "temperature": 0.0,
        "options": {
            "num_predict": 80,
            "repeat_penalty": 1.15,
            "top_k": 20,
            "top_p": 0.7
        }
    }
    with httpx.Client(timeout=300) as client:
        r = client.post(URL, json=payload)
        r.raise_for_status()
        return r.json()
