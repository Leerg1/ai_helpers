from fastapi import APIRouter
from reviewer.models.rewiev_request import ReviewRequest
from reviewer.services.ollama_client import from_deepseek_coder_6_7

router = APIRouter()


@router.post("/ai_review_deepseek_coder_6_7")
def review_from_deepseek_coder_6_7(req: ReviewRequest):
    prompt = f"""
    Python static code review. Find specific technical issues:

    CODE:
    {req.code}

    ANALYZE:
    - Logical errors
    - Potential bugs  
    - Logic improvements

    OUTPUT REQUIREMENTS:
    - 1-3 bullet points max
    - Each point in one line
    - Technical issues only (ignore style)
    - If no issues: "No fixes needed"
    """

    #TODO: сейчас передается только малая часть кода, только конкретные изменения. Нет контекста для анализа.
    #TODO: нужно передавать контекст и просить анализировать изменения.

    answer = from_deepseek_coder_6_7(prompt)
    return answer.response
