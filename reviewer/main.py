from fastapi import FastAPI

from reviewer.routers.reviewer import router

app = FastAPI(title="AI Code Reviewer")

app.include_router(router, prefix="/api", tags=["review"])
