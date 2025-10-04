from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="LearnXT-API",
    description="LearnXT-API for ai generate content",
    version="0.1.0",
)


