# table content: id, entrance_date, exit_date


class Shift:
    def __init__(self, id: int=None, entrance_date: str=None, exit_date: str=None):
        self.id = id
        self.entrance_date = entrance_date
        self.exit_date = exit_date

    @staticmethod
    def parse(json_data: dict):
        id = json_data.get("id")
        entrance_date = json_data.get("entrance_date")
        exit_date = json_data.get("exit_date")
        return Shift(id, entrance_date, exit_date)

    def serialize(self):
        return {
            "id": self.id,
            "entrance_date": self.entrance_date,
            "exit_date": self.exit_date,
        }

    def __str__(self):
        return f"Shift(id={self.id}, entrance_date={self.entrance_date}, exit_date={self.exit_date})"
