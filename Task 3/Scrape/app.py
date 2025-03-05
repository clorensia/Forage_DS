import tweepy
import pandas as pd
import time
from config import BEARER_TOKEN

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to handle rate limits
def make_request_with_retry(client, method, *args, **kwargs):
    max_retries = 5
    retry_delay = 60  # Start with a 60-second delay
    for attempt in range(max_retries):
        try:
            return method(*args, **kwargs)
        except tweepy.errors.TooManyRequests as e:
            print(f"Rate limit exceeded. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff
    raise Exception("Max retries exceeded. Please try again later.")

# Scrape tweets from @CommBank
username = 'CommBank'
user = make_request_with_retry(client, client.get_user, username=username)
user_id = user.data.id

tweets = make_request_with_retry(
    client,
    client.get_users_tweets,
    id=user_id,
    max_results=10,  # Fetch fewer tweets per request
    tweet_fields=['created_at', 'public_metrics', 'entities']
)

# Store tweet data in a list
tweet_data = []
for tweet in tweets.data:
    entities = tweet.entities if tweet.entities else {}
    tweet_data.append({
        'created_at': tweet.created_at,
        'tweet_id': tweet.id,
        'text': tweet.text,
        'likes': tweet.public_metrics['like_count'],
        'retweets': tweet.public_metrics['retweet_count'],
        'replies': tweet.public_metrics['reply_count'],
        'hashtags': [hashtag['tag'] for hashtag in entities.get('hashtags', [])],
        'mentions': [mention['username'] for mention in entities.get('mentions', [])]
    })

# Convert to DataFrame
df = pd.DataFrame(tweet_data)

# Save to CSV for further analysis
df.to_csv('commbank_tweets_v2.csv', index=False)