from typing import Union

from fastapi import FastAPI, responses

app = FastAPI()


@app.get("/api/ping")
def read_root():
    """Healthcheck."""
    
    return {"data": "pong"}


@app.get("/api/short")
def create_short_url(original_url: str):
    """Create a short url from original one."""

    return {"data": {"short_url": "http://localhost:8000/abcde"}}


@app.get("/{short_url}")
def follow_redirect(short_url: str):
    """Get original url from short url and redirect."""

    original_url = "https://practicum.com"
    return responses.RedirectResponse(original_url)