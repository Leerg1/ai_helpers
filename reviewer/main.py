from fastapi import FastAPI

from .routers import rewiever

app = FastAPI(title="AI Code Reviewer")

app.include_router(rewiever.router, prefix="/api", tags=["review"])
