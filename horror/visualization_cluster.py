import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler, StandardScaler

num_clusters = 250
df = pd.read_csv(f"horror_games_clustered_{num_clusters}.csv")

# — Feature engineering —

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
scaled_numeric = pd.DataFrame(
    MinMaxScaler().fit_transform(df[numeric_cols]),
    columns=numeric_cols
)

# Combine features
features = pd.concat([scaled_numeric, tag_features, genre_features], axis=1)

# Standardize and retrieve clustering
labels = df['cluster']
X_std = StandardScaler().fit_transform(features)

# ─── PCA for 2D visualization ───
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_std)

# Plot PCA scatter colored by cluster
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, alpha=0.6)
plt.colorbar(scatter, label='Cluster Label')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('PCA of Horror Game Features\nColored by K-Means Cluster')
plt.tight_layout()
plt.savefig(f"cluster_{num_clusters}_PCA.png", dpi=300, bbox_inches='tight')
plt.show()

# ─── t-SNE for 2D visualization ───
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
plt.savefig(f"cluster_{num_clusters}_t-SNE.png", dpi=300, bbox_inches='tight')
plt.show()
