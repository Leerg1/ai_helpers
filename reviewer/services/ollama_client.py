import httpx

from reviewer.models.rewiew_response import ReviewResponse


def from_deepseek_coder_6_7(prompt: str) -> ReviewResponse:
    """
    Синхронный запрос к Ollama HTTP API.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "deepseek-coder:6.7b-instruct-q4_1",
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "temperature": 0,  # Детерминированность
        "options": {
            "num_predict": 300,  # Достаточно для 1-3 пунктов
            "top_k": 40,         # Шире выбор, но не слишком
            "top_p": 0.9,        # Nucleus sampling
            "repeat_penalty": 1.1
        }
    }

    with httpx.Client(timeout=300) as client:
        r = client.post(url, json=payload)
        r.raise_for_status()
        return r.json()


def warmup_model():
    """
    Прогрев модели после её загрузки.
    Отправляет короткий запрос, чтобы Ollama полностью загрузил модель в память.
    """
    prompt = "Привет. Это тестовый запрос для прогрева модели. Ответ не важен."
    print("Прогрев модели: отправка тестового запроса...")
    response = from_deepseek_coder_6_7(prompt)
    print("Модель прогрета. Ответ прогрева:")
    print(response.response)
