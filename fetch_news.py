import feedparser
import os

# Define your RSS Feed (You can use any News RSS)
RSS_URL = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"

def fetch_and_save():
    feed = feedparser.parse(RSS_URL)
    if not feed.entries:
        print("No news found.")
        return

    # Get the latest news
    latest = feed.entries[0]
    title = latest.title
    summary = latest.summary

    # Create a "Human-like" script format
    script = f"Breaking News: {title}. \n\nDetails: {summary} \n\nStay tuned for more updates."

    # Save to a file so the next step can use it
    with open("latest_news.txt", "w", encoding="utf-8") as f:
        f.write(script)
    
    print(f"Successfully saved: {title}")

if __name__ == "__main__":
    fetch_and_save()