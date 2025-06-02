import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
from tqdm import tqdm

# Load enriched dataset
df = pd.read_csv('horror_games_enriched_full_new.csv')
#This slipped through the cracks earlier
df = df[~df["name"].str.lower().str.contains("demo")]

# --- Feature Engineering ---

# Clean numeric fields
df['review_count'] = df['review_count'].fillna(0)
df['review_score'] = df['review_score'].fillna(0.5)
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').fillna(0)
df['avg_playtime'] = df['avg_playtime'].fillna(0)
df['med_playtime'] = df['med_playtime'].fillna(0)
df['price_usd'] = df['price_usd'].fillna(df['price_usd'].median())

# Encode multi-label features
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
scaler_mm = MinMaxScaler()
numeric_scaled = pd.DataFrame(scaler_mm.fit_transform(df[numeric_cols]),
                              columns=numeric_cols)

# Combine all features
features = pd.concat([numeric_scaled, tag_features, genre_features], axis=1)

# Standardize for clustering
scaler_std = StandardScaler()
X = scaler_std.fit_transform(features)


'''# --- Elbow Method ---
inertias = []
k_range = range(1, 350)
for k in tqdm(k_range):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)

# Plot
plt.figure()
plt.plot(list(k_range), inertias, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for K-Means')
plt.tight_layout()
plt.show()'''

# --- Fit K-Means with chosen k ---
optimal_k = 250
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)
df['cluster'] = labels

# Display cluster sizes
cluster_counts = df['cluster'].value_counts().sort_index()
print(f"Cluster sizes for k={optimal_k}:\n", cluster_counts)

# Preview sample of clusters
preview = df[['appid', 'name', 'cluster']].sample(10)
print("\nSample assignments:\n", preview)

# At the very end of K_means_clustering.py
df['cluster'] = labels
df.to_csv(f"horror_games_clustered_{optimal_k}.csv", index=False)
print(f"✅ Clustered dataset saved as horror_games_clustered_{optimal_k}.csv")


