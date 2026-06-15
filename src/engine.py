import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import SVD, Dataset, Reader

class HybridRecommender:
    def __init__(self):
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.svd = SVD()
        self.movie_data = None
        self.cosine_sim = None

    def fit_content(self, movies_df):
        """Train Content-Based Filtering using Genres/Keywords"""
        self.movie_data = movies_df.reset_index()
        # Assuming a 'description' or 'genres' column exists
        tfidf_matrix = self.tfidf.fit_transform(movies_df['genres'].fillna(''))
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def fit_collaborative(self, ratings_df):
        """Train Collaborative Filtering using SVD"""
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
        trainset = data.build_full_trainset()
        self.svd.fit(trainset)

    def get_content_recs(self, title, top_n=10):
        # Basic exact match for simplicity in demo
        idx = self.movie_data.index[self.movie_data['title'] == title].tolist()[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        movie_indices = [i[0] for i in sim_scores]
        return self.movie_data['title'].iloc[movie_indices].tolist()