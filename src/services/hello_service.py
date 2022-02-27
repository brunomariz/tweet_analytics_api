from src.models.hello import Hello
from fastapi import HTTPException

def hello_service():
    return Hello(message='hello!')
