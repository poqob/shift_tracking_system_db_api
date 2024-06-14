# table content: id, entrance_date, exit_date


class Shift:
    def __init__(self, id, entrance_date, exit_date):
        self.id = id
        self.entrance_date = entrance_date
        self.exit_date = exit_date

    @staticmethod
    def parse(json_data):
        id = json_data.get("id")
        entrance_date = json_data.get("entrance_date")
        exit_date = json_data.get("exit_date")
        return Shift(id, entrance_date, exit_date)

    def __str__(self):
        return f"Shift(id={self.id}, entrance_date={self.entrance_date}, exit_date={self.exit_date})"