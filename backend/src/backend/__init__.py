# Defining data models
from datetime import datetime
import sqlite3
import fastapi

CARD_COUNT = 0

db = {}

class Card:
    def __init__(self, card_id: int, front_text: str, back_text: str, occurence_datetime: str):
        self.card_id = card_id
        self.front_text = front_text
        self.back_text = back_text
        self.occurence_datetime = occurence_datetime

# Defining API endpoints
def createCard(self, front_text: str, back_text):
    card_id = CARD_COUNT
    new_card = Card(
        card_id,
        front_text,
        back_text,
        datetime.now()
    )

    db[card_id] = new_card
    CARD_COUNT += 1

def getCards():
    cards_to_show = []

    for card in db.values():
        now = datetime.now()
        if now >= card.occurence_datetime:
            cards_to_show.append(card)

    return cards_to_show

def updateCard(card_id: int, new_front_text: str, new_back_text: str):
    card_that_needs_update = db[card_id]
    card_that_needs_update.front_text = new_front_text
    card_that_needs_update.back_text = new_back_text

def deleteCard(card_id):
    del db[card_id]

# CRUD = Create, Read, Update, Delete

def main() -> None:
    print("Hello from ada!")