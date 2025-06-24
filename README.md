# 🎬 Movie Recommendation System

A smart **Content-Based Movie Recommendation System** built using Python and Streamlit.  
Enter any movie title and instantly get 5 similar movie suggestions — based on plot-level understanding using machine learning.

---

## 📦 Features

✅ Clean Streamlit interface  
✅ 1000+ movie plots from Wikipedia  
✅ Fuzzy search for partial or misspelled titles  
✅ Recommends based on plot similarity using TF-IDF + Cosine Similarity  
✅ Supports both Indian and international movies

---

## 🧠 How it Works

1. Loads a dataset of movies with plot summaries (from Hugging Face)
2. Converts each plot to a numerical vector using `TfidfVectorizer`
3. Compares your movie with all others using cosine similarity
4. Displays the top 5 most similar titles

---

## 🖼 Example

Input: Vada Chennai
Output: Striker, Paisa Paisa, The Triplets of Belleville, etc.
## 📁 Project Structure
movie-recommendation-system/
├── main.py # Streamlit app
├── dataset.py # Generates dataset from Hugging Face
├──appendnew.py #this helps to add new movies with their summaries
├── data/
│ └── movies.csv # Contains title + overview for 1000+ movies
├── requirements.txt # Python dependencies
└── README.md # Project info (this file)

---

## 🛠 Installation & Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Saidharan-dev/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
python dataset.py
streamlit run main.py
💡 Future Plans
🎞 Add movie posters using TMDb API

🌍 Filter by language (Tamil, Hindi, English, etc.)

🤖 Use BERT for smarter, deeper plot-based recommendations

🧠 Save user preferences for better personalization

🙋‍♂️ About the Developer
👋 I’m Sai Dharan
🎓 B.Tech Artificial Intelligence & Data Science | Class of 2027
💻 Passionate about AI, ML, and full-stack development
🌐 GitHub
