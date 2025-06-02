import requests
import pandas as pd

url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
response = requests.get(url)
data = response.json()

apps = pd.DataFrame(data['applist']['apps'])
apps.to_csv('steam_apps.csv', index=False)
print(f"Saved {len(apps)} apps.")