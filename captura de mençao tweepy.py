import tweepy
import apscheduler
import requests

client = tweepy.Client(
consumer_key="mjhO8zDQ78ftUPVUJypFuX0hx",
consumer_secret="gysUbtDtqJP171MRB20RK3f1oC4QvygsErI1HhB35aM5HKd636",
access_token="1439150108092899331-pDeBFt2i6MsVoDZhzNa423Angizzcy",
access_token_secret="R7x2Tpx7eWItPiGrx85NK5l6ryXLyQCBpLfRpMxLn8eo1",
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMiKYwEAAAAAMrMp2PQn9Bupj%2B1GnbWnbFyEWjg%3DNhqKTmwBBUck6HqNltdXD7P0OHADuIGWifQVOHJzIvXIPDk3Lw"
)

b = client.get_users_mentions(id = 1439150108092899331,max_results = 100)
tweets = print(b)

response = client.create_tweet(text='menção capturada!', in_reply_to_tweet_id=1490042379549777923)
print(response)
