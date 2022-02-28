from ast import keyword
from src.models.hello import Hello
from fastapi import HTTPException
from src.twitter_handler import user_tweets, analytics, user_id

def tweet_service():
    return Hello(message='hello!')

def get_user_tweets_service(id, max_results=10):
    tweets = user_tweets.get_user_tweets(id, max_results=max_results)
    return tweets

def user_word_frequencies_service(id, max_results=10):
    # Fetch and parse data
    data = user_tweets.get_parsed_user_tweets(id, max_results=max_results)
    # Calculate word frequencies
    word_frequencies = analytics.word_frequency(data)
    return word_frequencies

def user_keywords_analytics_service(id, max_results=10):
    # Fetch and parse data
    data = user_tweets.get_parsed_user_tweets(id,max_results=max_results)
    # Get data keywords list
    keywords_list = analytics.keyword_analytics(data)
    return keywords_list


