from pydantic import BaseModel
import numpy as npy

lst = []
for i in range (0,785):
    lst.append(i)

class ImageObject(BaseModel):
    image: list #dogovor sa ML, videcemo
