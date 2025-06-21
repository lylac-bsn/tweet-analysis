from textblob import TextBlob
import pandas as pd
from fetch_tweets import fetch_tweets

def get_sentiment(text):
    """Analyzes sentiment of a tweet using TextBlob."""
    score = TextBlob(text).sentiment.polarity
    return "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"

def analyze_and_save(keyword="AI images", count=50):
    """Fetches tweets, analyzes sentiment, and saves results to CSV."""
    tweets = fetch_tweets(keyword, count)
    
    tweet_list = []
    for tweet in tweets:
        sentiment = get_sentiment(tweet.text)
        tweet_list.append([tweet.created_at, tweet.text, sentiment])
    
    df = pd.DataFrame(tweet_list, columns=["Date", "Tweet", "Sentiment"])
    df.to_csv("tweets_sentiment.csv", index=False)
    print("✅ Sentiment analysis complete. Results saved to tweets_sentiment.csv")

# Run analysis
if __name__ == "__main__":
    analyze_and_save()
