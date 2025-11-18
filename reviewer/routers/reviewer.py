import json

from fastapi import APIRouter
from reviewer.models.rewiev_request import ReviewRequest
from reviewer.services.ollama_client import from_deepseek_coder_1_3

router = APIRouter()


@router.post("/ai_review_deepseek_coder_1_3")
def review_from_deepseek_coder_1_3(req: ReviewRequest):
    prompt = f"""
    Ты - дотошный эксперт по Python.
    Ты получил код на ревью.
    Ищи логические ошибки и баги, предлагай улучшения, игнорируй стиль и линтеры PEP8. 
    Дай максимум 3 кратких замечания, каждый пункт ≤1 строки.
    Отвечай только на русском языке.
    Если нет ошибок, ответ - "Нет исправлений". 
    Формат ответа - только строка с замечаниями без форматирования.
    
    Код:
    {req.code}
    """

    #TODO: проработать промт. Сейчас возвращается случайная фраза.
    answer = from_deepseek_coder_1_3(prompt)
    return answer.response
