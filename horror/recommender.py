import pandas as pd
import matplotlib.pyplot as plt


#returns a dataframe of games based on user input
def recommend_games(game_name, price_max = float('Inf'), min_score = 0):
    df = pd.read_csv("horror_games_clustered_250.csv")
    #My main segment checks for this, but this allows this code to be called outside this file
    game = df[df['name'] == game_name]
    if(game.size == 0):
        return game
    df = df[(df["cluster"] == game.iloc[0]["cluster"]) & 
        (df["price_usd"] <= price_max) & 
        (df["review_score"] >= min_score) &
        (df["name"] != game_name)]
    df = df.sort_values(by='review_score',ascending=False)
    return df

def main():
    df = pd.read_csv("horror_games_clustered_100.csv")
    game = input("Please enter a game you'd like your recommendations to be based on: ")
    if(df[df["name"] == game].size == 0):
        print("Unable to find that game. It may not be in our database. Please ensure the game title matches the steam store page.")
        return
    price = input("Game found!\nEnter a maximum price in USD or press enter: ")
    score = input("Enter a minimum review score as a decimal or press enter: ")
    rec_num = input("Enter the number of reccommendations you want or press enter for 5: ")
    #Ensures that input will be correct
    price = float(price) if price else float('inf')
    score = float(score) if score else 0
    rec_num = int(rec_num) if rec_num else 5

    recs = recommend_games(game, price, score)
    if(recs.size == 0):
        print("Unable to find any games matching the criteria.")
        return
    recs = recs.rename(columns={
    "name": "Game Title",
    "price_usd": "Price (USD)",
    "developers": "Developer",
    "publishers": "Publisher",
    "review_score": "Review Score"
})
    print(f"Here is a list of games that may be similar to {game}")
    print(recs[["Game Title", "Price (USD)", "Developer", "Publisher","Review Score"]].head(rec_num).to_string(index=False))

if __name__ == "__main__":
    main()