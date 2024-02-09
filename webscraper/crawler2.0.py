## Needs to be updated, instagram changes the class name often 

## html parsing is out of date

import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find username 
        username_element = soup.find("h1", class_="rhpdm")  # Ensure correct class name
        username = username_element.get_text() if username_element else "Not found"
        
        # Find bio 
        bio_element = soup.find("div", class_="-vDIg")  
        bio = bio_element.get_text() if bio_element else "Not found"
        
        # Find follower count
        follower_count_element = soup.find("meta", {"name": "description"})
        follower_count = "Not found"
        if follower_count_element:
            follower_count_text = follower_count_element["content"]
            follower_count_index = follower_count_text.find("Followers")
            if follower_count_index != -1:  
                follower_count = follower_count_text[:follower_count_index].strip() 
                
        # Following count hard to get with html, would need to update code using js
        
        print(f"Username: {username}")
        print(f"Bio: {bio}")
        print(f"Follower count: {follower_count}")

    else:
        print(f"Failed to scrape Instagram account, status code {response.status_code}")
        
if __name__ == "__main__":
    url = input("Enter the URL of the Instagram account: ")
    crawl_website(url
