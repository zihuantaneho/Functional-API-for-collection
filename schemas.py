# Pydantic-схеми
from typing import List, Optional
from pydantic import BaseModel

class ContributionBase(BaseModel):
    user_name: str
    amount: float

class ContributionCreate(ContributionBase):
    pass

class Contribution(ContributionBase):
    id: int
    class Config:
        orm_mode = True

class CollectionBase(BaseModel):
    title: str
    description: Optional[str] = None
    target_amount: float
    link: Optional[str] = None

class CollectionCreate(CollectionBase):
    pass

class Collection(CollectionBase):
    id: int
    contribution: List[Contribution] = []

    class Config:
        orm_mode = True