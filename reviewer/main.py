from fastapi import FastAPI

from reviewer.routers.reviewer import router
from reviewer.services.ollama_client import warmup_model

app = FastAPI(title="AI Code Reviewer")

app.include_router(router, prefix="/api", tags=["review"])

# --- прогрев модели синхронно при старте приложения ---
print("=== Прогрев модели перед запуском FastAPI ===")
warmup_model()
print("=== Прогрев завершён ===")
