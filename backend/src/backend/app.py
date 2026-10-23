from datetime import datetime

from fastapi import FastAPI

from .database import CardDatabase
from .models import (
    Card,
    CreateCardRequestModel,
    CreateCardResponseModel,
    GetCardsResponseModel,
    UpdateCardRequestModel,
)

app = FastAPI()


@app.post("/cards", response_model=CreateCardResponseModel)
def create_card(request: CreateCardRequestModel):
    db = CardDatabase()
    card_id = db.insert_card(request.front_text, request.back_text, datetime.now())
    return {"id": card_id}


@app.get("/cards", response_model=GetCardsResponseModel)
def get_cards():
    db = CardDatabase()
    rows = db.select_queued_cards(datetime.now())
    return {
        "cards": [
            Card(
                id=row[0],
                front_text=row[1],
                back_text=row[2],
                occurence_datetime=row[3],
            )
            for row in rows
        ]
    }


@app.patch("/cards/{card_id}")
def update_card(card_id: int, request: UpdateCardRequestModel):
    if request.front_text is not None:
        update_front_text(card_id, request.front_text)
    if request.back_text is not None:
        update_back_text(card_id, request.back_text)
    if request.occurrence_datetime is not None:
        update_occurence(card_id, request.occurrence_datetime)


def update_front_text(card_id: int, front_text: str):
    db = CardDatabase()
    db.update_front_text(card_id, front_text)


def update_back_text(card_id: int, back_text: str):
    db = CardDatabase()
    db.update_back_text(card_id, back_text)


def update_occurence(card_id: int, occurence_datetime: str):
    db = CardDatabase()
    db.update_occurence(card_id, occurence_datetime)


@app.delete("/cards/{card_id}")
def delete_card(card_id: int):
    db = CardDatabase()
    db.delete_card(card_id)