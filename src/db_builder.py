import sqlite3
import configparser


class DbBuilder:
    config = configparser.ConfigParser()
    config.read("../config/config.ini")
    db_address = config["database"]["path"]
    name = config["database"]["name"]

    def create_database(self):
        conn = sqlite3.connect(self.db_address)
        cursor = conn.cursor()

        # shifts table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS shifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entrance TIMESTAMP,
                exit TIMESTAMP
            )
        """
        )

        # shift table default values
        cursor.execute(
            """
             insert into shifts (entrance,exit) values ('2021-01-01 00:00:00','2021-01-01 08:00:00');
             insert into shifts (entrance,exit) values ('2021-01-01 08:00:00','2021-01-01 17:00:00');
             insert into shifts (entrance,exit) values ('2021-01-01 17:00:00','2021-01-01 00:00:00');
        """
        )

        # personel table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS personels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(20),
                surname VARCHAR(20),
                mail VARCHAR(25),
                password VARCHAR(15),
            )
        """
        )

        # attendance table, its dynamic table
        cursor.execute(
            """
                    CREATE TABLE IF NOT EXISTS attandance (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        person_id INTEGER,
                        entrance TIMESTAMP,
                        exit TIMESTAMP,
                        shift_id INTEGER,
                        FOREIGN KEY (person_id) REFERENCES personels(id),
                        FOREIGN KEY (shift_id) REFERENCES shifts(id)
                    )
                """
        )

        # logs, its static table end of the day attandance table will be inserted to logs table
        cursor.execute(
            """
                    CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        person_id INTEGER,
                        entrance TIMESTAMP,
                        exit TIMESTAMP,
                        shift_id INTEGER,
                        FOREIGN KEY (person_id) REFERENCES personels(id),
                        FOREIGN KEY (shift_id) REFERENCES shifts(id)
                    )
                """
        )

        conn.commit()
        conn.close()
