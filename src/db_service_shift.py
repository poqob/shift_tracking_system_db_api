from model.shift import Shift
import configparser
from typing import List
import sqlite3


class ShiftService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def add(self, shift: Shift):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO shifts (entrance, exit)
            VALUES (?, ?)
            """,
            (shift.entrance, shift.exit),
        )
        conn.commit()
        conn.close()

    def delete(self, shift_id: int):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM shifts WHERE id = ?
            """,
            (shift_id,),
        )
        conn.commit()
        conn.close()

    def update(self, shift: Shift):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE shifts SET entrance = ?, exit = ?
            WHERE id = ?
            """,
            (
                shift.entrance,
                shift.exit,
                shift.id,
            ),
        )
        conn.commit()
        conn.close()

    def get_all(self) -> List[Shift]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM shifts
            """
        )
        result = cursor.fetchall()
        conn.close()
        shift_list = []
        for row in result:
            shift = Shift(row[0], row[1], row[2])
            shift_list.append(shift)
        return shift_list

    def get_by_id(self, shift_id: int) -> Shift:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM shifts WHERE id = ?
            """,
            (shift_id,),
        )
        result = cursor.fetchone()
        conn.close()
        shift = Shift(result[0], result[1], result[2])
        return shift
