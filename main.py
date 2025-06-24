# main.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
df = pd.read_csv('data/movies.csv')
df = df[['title', 'overview']].dropna()

# Vectorize Overview Text
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['overview'])

# Compute Similarity Matrix
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation Function
def recommend(movie_name):
    movie_name = movie_name.lower()
    if movie_name not in df['title'].str.lower().values:
        return ["Movie not found in database."]

    idx = df[df['title'].str.lower() == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended = [df.iloc[i[0]]['title'] for i in scores]
    return recommended

# Example
if __name__ == '__main__':
    movie = input("Enter a movie name: ")
    results = recommend(movie)
    print("\nRecommended movies:")
    for i, title in enumerate(results, 1):
        print(f"{i}. {title}")
