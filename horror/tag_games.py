# enrich_horror_full.py

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import re

# ————— CONFIG —————
INPUT_CSV    = "horror_games.csv"
OUTPUT_CSV   = "horror_games_enriched_full_new.csv"

# Steam API endpoints
STORE_API    = "https://store.steampowered.com/api/appdetails"
STEAMSPY_API = "https://steamspy.com/api.php"

HEADERS = {"User-Agent": "Mozilla/5.0"}

# ————— HELPER FUNCTIONS —————

def get_store_api_data(appid):
    """Call the Steam Store API to get price, release date, description, dev/pub, genres."""
    params = {"appids": appid, "l": "en"}
    try:
        r = requests.get(STORE_API, params=params, headers=HEADERS, timeout=10)
        data = r.json().get(str(appid), {}).get("data", {})
        price = None
        if data.get("is_free"):
            price = 0.0
        elif "price_overview" in data:
            price = data["price_overview"]["final"] / 100.0

        release = data.get("release_date", {}).get("date", "")
        year = ""
        if release:
            # e.g. "28 Oct, 2022"
            year = release.strip().split()[-1]

        short_desc = data.get("short_description", "").replace("\n", " ").strip()
        devs  = "|".join(data.get("developers", []))
        pubs  = "|".join(data.get("publishers", []))
        genres = "|".join([g["description"] for g in data.get("genres", [])])

        return price, year, short_desc, devs, pubs, genres
    except Exception:
        return None, None, None, None, None, None

def get_steamspy_data(appid):
    """Call SteamSpy to get average and median playtime."""
    params = {"request": "appdetails", "appid": appid}
    try:
        r = requests.get(STEAMSPY_API, params=params, timeout=10)
        data = r.json()
        avg_play = data.get("average_forever")
        med_play = data.get("median_forever")
        return avg_play, med_play
    except Exception:
        return None, None

percent_pattern = re.compile(r'(\d+(?:\.\d+)?)%')
def scrape_store_page(appid):
    """Scrape the Steam store page for user tags, positive review percent, & count."""
    url = f"https://store.steampowered.com/app/{appid}/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.content, "html.parser")

        # user-defined tags
        tags = [t.get_text(strip=True) for t in soup.find_all("a", class_="app_tag")]
        tags = "|".join(tags)

        # review summary + count
        review = soup.find("div", class_="user_reviews_summary_row", itemprop="aggregateRating")
        if not review:
            return tags, None, None
        
        review_count = review.find("meta", itemprop="reviewCount")
        count = int(review_count["content"]) if review_count else None

        percent_span = review.find("span", class_="nonresponsive_hidden responsive_reviewdesc")
        if not percent_span:
            return tags, None, count
        percent_match = percent_pattern.search(percent_span.get_text())
        percent = float(percent_match.group(1)) / 100 if percent_match else None

        return tags, percent, count
    except Exception:
        return None, None, None

# ————— MAIN ENRICH LOOP —————

def main():
    df = pd.read_csv(INPUT_CSV)
    enriched = []

    for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Enriching horror games"):
        appid = int(row["appid"])
        name  = row["name"]

        # 1) Store API data
        price, year, short_desc, devs, pubs, genres = get_store_api_data(appid)

        # 2) SteamSpy data
        avg_play, med_play = get_steamspy_data(appid)

        # 3) Page scrape data
        user_tags, review_score, review_count = scrape_store_page(appid)

        enriched.append({
            "appid":         appid,
            "name":          name,
            "price_usd":     price,
            "release_year":  year,
            "short_desc":    short_desc,
            "developers":    devs,
            "publishers":    pubs,
            "genres_official": genres,
            "user_tags":     user_tags,
            "review_score": review_score,
            "review_count":  review_count,
            "avg_playtime":  avg_play,
            "med_playtime":  med_play,
        })

      
    # save out
    enriched_df = pd.DataFrame(enriched)
    enriched_df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ All done — enriched data saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
