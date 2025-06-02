import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
import os

# Load and clean app list
apps = pd.read_csv("steam_apps.csv")
apps["appid"] = pd.to_numeric(apps["appid"], errors='coerce')
apps = apps.dropna(subset=["name"])
apps = apps.dropna(subset=["appid"])
apps = apps[~apps['name'].str.lower().str.contains("test")]
apps = apps[apps["appid"] > 100000]  # Remove legacy/test apps
apps = apps.drop_duplicates(subset=["appid"]).reset_index(drop=True)

# Output file
OUTPUT_FILE = "horror_games.csv"
SAVE_INTERVAL = 100  # Save every 100 games

# Shared list for results
horror_games = []

# Function to check for horror tag
def check_horror(row):
    appid = row["appid"]
    name = row["name"]
    url = f"https://store.steampowered.com/app/{appid}/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.content, "html.parser")
        tags = soup.find_all("a", class_="app_tag")
        for tag in tags:
            if "Horror" in tag.text:
                print(f"✅ {name}")
                return {"appid": appid, "name": name}
    except Exception as e:
        print(f"⚠️ Error for {name}: {e}")

    print(f"❌ Skipping: {name}")
    return None

# Main loop using ThreadPoolExecutor
def run_parallel_filter():
    global horror_games
    start = 0
    total = len(apps)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_index = {executor.submit(check_horror, row): idx for idx, row in apps.iterrows()}
        for i, future in enumerate(concurrent.futures.as_completed(future_to_index)):
            result = future.result()
            if result:
                horror_games.append(result)

            # Save every SAVE_INTERVAL games
            if (i + 1) % SAVE_INTERVAL == 0:
                df = pd.DataFrame(horror_games)
                df.to_csv(OUTPUT_FILE, index=False)
                print(f"💾 Autosaved after {i + 1} checks")

    # Final save
    pd.DataFrame(horror_games).to_csv(OUTPUT_FILE, index=False)
    print(f"🎉 Done! Total horror games: {len(horror_games)}")

if __name__ == "__main__":
    run_parallel_filter()
