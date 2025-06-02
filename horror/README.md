# BigDataCPH25
Group project for big data class
# 🎮 Clustering Horror Games Using Steam Data

This project explores the application of Big Data collection, feature engineering, and unsupervised machine learning to discover hidden structures within horror games on the Steam platform.We extracted and enriched metadata for over 4,600 horror games, clustered them based on gameplay, tags, and market features, and visualized their relationships using PCA and t-SNE.

## Methods Used

APIs/Scraping: Steam Store API, SteamSpy API, BeautifulSoup (web scraping)

Feature Engineering: Tags, genres, price, reviews, playtime, release year

Clustering: K-Means clustering + Elbow Method

Dimensionality Reduction: PCA and t-SNE for 2D visualizations

Libraries Used:pandas, numpy, scikit-learn, matplotlib, BeautifulSoup4, requests

## 🔍 Project Structure

This project uses a combination of numerical and categorical features:

File/Folder                         Purpose
all_games.py                        Gets initial list of all games on steam
filter_horror_games.py:             Filters full Steam game list to horror-only games
tag_games.py                        Scrapes user tags and review summaries
feature_matrix.py                   Creates a cleaned, scaled feature matrix
K_means_clustering.py               Applies K-Means clustering to feature matrix
clustered_games_analysis.py         Analyzes top tags, genres, numeric summaries per cluster
horror_games.csv                    Initial list of horror games
horror_games_enriched_full_new.csv  Full enriched dataset
horror_games_clustered_10.csv       Final dataset with cluster labels
visualization_cluster.py            Visualizes results with PCA and t-SNE
recommender.py                      Uses clustering results to recommend games to user
old_versions                        Contains archived files that became obsolete during project completion

## How to Run 

Install dependencies:

pip install pandas scikit-learn beautifulsoup4 matplotlib requests

Run scripts in order:

all_games.py

filter_horror_games.py

tag_games.py

feature_matrix.py

K_means_clustering.py

clustered_games_analysis.py

Visualizations (optional but recommended):

visualization_cluster.py

Recommender (optional):

Recommender.py

## Key Insights

Strategy, Platformer, Abstract Horror, and Roguelike games form distinct groups.
Remaining mix of strategy games are easily differentiable by playtime and review score (the two are positively correlated).

## Final Deliverables

Cleaned dataset of 4,600+ horror games

Feature matrix with 459 dimensions

K-Means clustering output with 5, 10, 20, or 100 distinct groups

PCA and t-SNE visualizations

Analytical report of cluster profiles and game insights

Recommendation program