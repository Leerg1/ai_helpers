from fastapi import APIRouter

from reviewer.models.rewiev_request import ReviewRequest
from reviewer.services.ollama_client import ask_model

router = APIRouter()

@router.post("/ai_review")
async def review_python(req: ReviewRequest):
    prompt = f"""
    Как Python эксперт, проанализируй код на логику, ошибки и баги
    Код:
    {req.code}
    Ответ - краткий пронумерованный список.
    """
    try:
        print(f"Получен код для ревью:\n{req.code}")
        answer = await ask_model(prompt)
        print(f"Результат ревью:\n{answer}")
        return answer
    except Exception as e:
        print(f"Ошибка при анализе: {e}")
        return f"Ошибка при анализе: {e}"


@router.get("/check_service")
def ping():
    return {"msg": "hello world"}