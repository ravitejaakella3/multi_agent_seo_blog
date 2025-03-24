import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_trending_hr_topics():
    """Fetches trending HR-related news articles using NewsAPI."""
    
    # Get API key from environment variables
    API_URL = "https://newsapi.org/v2/top-headlines"
    API_KEY = os.getenv("NEWS_API_KEY")

    if not API_KEY:
        print("❌ Error: NEWS_API_KEY not found in environment variables!")
        return []

    # Parameters for the API request
    params = {
        "country": "us",
        "category": "business",
        "q": "HR",
        "apiKey": API_KEY
    }

    # ✅ Corrected: Removed 'headers' from request
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        articles = response.json().get("articles", [])
        if not articles:
            print("No trending HR articles found.")
            return []
        
        trending_articles = [
            {"title": article["title"], "url": article["url"]}
            for article in articles
        ]
        
        # ✅ Print the fetched articles
        print("\n🔹 Trending HR Articles:")
        for i, article in enumerate(trending_articles[:3]):  # Get top 3 articles
            print(f"{i+1}. {article['title']} - {article['url']}")

        return trending_articles

    else:
        print("❌ Error fetching topics:", response.json())
        return []

if __name__ == "__main__":
    fetch_trending_hr_topics()

