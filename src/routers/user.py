from fastapi import APIRouter, HTTPException
from src.models.tweet import Tweet
from src.services import user_service 
from src.models.hello import Hello


router = APIRouter(
    prefix='/user',
)

@router.get("/", response_model=Hello)
async def example_user_route():
    return Hello(message="user!")

@router.get("/{username}")
async def user_data_from_username(username: str):
    return user_service.user_data_by_username_service(username)
    # return username



