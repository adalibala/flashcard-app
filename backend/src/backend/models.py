from typing import List, Optional

from pydantic import BaseModel


class CreateCardRequestModel(BaseModel):
    front_text: str
    back_text: str


class CreateCardResponseModel(BaseModel):
    id: int


class Card(BaseModel):
    id: int
    front_text: str
    back_text: str
    occurence_datetime: str


class GetCardsResponseModel(BaseModel):
    cards: List[Card]


class UpdateCardRequestModel(BaseModel):
    front_text: Optional[str] = None
    back_text: Optional[str] = None
    occurrence_datetime: Optional[str] = None