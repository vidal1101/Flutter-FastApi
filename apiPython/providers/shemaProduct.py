from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: Optional[int]
    nameproduct:str
    description: str
    price: int
    imageProduct: Optional[int]
    stock: int 

    class Config: 
        orm_mode=True