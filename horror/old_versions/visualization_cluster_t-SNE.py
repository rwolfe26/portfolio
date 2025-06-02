import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler, StandardScaler
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

# Load enriched dataset (path in notebook environment)
df = pd.read_csv("horror_games_enriched_full.csv")

# — Feature Engineering — 
df['review_count'] = df['review_count'].str.replace(',', '').astype(float).fillna(0)
review_mapping = {
    'Overwhelmingly Positive': 1.0, 'Very Positive': 0.8, 'Positive': 0.6,
    'Mostly Positive': 0.6, 'Mixed': 0.5, 'Mostly Negative': 0.2,
    'Negative': 0.2, 'Very Negative': 0.1, 'Overwhelmingly Negative': 0.0
}
df['review_score'] = df['review_summary'].map(review_mapping).fillna(0.5)
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').fillna(0)
df['avg_playtime'] = df['avg_playtime'].fillna(0)
df['med_playtime'] = df['med_playtime'].fillna(0)
df['price_usd'] = df['price_usd'].fillna(df['price_usd'].median())

# Encode user_tags and genres_official
mlb_tags = MultiLabelBinarizer()
tags_split = df['user_tags'].fillna('').str.split('|')
tag_features = pd.DataFrame(mlb_tags.fit_transform(tags_split),
                            columns=[f"tag_{t}" for t in mlb_tags.classes_])
mlb_genres = MultiLabelBinarizer()
genres_split = df['genres_official'].fillna('').str.split('|')
genre_features = pd.DataFrame(mlb_genres.fit_transform(genres_split),
                              columns=[f"genre_{g}" for g in mlb_genres.classes_])

# Scale numeric features
numeric_cols = ['price_usd', 'review_count', 'review_score', 'avg_playtime', 'med_playtime', 'release_year']
scaled_numeric = pd.DataFrame(MinMaxScaler().fit_transform(df[numeric_cols]), columns=numeric_cols)

# Combine features
features = pd.concat([scaled_numeric, tag_features, genre_features], axis=1)

# Standardize for clustering and TSNE
X_std = StandardScaler().fit_transform(features)

# K-Means clustering (k=5)
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_std)

# Compute t-SNE embedding
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
X_tsne = tsne.fit_transform(X_std)

# Plot t-SNE scatter with cluster colors
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels, alpha=0.6)
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE of Horror Game Features Colored by Cluster')
plt.colorbar(scatter, label='Cluster Label')
plt.tight_layout()
plt.savefig("cluster_t-SNE.png", dpi=300, bbox_inches='tight')
plt.show()
