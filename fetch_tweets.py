import tweepy

# Replace with your X Developer API credentials
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJgc0AEAAAAAEUdc6BNcUgRxi3i1nwazr0zx1V8%3DdobzWUNa7tYWnTtw4LQ5Zz8ad0jcLXDdYbP0KUbOBVaYVC0mqd"

# Authenticate with Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(keyword, count=50):
    """Fetches recent tweets containing the given keyword."""
    tweets = client.search_recent_tweets(query=keyword, max_results=count, tweet_fields=["text", "created_at"])
    return tweets.data if tweets.data else []
