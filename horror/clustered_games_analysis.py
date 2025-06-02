import pandas as pd
import numpy as np
import sys

# Load clustered dataset
num_clusters = 250

df = pd.read_csv(f'horror_games_clustered_{num_clusters}.csv')
print(df.dtypes)

# breakup tags and genres into lists
df["user_tags"] = df["user_tags"].str.split("|")
df["genres_official"] = df["genres_official"].str.split("|")

# fix year 0 release year
df["release_year"] = df["release_year"].replace(0, np.nan)

# Give stats on dataset
max_rows = 20
def print_stats(df):
    print(df.describe())
    print("\nGenre Relative Frequency:\n" , df["genres_official"].explode().value_counts().iloc[:max_rows]/df.shape[0])
    print("\nTag Relative Frequency:\n", df['user_tags'].explode().value_counts().iloc[:max_rows] / df.shape[0])

pd.set_option('display.max_columns', None)
with open(f"{num_clusters}_cluster_analysis.txt", "w") as sys.stdout:
    # Whole dataset
    print("\n~~~Whole Dataset~~~")
    print_stats(df)
    print("\n")

    #Summarizes clusters in dataset
    cluster_summary = []
    for i in range(num_clusters):
        cluster_data = df[df["cluster"] == i]
        cluster_summary.append({
                        "Cluster ID": i,
                        "Size": cluster_data.shape[0],
                        "Average Review Score": cluster_data["review_score"].mean(),
                        "Average Price (USD)": cluster_data["price_usd"].mean()
                        })
    df2 = pd.DataFrame(cluster_summary)

    #Prints the summary for all of the clusters in the dataset
    
    print("~~~Cluster Summary~~~")
    #This lessening with k indicates greater splitting and less miscellaneous categories
    print(f"\nSize Range: {df2['Size'].max()-df2['Size'].min()}")
    #These two increasing with k shows that the groups are getting more specific
    print(f"\nPrice Range: {round(df2['Average Price (USD)'].max()-df2['Average Price (USD)'].min(), 2)}")
    print(f"\nReview Range: {df2['Average Review Score'].max()-df2['Average Review Score'].min()}")
    print(f"\nNumber of Singlets: {df2[df2['Size'] == 1].shape[0]}")
    print(f"\nPercent Singlets: {round((df2[df2['Size'] == 1].shape[0])/num_clusters, 2)}")

    n = 5
    print(f"\nLargest {n}")
    print(df2[["Cluster ID","Size"]].sort_values(by="Size", ascending=False).head(n).to_string(index = False))
    print(f"\nSmallest {n}")
    print(df2[["Cluster ID","Size"]].sort_values(by="Size").head(n).to_string(index = False))
    print(f"\nTop {n} Average Review Score")
    print(df2[["Cluster ID","Average Review Score"]].sort_values(by="Average Review Score", ascending=False).head(n).to_string(index = False))
    print(f"\nBottom {n} Average Review Score")
    print(df2[["Cluster ID","Average Review Score"]].sort_values(by="Average Review Score").head(n).to_string(index = False))
    print(f"\nTop {n} Most Expensive")
    print(df2[["Cluster ID","Average Price (USD)"]].sort_values(by="Average Price (USD)", ascending=False).head(n).to_string(index = False))


    # Stats on each cluster
    for i in range(num_clusters):
        print(f"~~~Cluster {i}~~~")
        print_stats(df[df["cluster"] == i])
        print("\n")


# OBSERVATIONS on 5 cluster
# C0 (4): NAVAL 100%

# C1 (3198): everything else

# C2 (1371): 64% Story Rich, 50% Atmospheric

# C3 (26): 69% Strategy, 69% Simulation

# C4 (1): Movavi Video Editor Plus 2020 - Halloween Pack


# OBSERVATIONS on 10 cluster
# C0 (13): 100% Atmospheric, 92% Singleplayer, 77% First-Person, 69% Submarine (??)

# C1 (1): Movavi Video Editor Plus 2020 - Halloween Pack

# C2 (4): DDLC, Stray, Sons of The Forest, Lethal Company
# THESE ARE LITERALLY THE TOP 4 MOST REVIEWED LMAO

# C3 (1129): 76% Adventure, 72% Singleplayer, 66% Psychological

# C4 (107): 94% Abstract

# C5 (205): 47% Action Roguelike, 41% Roguelike, 40% Roguelite

# C6 (197): 78% Strategy

# C7 (286): 79% Platformer

# C8 (1): RPG Maker MZ - Magnafied Games - Sound of Dread

# C9 (2657): just seems like the leftovers lmao