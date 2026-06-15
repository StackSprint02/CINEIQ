from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="CINEIQ API")

class RecommendationRequest(BaseModel):
    user_id: int
    movie_title: str

@app.get("/")
def root():
    return {"message": "Welcome to the CINEIQ API"}

@app.post("/recommend")
def get_recommendations(req: RecommendationRequest):
    # In a real scenario, you would call engine.py here.
    # We are mocking the response so you can test the frontend instantly.
    mock_recs = [
        {"title": "The Matrix", "reason": "Because you watch Sci-Fi."},
        {"title": "Inception", "reason": "Highly rated by users similar to you."},
        {"title": "Interstellar", "reason": "Sentiment analysis shows highly positive audience reception."}
    ]
    return {"user_id": req.user_id, "recommendations": mock_recs}