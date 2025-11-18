from pydantic import BaseModel

class ReviewResponse(BaseModel):
    model: str
    created_at: str
    response: str
    done: str | bool
    context: list
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int
