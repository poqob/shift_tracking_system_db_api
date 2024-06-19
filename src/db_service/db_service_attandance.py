from src.model.attandance import Attandance
import configparser
from typing import List
import sqlite3


class AttandanceDbService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def add(self, attandance: Attandance):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO attandance (person_id, entrance, exit, shift_id)
            VALUES (?, ?, ?, ?)
            """,
            (
                attandance.person_id,
                attandance.entrance,
                attandance.exit,
                attandance.shift_id,
            ),
        )
        conn.commit()
        conn.close()

    def delete(self, attandance_id: int):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM attandance WHERE id = ?
            """,
            (attandance_id,),
        )
        conn.commit()
        conn.close()

    def update(self, attandance: Attandance):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE attandance SET person_id = ?, entrance = ?, exit = ?, shift_id = ?
            WHERE id = ?
            """,
            (
                attandance.person_id,
                attandance.entrance,
                attandance.exit,
                attandance.shift_id,
                attandance.id,
            ),
        )
        conn.commit()
        conn.close()

    def get_all(self) -> List[Attandance]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM attandance
            """
        )
        result = cursor.fetchall()
        attandance_list = []
        for row in result:
            attandance = Attandance(
                id=row[0],
                person_id=row[1],
                entrance=row[2],
                exit=row[3],
                shift_id=row[4],
            )
            attandance_list.append(attandance)
        conn.close()
        return attandance_list

    def get_by_id(self, attandance_id: int) -> Attandance:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM attandance WHERE id = ?
            """,
            (attandance_id,),
        )
        result = cursor.fetchone()
        attandance = Attandance(
            id=result[0],
            person_id=result[1],
            entrance=result[2],
            exit=result[3],
            shift_id=result[4],
        )
        conn.close()
        return attandance

    def get_by_person_id(self, person_id: int) -> List[Attandance]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM attandance WHERE person_id = ?
            """,
            (person_id,),
        )
        result = cursor.fetchall()
        attandance_list = []
        for row in result:
            attandance = Attandance(
                id=row[0],
                person_id=row[1],
                entrance=row[2],
                exit=row[3],
                shift_id=row[4],
            )
            attandance_list.append(attandance)
        conn.close()
        return attandance_list

    def get_by_shift_id(self, shift_id: int) -> List[Attandance]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM attandance WHERE shift_id = ?
            """,
            (shift_id,),
        )
        result = cursor.fetchall()
        attandance_list = []
        for row in result:
            attandance = Attandance(
                id=row[0],
                person_id=row[1],
                entrance=row[2],
                exit=row[3],
                shift_id=row[4],
            )
            attandance_list.append(attandance)
        conn.close()
        return attandance_list

    def get_by_person_id_and_shift_id(
        self, person_id: int, shift_id: int
    ) -> List[Attandance]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM attandance WHERE person_id = ? AND shift_id = ?
            """,
            (person_id, shift_id),
        )
        result = cursor.fetchall()
        attandance_list = []
        for row in result:
            attandance = Attandance(
                id=row[0],
                person_id=row[1],
                entrance=row[2],
                exit=row[3],
                shift_id=row[4],
            )
            attandance_list.append(attandance)
        conn.close()
        return attandance_list
