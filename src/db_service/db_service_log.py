from src.model.log import Log
import configparser
from typing import List
import sqlite3


# log service copies attandance table directly and stores it after
# personel done with work and leaves the building.
class LogService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def add(self, log: Log):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO logs (person_id, entrance, exit, shift_id)
            VALUES (?, ?, ?, ?)
            """,
            (
                log.person_id,
                log.entrance,
                log.exit,
                log.shift_id,
            ),
        )
        conn.commit()
        conn.close()

    def delete(self, log_id: int):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM logs WHERE id = ?
            """,
            (log_id,),
        )
        conn.commit()
        conn.close()

    def get_all(self) -> List[Log]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM logs
            """
        )
        result = cursor.fetchall()
        conn.close()
        logs = []
        for row in result:
            log = Log(
                id=row[0],
                person_id=row[1],
                entrance=row[2],
                exit=row[3],
                shift_id=row[4],
            )
            logs.append(log)
        return logs

    def get_by_person_id(self, person_id: int) -> List[Log]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM logs WHERE person_id = ?
            """,
            (person_id,),
        )
        result = cursor.fetchall()
        conn.close()
        logs = []
        for row in result:
            log = Log(
                id=row[0],
                person_id=row[1],
                entrance=row[2],
                exit=row[3],
                shift_id=row[4],
            )
            logs.append(log)
        return logs

    def get_log_by_id(self, log_id: int) -> Log:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM logs WHERE id = ?
            """,
            (log_id,),
        )
        result = cursor.fetchone()
        conn.close()
        log = Log(
            id=result[0],
            person_id=result[1],
            entrance=result[2],
            exit=result[3],
            shift_id=result[4],
        )
        return log
