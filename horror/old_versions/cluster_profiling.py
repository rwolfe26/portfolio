# cluster_profiling.py

import pandas as pd

# Load your cluster assignments
df = pd.read_csv("horror_games_clustered.csv")

# — 1) Numeric summaries per cluster —
numeric_cols = [
    'price_usd',
    'review_count',
    'review_score',
    'avg_playtime',
    'med_playtime',
    'release_year'
]
cluster_numeric = (
    df
    .groupby('cluster')[numeric_cols]
    .agg(['mean', 'median', 'std', 'count'])
    .round(2)
)
print("\n=== Numeric Summary by Cluster ===")
print(cluster_numeric)

# — 2) Top 10 user-defined tags per cluster —
tags = (
    df[['cluster', 'user_tags']]
    .assign(tag_list=lambda d: d['user_tags'].fillna('').str.split('|'))
    .explode('tag_list')
)
tags = tags[tags['tag_list'] != '']  # drop empty
tag_counts = (
    tags
    .groupby(['cluster', 'tag_list'])
    .size()
    .reset_index(name='count')
)
top_tags = (
    tag_counts
    .sort_values(['cluster', 'count'], ascending=[True, False])
    .groupby('cluster')
    .head(10)
)
print("\n=== Top 10 User Tags by Cluster ===")
for c in sorted(top_tags['cluster'].unique()):
    print(f"\nCluster {c}:")
    subset = top_tags[top_tags['cluster']==c]
    for _, row in subset.iterrows():
        print(f"  {row['tag_list']} ({row['count']})")

# — 3) Top 10 official genres per cluster —
genres = (
    df[['cluster', 'genres_official']]
    .assign(genre_list=lambda d: d['genres_official'].fillna('').str.split('|'))
    .explode('genre_list')
)
genres = genres[genres['genre_list'] != '']
genre_counts = (
    genres
    .groupby(['cluster', 'genre_list'])
    .size()
    .reset_index(name='count')
)
top_genres = (
    genre_counts
    .sort_values(['cluster', 'count'], ascending=[True, False])
    .groupby('cluster')
    .head(10)
)
print("\n=== Top 10 Official Genres by Cluster ===")
for c in sorted(top_genres['cluster'].unique()):
    print(f"\nCluster {c}:")
    subset = top_genres[top_genres['cluster']==c]
    for _, row in subset.iterrows():
        print(f"  {row['genre_list']} ({row['count']})")
