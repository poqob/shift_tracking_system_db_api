from model.personel import Personel
import configparser
from typing import List
import sqlite3


class PersonelService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def add(self, personel: Personel):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO personels (name, surname, mail, password)
            VALUES (?, ?, ?, ?)
            """,
            (personel.name, personel.surname, personel.mail, personel.password),
        )
        conn.commit()
        conn.close()

    def delete(self, personel_id: int):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM personels WHERE id = ?
            """,
            (personel_id,),
        )
        conn.commit()
        conn.close()

    def update(self, personel: Personel):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE personels SET name = ?, surname = ?, mail = ?, password = ?
            WHERE id = ?
            """,
            (
                personel.name,
                personel.surname,
                personel.mail,
                personel.password,
                personel.id,
            ),
        )
        conn.commit()
        conn.close()

    def get_all(self) -> List[Personel]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM personels
            """
        )
        result = cursor.fetchall()
        conn.close()
        personels = []
        for row in result:
            personel = Personel(
                name=row[1], surname=row[2], mail=row[3], password=row[4]
            )
            personels.append(personel)
        return personels

    def get_by_id(self, personel_id: int) -> Personel:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM personels WHERE id = ?
            """,
            (personel_id,),
        )
        result = cursor.fetchone()
        conn.close()

        return Personel(
            name=result[1], surname=result[2], mail=result[3], password=result[4]
        )
