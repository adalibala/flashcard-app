# Defining data models
from datetime import datetime
import sqlite3
import fastapi

class CardDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("flashcards-app.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY,
                front_text TEXT NOT NULL,
                back_text TEXT NOT NULL,
                occurence_datetime TEXT
            );
        """)
        self.connection.commit()

    def insert_card(self, front_text, back_text, occurence_datetime, card_id=None):
        self.cursor.execute(
            "INSERT INTO cards (id, front_text, back_text, occurence_datetime) VALUES (?, ?, ?, ?)",
            (card_id, front_text, back_text, occurence_datetime)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def select_queued_cards(self, occurence_datetime):
        self.cursor.execute(
            "SELECT * FROM cards WHERE occurence_datetime <= ?",
            (occurence_datetime,)
        )
        return self.cursor.fetchall()

    def update_front_text(self, card_id, front_text):
        self.cursor.execute(
            "UPDATE cards SET front_text = ? WHERE id = ?",
            (front_text, card_id)
        )
        self.connection.commit()
        return self.cursor.rowcount

    def update_back_text(self, card_id, back_text):
        self.cursor.execute(
            "UPDATE cards SET back_text = ? WHERE id = ?",
            (back_text, card_id)
        )
        self.connection.commit()
        return self.cursor.rowcount

    def update_occurence(self, card_id, occurence_datetime):
        self.cursor.execute(
            "UPDATE cards SET occurence_datetime = ? WHERE id = ?",
            (occurence_datetime, card_id)
        )
        self.connection.commit()
        return self.cursor.rowcount

    def delete_card(self, card_id):
        self.cursor.execute("DELETE FROM cards WHERE id = ?", (card_id,))
        self.connection.commit()
        return self.cursor.rowcount

# Defining API endpoints
def create_card(front_text: str, back_text):
    db = CardDatabase()
    return db.insert_card(front_text, back_text, datetime.now())

def get_cards():
    db = CardDatabase()
    result = db.select_queued_cards(datetime.now())
    return result

def update_front_text(front_text: str):
    db = CardDatabase()
    db.update_front_text(front_text)

def update_back_text(back_text: str):
    db = CardDatabase()
    db.update_back_text(back_text)

def update_occurence(occurence_datetime: str):
    db = CardDatabase()
    db.update_occurence(occurence_datetime)

def delete_card(card_id: int):
    db = CardDatabase()
    db.delete_card(card_id)

def main() -> None:
    create_card("What keyword is used to fetch cards from SQL", "SELECT")
    print(get_cards())
