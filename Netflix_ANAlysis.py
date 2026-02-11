import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# LOAD DATA
# ======================================
# Load Netflix dataset
df = pd.read_csv("netflix_titles.csv")

# ======================================
# DATA CLEANING
# ======================================

# Remove rows with missing ratings
df = df.dropna(subset=["rating"])

# Remove duplicate rows
df = df.drop_duplicates()

# Remove incorrect rating values (e.g., "74 min" mistakenly in rating column)
df = df[~df["rating"].str.contains("min", na=False)]

# ======================================
# BAR CHART: RATINGS DISTRIBUTION
# ======================================

# Count titles per rating
rating_counts = df["rating"].value_counts()

plt.figure(figsize=(10, 6))
bars = plt.bar(rating_counts.index, rating_counts.values)

plt.title("Ratings Distribution of Netflix Titles")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

# Add count labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

# ======================================
# PIE CHART: MOVIES VS TV SHOWS
# ======================================

type_counts = df["type"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    type_counts,
    labels=type_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Share of Movies vs TV Shows on Netflix")
plt.axis("equal")

plt.show()