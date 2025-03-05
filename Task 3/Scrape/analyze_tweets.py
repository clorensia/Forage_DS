import pandas as pd
from collections import Counter
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('commbank_tweets_v2.csv')

# Basic statistics
print(f"Total Tweets: {len(df)}")
print(f"Average Likes: {df['likes'].mean()}")
print(f"Average Retweets: {df['retweets'].mean()}")
print(f"Average Replies: {df['replies'].mean()}")

# Top 10 tweets by likes
top_likes = df.nlargest(10, 'likes')[['text', 'likes']]
print("Top 10 Tweets by Likes:")
print(top_likes)

# Top 10 hashtags
hashtags = [hashtag for sublist in df['hashtags'].dropna().apply(eval) for hashtag in sublist]
top_hashtags = Counter(hashtags).most_common(10)
print("Top 10 Hashtags:")
print(top_hashtags)

# Sentiment analysis
df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment_category'] = df['sentiment'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
sentiment_counts = df['sentiment_category'].value_counts()
print("Sentiment Analysis:")
print(sentiment_counts)

# Temporal analysis
df['created_at'] = pd.to_datetime(df['created_at'])
df['hour'] = df['created_at'].dt.hour

# Use a list to select multiple columns
hourly_engagement = df.groupby('hour')[['likes', 'retweets', 'replies']].mean()

# Plot hourly engagement
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_engagement.index, y=hourly_engagement['likes'], label='Likes')
sns.lineplot(x=hourly_engagement.index, y=hourly_engagement['retweets'], label='Retweets')
sns.lineplot(x=hourly_engagement.index, y=hourly_engagement['replies'], label='Replies')
plt.title('Hourly Engagement')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Engagement')
plt.legend()
plt.show()