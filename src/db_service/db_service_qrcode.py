import sqlite3
import configparser
from src.model.qrCode import QrCode
from src.model.actions import Actions
from src.db_service.db_service_actions import DbActionsService
from typing import List


class DbQrcodeService:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database_code"]["path"]
    name = config["database_code"]["name"]

    def add(self, action: Actions, code: str):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO  {} (action, code)
            VALUES (?, ?)
            """.format(
                self.name
            ),
            (action.id, code),
        )

        conn.commit()
        conn.close()

    def delete(self, code: str):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM {self.name} WHERE code = {code}
        """.format(
                self.name, code
            )
        )
        conn.commit()
        conn.close()

    def get_all(self) -> List[QrCode]:
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT * FROM {n} ;
            """.format(
                n=self.name
            )
        )
        result = cursor.fetchall()
        conn.close()

        qr_codes = []
        for row in result:
            action = DbActionsService().get_by_id(id=row[2])
            qr_code = QrCode(
                id=row[0],
                time=row[1],
                action=Actions(id=action.id, name=action.name),
                code=row[3],
            )
            qr_codes.append(qr_code)
        return qr_codes

    def get_by_code(self, code: str) -> QrCode:
        conn = sqlite3.connect(self.db_address)
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM {table_name} WHERE code = ?
            """.format(
                    table_name=self.name
                ),
                (code,),
            )
            result = cursor.fetchone()
            conn.close()
            if result:
                qr_code = QrCode(result[0], result[1])
                return qr_code
            else:
                return None
        except Exception as e:
            print("Error in db_service get_by_code() function:", e)
            return None

    def get_by_action(self, action: Actions):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM {table_name} WHERE action = ?
        """.format(
                table_name=self.name
            ),
            (action.id,),
        )
        result = cursor.fetchall()
        conn.close()
        return result

   