import pandas as pd 
tamil_movies = [
    {"title": "Vada Chennai", "overview": "A carrom champion is drawn into the world of crime in North Chennai."},
    {"title": "96", "overview": "Two high school sweethearts reunite after 22 years at a school reunion and relive their past."},
    {"title": "Kaithi", "overview": "An ex-convict fights to save injured police officers from a drug gang on the night of Diwali."}
]

df = pd.read_csv("data/movies.csv")
df = pd.concat([df, pd.DataFrame(tamil_movies)], ignore_index=True)
df.to_csv("data/movies.csv", index=False)
print("✅ Added Tamil movies to the dataset.")
