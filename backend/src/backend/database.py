import sqlite3


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

    def select_queued_cards(self, occurence_datetime) -> list[tuple[int, str, str, str]]:
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