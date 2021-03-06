import tweepy, config

class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.text)

words = ["#happy"]
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=words, async=False)
