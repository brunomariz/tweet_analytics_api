from typing import List, Optional

from pydantic import BaseModel


class Hello(BaseModel):
    message: str
