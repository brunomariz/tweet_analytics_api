from typing import List
import requests
import re
import os

BEARER_TOKEN = os.environ['BEARER_TOKEN']

def get_user_tweets(id, max_results=10):
    headers = {'Authorization': 'Bearer ' + BEARER_TOKEN}
    url = f'https://api.twitter.com/2/users/{id}/tweets?max_results={max_results}'

    r = requests.get(url, headers=headers)
    return r.json()

def get_parsed_user_tweets(id, max_results=10):
    # Fetch tweets
    tweets = get_user_tweets(id, max_results=max_results)
    # Parse data
    data = [item['text'] for item in tweets['data']]
    # Remove hashtags, @ mentions and links from tweets text
    data = [' '.join(re.sub("(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split()) for x in data]

    return data

