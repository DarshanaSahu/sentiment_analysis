## Purpose of this is to analyze the sentiment of the tweets on the user timeline

## To run this we need to have a twitter developers account and create a project

## Once you have created a project. Go to keys and token and replace API_KEY, API_KEY_SECRET, ACCESS_TOKEN and ACCESS_TOKEN_SECRET resp. in the TwitterAuthenticator.py

## On the terminal run following to install numpy, pandas and tweepy

### `pip install numpy`
### `pip install pandas`
### `pip install tweepy`

## Run SentimentAnalysis.py script 

## It will ask you for the screen name of the user(whom you want to analyze the tweets)

## If the user exists then it will create a csv with name tweets_sentiment_analysis.csv and column sentiment will show the sentiment of the tweet

## Sentiment 1, 0 and -1 represents positive, neutral and negative resp

## If the user does not exists then it will fail with the error msg "Error on fetching user timeline: error_msg"