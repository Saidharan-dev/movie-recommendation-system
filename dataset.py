import pandas as pd
from datasets import load_dataset

# Load full dataset
ds = load_dataset("vishnupriyavr/wiki-movie-plots-with-summaries", split="train")
df = pd.DataFrame(ds[:30000])  # Increase sample size

# Rename columns
df.rename(columns={"Title": "title", "Plot": "overview", "Release Year": "year"}, inplace=True)

# Filter movies after 2000 with good descriptions
df = df[df["year"] > 2000]
df = df[df["overview"].notna() & df["title"].notna()]
df = df[df["overview"].str.len() > 50]

# Keep only required columns
df = df[["title", "overview"]]

# Save new cleaned dataset
df.to_csv("data/movies.csv", index=False)
print(f"✅ Saved {len(df)} movies to data/movies.csv")
