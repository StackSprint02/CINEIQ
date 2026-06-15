# 🎬 CINEIQ: Explainable Hybrid Recommendation Engine

## Problem Statement
Content discovery on modern streaming platforms is often opaque, biased toward promoted titles, and traps users in recommendation loops. CINEIQ is an open, explainable movie recommendation engine that combines multiple ML strategies to deliver personalized, interpretable suggestions that evolve with user taste.

## Features
* **Hybrid Recommendation Engine:** Combines Collaborative Filtering (SVD) and Content-Based Filtering (TF-IDF + Cosine Similarity).
* **Sentiment-Aware Re-Ranker:** Utilizes VADER NLP to analyze audience reviews and re-rank suggestions based on true audience reception.
* **Explainability Layer:** Surfaces human-readable reasons for every recommendation to build user trust.
* **User Taste Dashboard:** Built with Streamlit and Plotly to visualize genre affinities via interactive radar charts.

## Tech Stack
* **Machine Learning:** Python, scikit-learn, Surprise (SVD), Pandas, NumPy
* **NLP:** VADER Sentiment Analysis
* **Backend Serving:** FastAPI, Uvicorn
* **Frontend Dashboard:** Streamlit, Plotly
* **Experiment Tracking:** MLflow

## How to Run Locally

1. **Clone the repository:**

   ```bash
   git clone <your-github-link>
   cd cineiq
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI Backend:**

   ```bash
   uvicorn api.main:app --reload --port 8001
   ```

4. **Start the Streamlit Dashboard:**

   ```bash
   python -m streamlit run app/dashboard.py
   ```

## Dataset Used

**10,000 Movies Dataset:** A unified subset containing text overviews, genres, user ratings, and reviews to ensure seamless ID mapping and highly efficient computational inference across the hybrid model architecture.
