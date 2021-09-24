from TwitterClient import TwitterClient
from TweetAnalyzer import TweetAnalyzer
import numpy as np

if __name__ == "__main__":
    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    api = twitter_client.get_twitter_client_api()
    twitter_screen_name = input("Enter twitter screen name to analyze sentiment of tweets: ")
    try:
        tweets = api.user_timeline(screen_name=twitter_screen_name, count=200)
        df = tweet_analyzer.tweets_to_data_frame(tweets)
        df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
        df.to_csv('tweets_sentiment_analysis.csv')
    except BaseException as e:
            print("Error on fetching user timeline: %s" % str(e))
    