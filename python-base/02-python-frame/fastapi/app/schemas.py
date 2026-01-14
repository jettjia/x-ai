from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str
    description: str = None
    price: float = Field(..., gt=0)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True