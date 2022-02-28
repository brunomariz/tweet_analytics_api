from fastapi import FastAPI
from src.routers import hello, tweet, user
from fastapi.middleware.cors import CORSMiddleware

from src.twitter_handler import user_tweets

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello.router)
app.include_router(tweet.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello!"}

