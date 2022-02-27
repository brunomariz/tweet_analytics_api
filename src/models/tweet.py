from typing import List, Optional

from pydantic import BaseModel


class Tweet(BaseModel):
    tweets: dict
