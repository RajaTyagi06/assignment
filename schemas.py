from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
