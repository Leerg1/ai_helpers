# ollama_client.py
import httpx

async def ask_model(prompt: str):
    """
    Асинхронный запрос к Ollama HTTP API.
    """
    url = "http://localhost:11434/api/generate"
    payload = {"model": "qwen2.5-coder:7b-base", "prompt": prompt, "stream": False}

    try:
        async with httpx.AsyncClient(timeout=300) as client:
            r = await client.post(url, json=payload)
            r.raise_for_status()
            data = r.json()
            # поле 'response' гарантировано документацией
            return data.get("response", ""), data
    except httpx.RequestError as e:
        return f"Ошибка запроса к Ollama: {e}"
    except httpx.HTTPStatusError as e:
        return f"HTTP ошибка: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Неожиданная ошибка: {e}"
