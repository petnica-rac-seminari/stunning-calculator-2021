from pydantic import BaseModel
from typing import List

class ImageObject(BaseModel):
    image: List[int] = None