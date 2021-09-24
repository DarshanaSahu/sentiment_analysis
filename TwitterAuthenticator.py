from tweepy import OAuthHandler

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler("API_KEY", "API_KEY_SECRET")
        auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")
        return auth