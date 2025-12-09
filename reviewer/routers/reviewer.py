import logging
import traceback

from fastapi import APIRouter
from reviewer.models.rewiev_request import ReviewRequest
from reviewer.services.ollama_client import from_deepseek_coder_6_7, from_codellama_7b

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/ai_review_deepseek_coder_6_7")
def review_from_deepseek_coder_6_7(req: ReviewRequest):
    prompt = f"""
    You are a Python static analyzer.
    You do not fix code, and you do not provide suggestions. You only report real issues.
    
    TASK:
    Analyze the Python code below.
    Find up to 3 REAL technical issues ONLY for:
    - logical errors
    - runtime bugs
    - edge cases that may break
    Ignore style, formatting, refactoring.
    
    RULES:
    - Do NOT invent hypothetical issues or environment assumptions.
    - Do NOT provide corrected code, examples, or suggestions.
    - Output each issue on a single line. 
    - MAX 100 characters per line. If you exceed it, the answer is INVALID.
    - No explanations, no intro, no outro.
    
    CODE:
    {req.code}
    """
    logger.info(prompt)
    try:
        resp = from_deepseek_coder_6_7(prompt)
        return resp.get("response", "")
    except Exception:
        print(traceback.format_exc())
        raise


@router.post("/ai_review_codellama_7b")
def review_from_codellama_7b(req: ReviewRequest):
    prompt = f"""
    You are a strict Python static analyzer.

    TASK:
    Find up to 3 real issues (logical error, runtime bug, breaking edge case).
    
    OUTPUT RULES:
    - Only issues, no explanations.
    - Allowed types: logic, runtime, edge.
    - MAX line length: 100 characters.
    - No multi-sentence lines. No "because", "which", "that", "this could".
    - No extra text. If no issues → output "OK".
    
    CODE:
    {req.code}
    """
    logger.info(prompt)
    try:
        resp = from_codellama_7b(prompt)
        return resp.get("response", "")
    except Exception:
        print(traceback.format_exc())
        raise
