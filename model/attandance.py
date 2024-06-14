class Attandance:
    def __init__(
        self, personel_id: int, entrance_time: str, exit_date: str, shift_id: int
    ) -> None:
        self.personel_id = personel_id
        self.entrance_time = entrance_time
        self.exit_date = exit_date
        self.shift_id = shift_id

    @staticmethod
    def parse(json_data):
        personel_id = json_data.get("personel_id")
        entrance_time = json_data.get("entrance_time")
        exit_date = json_data.get("exit_date")
        shift_id = json_data.get("shift_id")
        return Attandance(personel_id, entrance_time, exit_date, shift_id)
