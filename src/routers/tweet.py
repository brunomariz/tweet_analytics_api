from fastapi import APIRouter, HTTPException
from src.models.tweet import Tweet
from src.services import tweet_service 
from src.models.hello import Hello


router = APIRouter(
    prefix='/tweet',
)

@router.get("/", response_model=Hello)
async def example_tweet_route():
    return Hello(message="tweet!")

@router.get("/{id}", response_model=Tweet)
async def user_tweets(id: int):
    return Tweet(tweets=tweet_service.get_user_tweets_service(id, max_results=5))


@router.get("/freq/{id}")
async def user_word_frequency(id: int):
    return tweet_service.user_word_frequencies_service(id, max_results=5)

@router.get("/keywords/{id}")
async def user_keywords_list(id: int):
    return tweet_service.user_keywords_analytics_service(id, max_results=100)
    # from src.utils.example_response import example_keywords
    # return example_keywords


