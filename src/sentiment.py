from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentReRanker:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_review(self, text):
        """Returns a compound score from -1 (negative) to 1 (positive)"""
        score = self.analyzer.polarity_scores(text)
        return score['compound']

    def rerank_recommendations(self, recommendations, reviews_dict):
        """
        Takes a list of recommended movies and a dictionary of their reviews,
        adjusts their rank based on audience sentiment.
        """
        ranked_recs = []
        for movie in recommendations:
            reviews = reviews_dict.get(movie, [])
            if not reviews:
                ranked_recs.append((movie, 0)) # Neutral if no reviews
                continue
            
            avg_sentiment = sum([self.analyze_review(r) for r in reviews]) / len(reviews)
            ranked_recs.append((movie, avg_sentiment))
            
        # Sort by sentiment descending
        ranked_recs.sort(key=lambda x: x[1], reverse=True)
        return [movie[0] for movie in ranked_recs]