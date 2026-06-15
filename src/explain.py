def generate_explanation(user_profile, movie_features, method="rule_based"):
    """Rule-based template generation for fast explainability."""
    if method == "rule_based":
        shared_genres = set(user_profile['top_genres']).intersection(set(movie_features['genres']))
        if shared_genres:
            genres_str = ", ".join(list(shared_genres))
            return f"Because you frequently watch {genres_str} movies."
        return "Based on similarities to users with your rating history."
    return "Explanation not available."