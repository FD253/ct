import sys
import requests
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret, api_key, username

if not api_key:
    payload = {"consumer_key": consumer_key, "consumer_secret": consumer_secret, 
            "access_token_key": access_token_key, "access_token_secret": access_token_secret}

    r = requests.post('http://0.0.0.0:8000/api/v1/credentials/', json=payload)
else:
    tweet_payload = {}
    args = sys.argv[1:]
    if len(args) >= 1:
        tweet_payload['text'] = args[0]
    if len(args) >= 2:
        tweet_payload['image1'] = args[1]
    if len(args) >= 3:
        tweet_payload['image2'] = args[2]
    if len(args) >= 4:
        tweet_payload['image3'] = args[3]
    if len(args) >= 5:
        tweet_payload['image4'] = args[4]
    r = requests.post('http://0.0.0.0:8000/api/v1/tweet/?username={}&api_key={}'.format(username, api_key), json=tweet_payload)
