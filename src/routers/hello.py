from fastapi import APIRouter, HTTPException
from src.services.hello_service import hello_service
from src.models.hello import Hello


router = APIRouter(
    prefix='/hello',
)

@router.get("/", response_model=Hello)
async def example_login_route():
    return hello_service()