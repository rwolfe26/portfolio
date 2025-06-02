import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler


# Load the enriched dataset
df = pd.read_csv("horror_games_enriched_full_new.csv")

# 1. Clean and convert numeric fields
df['review_count'] = (
    df['review_count']
    .str.replace(',', '')
    .astype(float)
    .fillna(0)
)

# Map review summary to sentiment scores
review_mapping = {
    'Overwhelmingly Positive': 1.0,
    'Very Positive': 0.8,
    'Positive': 0.6,
    'Mostly Positive': 0.6,
    'Mixed': 0.5,
    'Mostly Negative': 0.2,
    'Negative': 0.2,
    'Very Negative': 0.1,
    'Overwhelmingly Negative': 0.0
}
df['review_score'] = df['review_summary'].map(review_mapping).fillna(0.5)

# Convert release_year to numeric
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Fill missing playtime and price
df['avg_playtime'] = df['avg_playtime'].fillna(0)
df['med_playtime'] = df['med_playtime'].fillna(0)
df['price_usd'] = df['price_usd'].fillna(df['price_usd'].median())

# 2. Encode multi-label features: user_tags and genres_official
mlb_tags = MultiLabelBinarizer()
tags_split = df['user_tags'].fillna('').str.split('|')
tag_features = pd.DataFrame(
    mlb_tags.fit_transform(tags_split),
    columns=[f"tag_{t}" for t in mlb_tags.classes_]
)

mlb_genres = MultiLabelBinarizer()
genres_split = df['genres_official'].fillna('').str.split('|')
genre_features = pd.DataFrame(
    mlb_genres.fit_transform(genres_split),
    columns=[f"genre_{g}" for g in mlb_genres.classes_]
)

# 3. Scale numeric features between 0 and 1
numeric_cols = ['price_usd', 'review_count', 'review_score', 'avg_playtime', 'med_playtime', 'release_year']
scaler = MinMaxScaler()
scaled_numeric = pd.DataFrame(
    scaler.fit_transform(df[numeric_cols]),
    columns=[f"scaled_{col}" for col in numeric_cols]
)

# 4. Combine all features into one DataFrame
features_df = pd.concat([scaled_numeric, tag_features, genre_features], axis=1)

# Display the feature matrix shape and a sample
print("Feature matrix shape:", features_df.shape)
print(features_df.head())

# Show interactive preview
print(features_df.head())
