import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set up page
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Title
st.title("🎬 Movie Recommendation System")
st.markdown("Type a movie title and get similar recommendations based on its description!")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")
    df.dropna(subset=["title", "overview"], inplace=True)
    return df

df = load_data()

# Vectorize overviews
@st.cache_resource
def compute_similarity():
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

similarity_matrix = compute_similarity()

# Recommendation function
def recommend(title):
    title = title.lower().strip()
    if title not in df['title'].str.lower().values:
        return ["❌ Movie not found. Please check the spelling."]
    
    idx = df[df['title'].str.lower() == title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # top 5 excluding itself
    return [df.iloc[i[0]]['title'] for i in sim_scores]

# Input box
user_input = st.text_input("Enter a movie title:")

if st.button("Recommend"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid movie title.")
    else:
        results = recommend(user_input)
        st.subheader("🔍 Top 5 Recommendations:")
        for i, movie in enumerate(results, 1):
            st.write(f"{i}. {movie}")
