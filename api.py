from flask import Flask, json, render_template
import tweepy
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

app = Flask(__name__)


@app.route('/pybay_tweets')
def bay_tweets():
    return render_template('pybay_tweets.html', tweets=get_tweets('py_bay', 20))


@app.route('/api/pybay_recent_tweets')
def bay_recent_tweets():
    response = app.response_class(
        response=json.dumps(get_tweets('py_bay', 5)),
        status=200,
        mimetype='application/json'
    )
    return response
 

def get_tweets(twitter_id, count):
    auth_api = get_auth_api()
    tweets = auth_api.user_timeline(id=twitter_id, count=count)
    return [{
                'tweet': tweet.text,
                'created_at': tweet.created_at,
                'username': twitter_id,
                'headshot_url': tweet.user.profile_image_url
            } for tweet in tweets]


def get_auth_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)
