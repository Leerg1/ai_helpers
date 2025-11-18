import httpx

from reviewer.models.rewiew_response import ReviewResponse


def from_deepseek_coder_1_3(prompt: str) -> ReviewResponse:
    """
    Синхронный запрос к Ollama HTTP API.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "deepseek-coder:1.3b",
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    #TODO: модель слишком глупая или я использую ее неправильно. Нужно изучить модели.

    with httpx.Client(timeout=300) as client:
        r = client.post(url, json=payload)
        r.raise_for_status()
        data = ReviewResponse(**r.json())
        return data


def warmup_model():
    """
    Прогрев модели после её загрузки.
    Отправляет короткий запрос, чтобы Ollama полностью загрузил модель в память.
    """
    prompt = "Привет. Это тестовый запрос для прогрева модели. Ответ не важен."
    print("Прогрев модели: отправка тестового запроса...")
    response = from_deepseek_coder_1_3(prompt)
    print("Модель прогрета. Ответ прогрева:")
    print(response.response)
