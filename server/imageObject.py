from pydantic import BaseModel
from typing import List
import numpy as npy

class ImageObject(BaseModel):
    image: List[int] #dogovor sa ML, videcemo
